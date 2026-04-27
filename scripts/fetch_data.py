#!/usr/bin/env python3
"""
Daily data feed builder for the Investor Dashboard.

Pulls public-record data:
  - Macro snapshot (VIX, 10Y Treasury, S&P 500) via Yahoo Finance
  - Recent SEC filings (10-K, 10-Q, 8-K) per stock via EDGAR
  - Insider transactions (Form 4) parsed for actual purchases vs. routine grants
  - Next earnings dates via Yahoo Finance

Outputs: data/feed.json

No API keys required. SEC's user-agent rule is satisfied via CONTACT_EMAIL env var.
Stdlib only — no pip install needed on the runner.
"""

import json
import os
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import URLError, HTTPError
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET

# ============================================================
# Config
# ============================================================

SYMBOLS = ['MU', 'AVGO', 'PLTR', 'TSLA', 'NVDA']

# SEC's CIK identifiers — stable, public IDs
CIK_MAP = {
    'MU':   '0000723125',
    'AVGO': '0001730168',
    'PLTR': '0001321655',
    'TSLA': '0001318605',
    'NVDA': '0001045810',
}

# SEC requires a User-Agent identifying the requester (with contact info).
CONTACT_EMAIL = os.environ.get('CONTACT_EMAIL', 'investor-dashboard@example.com')
USER_AGENT = f'Investor-Dashboard/1.0 ({CONTACT_EMAIL})'

INSIDER_LOOKBACK_DAYS = 90
FILINGS_LOOKBACK_DAYS = 90

# Output path — repo_root/data/feed.json
OUTPUT_PATH = Path(__file__).resolve().parent.parent / 'data' / 'feed.json'

# Cap how many Form 4 filings to fetch per stock (avoids rate limits & long runs)
MAX_FORM4_PER_STOCK = 25


# ============================================================
# HTTP helpers
# ============================================================

# Browser-like User-Agent for sites (Yahoo, Stooq) that block "bot-looking" requests.
# SEC EDGAR has the opposite policy: they require an identifying email contact.
BROWSER_HEADERS = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/120.0.0.0 Safari/537.36'),
    'Accept': 'application/json, text/plain, text/csv, */*',
    'Accept-Language': 'en-US,en;q=0.9',
}


def http_get(url, headers=None, timeout=30):
    """GET text from URL with proper User-Agent."""
    headers = dict(headers or {})
    headers.setdefault('User-Agent', USER_AGENT)
    headers.setdefault('Accept', 'application/json, text/html, application/xml, */*')
    req = Request(url, headers=headers)
    with urlopen(req, timeout=timeout) as r:
        return r.read().decode('utf-8', errors='replace')


def http_get_json(url, **kw):
    return json.loads(http_get(url, **kw))


def yahoo_get_json(url):
    """Yahoo Finance with browser User-Agent (their endpoint blocks bot-style UAs)."""
    return json.loads(http_get(url, headers=BROWSER_HEADERS))


def sec_throttle():
    """SEC asks for max 10 req/sec from automated tools. Stay well under."""
    time.sleep(0.15)


# ============================================================
# Yahoo Finance — macro & earnings
# ============================================================

def fetch_yahoo_quote(symbol):
    """Return latest price + previous close + daily change % for a symbol."""
    url = f'https://query1.finance.yahoo.com/v8/finance/chart/{symbol}'
    try:
        data = yahoo_get_json(url)
        meta = data['chart']['result'][0]['meta']
        cur = meta.get('regularMarketPrice')
        prev = meta.get('chartPreviousClose') or meta.get('previousClose')
        change_pct = ((cur - prev) / prev * 100) if (cur and prev) else None
        return {
            'value': round(cur, 4) if cur else None,
            'previous': round(prev, 4) if prev else None,
            'change_pct': round(change_pct, 2) if change_pct is not None else None,
        }
    except Exception as e:
        print(f'  ! Yahoo quote {symbol}: {e}', file=sys.stderr)
        return None


def fetch_macro_snapshot():
    """VIX, 10Y Treasury yield, S&P 500."""
    return {
        'vix':            fetch_yahoo_quote('^VIX'),
        'ten_year_yield': fetch_yahoo_quote('^TNX'),
        'sp500':          fetch_yahoo_quote('^GSPC'),
    }


def fetch_next_earnings(symbol):
    """Next earnings date (YYYY-MM-DD) from Yahoo's quoteSummary endpoint."""
    url = (f'https://query2.finance.yahoo.com/v10/finance/quoteSummary/{symbol}'
           f'?modules=calendarEvents')
    try:
        data = yahoo_get_json(url)
        cal = data['quoteSummary']['result'][0]['calendarEvents']
        dates = cal.get('earnings', {}).get('earningsDate', [])
        if dates and dates[0].get('raw'):
            return datetime.fromtimestamp(
                dates[0]['raw'], tz=timezone.utc
            ).strftime('%Y-%m-%d')
    except Exception as e:
        print(f'  ! Yahoo earnings {symbol}: {e}', file=sys.stderr)
    return None


# ============================================================
# SEC EDGAR — filings list
# ============================================================

def sec_recent_filings(cik):
    """Return list of recent filings for a CIK. Stable, official endpoint."""
    cik_padded = cik.lstrip('0').zfill(10)
    url = f'https://data.sec.gov/submissions/CIK{cik_padded}.json'
    sec_throttle()
    try:
        data = http_get_json(url)
    except Exception as e:
        print(f'  ! SEC submissions {cik}: {e}', file=sys.stderr)
        return []

    recent = data.get('filings', {}).get('recent', {})
    forms = recent.get('form', [])
    dates = recent.get('filingDate', [])
    accessions = recent.get('accessionNumber', [])
    primary_docs = recent.get('primaryDocument', [])

    out = []
    for i in range(len(forms)):
        out.append({
            'form':        forms[i],
            'date':        dates[i],
            'accession':   accessions[i],
            'primary_doc': primary_docs[i],
            'cik_int':     int(cik),
        })
    return out


def filing_url(filing):
    """URL to the filing's primary document on EDGAR."""
    acc = filing['accession'].replace('-', '')
    return (f'https://www.sec.gov/Archives/edgar/data/'
            f'{filing["cik_int"]}/{acc}/{filing["primary_doc"]}')


def filing_dir_url(filing):
    """URL to the filing's directory listing (contains all docs)."""
    acc = filing['accession'].replace('-', '')
    return f'https://www.sec.gov/Archives/edgar/data/{filing["cik_int"]}/{acc}/'


def filter_material_filings(filings, lookback_days=FILINGS_LOOKBACK_DAYS):
    """Keep only material filings (10-K, 10-Q, 8-K) within lookback window."""
    cutoff = (datetime.now(timezone.utc) - timedelta(days=lookback_days)).strftime('%Y-%m-%d')
    descriptions = {
        '10-K': 'Annual report',
        '10-Q': 'Quarterly report',
        '8-K':  'Material event',
    }
    out = []
    for f in filings:
        if f['date'] < cutoff:
            continue
        if f['form'] in descriptions:
            out.append({
                'date':        f['date'],
                'type':        f['form'],
                'description': descriptions[f['form']],
                'url':         filing_url(f),
            })
    return out[:10]


# ============================================================
# SEC EDGAR — Form 4 (insider transactions) parsing
# ============================================================

def find_text(elem, path):
    """Form 4 schemas wrap simple values in <value> child nodes."""
    if elem is None:
        return None
    node = elem.find(path)
    if node is None:
        return None
    val = node.find('value')
    return (val.text if val is not None else node.text) or None


def parse_form4_xml(xml_text):
    """Parse Form 4 XML, extracting owner identity and non-derivative transactions."""
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return None

    # Owner identity
    owner = root.find('reportingOwner')
    name = find_text(owner, 'reportingOwnerId/rptOwnerName')
    rel = owner.find('reportingOwnerRelationship') if owner is not None else None
    title = find_text(rel, 'officerTitle')
    is_director = (find_text(rel, 'isDirector') or '').strip().lower() in ('1', 'true')
    is_officer  = (find_text(rel, 'isOfficer')  or '').strip().lower() in ('1', 'true')
    is_ten_pct  = (find_text(rel, 'isTenPercentOwner') or '').strip().lower() in ('1', 'true')

    roles = []
    if title:
        roles.append(title)
    elif is_officer:
        roles.append('Officer')
    if is_director:
        roles.append('Director')
    if is_ten_pct:
        roles.append('10%+ Owner')
    role = ', '.join(roles) or 'Insider'

    # Non-derivative transactions = actual share purchases/sales
    transactions = []
    for tx in root.iterfind('nonDerivativeTable/nonDerivativeTransaction'):
        date   = find_text(tx, 'transactionDate')
        code   = find_text(tx, 'transactionCoding/transactionCode')
        shares = find_text(tx, 'transactionAmounts/transactionShares')
        price  = find_text(tx, 'transactionAmounts/transactionPricePerShare')
        ad     = find_text(tx, 'transactionAmounts/transactionAcquiredDisposedCode')

        try:
            shares_n = float(shares) if shares else 0.0
            price_n = float(price) if price else 0.0
        except (TypeError, ValueError):
            shares_n = 0.0
            price_n = 0.0

        transactions.append({
            'date':      date,
            'code':      code,    # P=purchase, S=sale, A=grant, M=option exercise, F=tax, G=gift
            'shares':    shares_n,
            'price':     price_n if price_n else None,
            'value':     shares_n * price_n,
            'direction': 'buy' if ad == 'A' else 'sell' if ad == 'D' else None,
        })

    return {'name': name, 'role': role, 'transactions': transactions}


def fetch_form4_xml(filing):
    """Find and fetch the actual XML for a Form 4 filing.

    SEC stores each submission in a directory. The XML may be the primary doc,
    or a sibling file in the same directory. We try the primary doc first, then
    fall back to scanning the directory.
    """
    primary_url = filing_url(filing)
    sec_throttle()
    try:
        text = http_get(primary_url)
    except Exception as e:
        print(f'  ! Form 4 primary fetch {filing["accession"]}: {e}', file=sys.stderr)
        return None

    if '<ownershipDocument' in text:
        return text

    # Otherwise look for an XML file in the directory listing
    try:
        sec_throttle()
        index_text = http_get(filing_dir_url(filing))
        # Find candidate XML files (Form 4 XML files often have these patterns)
        candidates = re.findall(r'href="([^"]+\.xml)"', index_text)
        for c in candidates:
            fname = c.split('/')[-1]
            if not fname.lower().endswith('.xml'):
                continue
            # Skip schema/index files
            if fname.lower() in ('xbrlrss.xml', 'index.xml'):
                continue
            xml_url = filing_dir_url(filing) + fname
            sec_throttle()
            xml_text = http_get(xml_url)
            if '<ownershipDocument' in xml_text:
                return xml_text
    except Exception as e:
        print(f'  ! Form 4 dir scan {filing["accession"]}: {e}', file=sys.stderr)

    return None


def summarize_insider_activity(form4_filings, lookback_days=INSIDER_LOOKBACK_DAYS):
    """Summarize Form 4 filings into purchases vs. sales over the lookback window.

    Only counts open-market purchases (code P) and open-market sales (code S).
    Excludes routine grants (A), option exercises (M), tax withholding (F),
    gifts (G), and other non-discretionary transactions.
    """
    cutoff = (datetime.now(timezone.utc) - timedelta(days=lookback_days)).strftime('%Y-%m-%d')
    purchases = []
    sales = []

    for f in form4_filings:
        if f['date'] < cutoff:
            break  # Filings come back sorted descending
        xml = fetch_form4_xml(f)
        if not xml:
            continue
        details = parse_form4_xml(xml)
        if not details:
            continue
        for tx in details['transactions']:
            if not tx.get('shares') or not tx.get('code'):
                continue
            entry = {
                'date':   tx['date'] or f['date'],
                'name':   details['name'],
                'role':   details['role'],
                'shares': int(tx['shares']),
                'price':  round(tx['price'], 2) if tx['price'] else None,
                'value':  int(round(tx['value'])),
                'url':    filing_url(f),
            }
            if tx['code'] == 'P':
                purchases.append(entry)
            elif tx['code'] == 'S':
                sales.append(entry)

    purchases.sort(key=lambda e: e['date'], reverse=True)
    sales.sort(key=lambda e: e['date'], reverse=True)

    return {
        'lookback_days':     lookback_days,
        'purchases':         purchases,
        'sales':             sales,
        'purchase_count':    len(purchases),
        'purchase_value':    sum(p['value'] for p in purchases),
        'sale_count':        len(sales),
        'sale_value':        sum(s['value'] for s in sales),
        'unique_purchasers': len({p['name'] for p in purchases}),
        'unique_sellers':    len({s['name'] for s in sales}),
    }


# ============================================================
# Price history & technical indicators
# ============================================================

def fetch_yahoo_history(symbol, range_='5y'):
    """Fetch daily OHLCV history from Yahoo Finance.

    Returns list of dicts: [{date, open, high, low, close, volume}, ...]
    Uses browser User-Agent because Yahoo's endpoints block bot-style UAs.
    """
    url = (f'https://query1.finance.yahoo.com/v8/finance/chart/{symbol}'
           f'?interval=1d&range={range_}')
    try:
        data = yahoo_get_json(url)
        result = data['chart']['result'][0]
        timestamps = result['timestamp']
        quote = result['indicators']['quote'][0]
        bars = []
        for i, ts in enumerate(timestamps):
            if quote['close'][i] is None or quote['volume'][i] is None:
                continue
            bars.append({
                'date':   datetime.fromtimestamp(ts, tz=timezone.utc).strftime('%Y-%m-%d'),
                'open':   quote['open'][i],
                'high':   quote['high'][i],
                'low':    quote['low'][i],
                'close':  quote['close'][i],
                'volume': quote['volume'][i],
            })
        return bars
    except Exception as e:
        print(f'  ! Yahoo history {symbol}: {e}', file=sys.stderr)
        return None


def fetch_stooq_history(symbol, years=5):
    """Fallback: fetch daily OHLCV CSV from Stooq.com.

    Stooq is permissive about cloud IPs and is reliable when Yahoo blocks.
    Returns same format as fetch_yahoo_history.
    """
    end = datetime.now(timezone.utc)
    start = end - timedelta(days=int(years * 365.25 + 30))
    s_lower = symbol.lower()
    url = (f'https://stooq.com/q/d/l/?s={s_lower}.us'
           f'&d1={start.strftime("%Y%m%d")}&d2={end.strftime("%Y%m%d")}&i=d')
    try:
        text = http_get(url, headers=BROWSER_HEADERS)
        lines = text.strip().split('\n')
        if len(lines) < 2:
            return None
        # Stooq returns "Date,Open,High,Low,Close,Volume" as the header
        if not lines[0].lower().startswith('date'):
            return None
        bars = []
        for line in lines[1:]:
            parts = line.strip().split(',')
            if len(parts) < 5:
                continue
            try:
                bar = {
                    'date':   parts[0],  # already YYYY-MM-DD format from Stooq
                    'open':   float(parts[1]),
                    'high':   float(parts[2]),
                    'low':    float(parts[3]),
                    'close':  float(parts[4]),
                    'volume': int(float(parts[5])) if len(parts) > 5 and parts[5] else 0,
                }
                bars.append(bar)
            except (ValueError, IndexError):
                continue
        return bars if bars else None
    except Exception as e:
        print(f'  ! Stooq history {symbol}: {e}', file=sys.stderr)
        return None


def fetch_price_history(symbol, range_='5y'):
    """Try Yahoo first, fall back to Stooq.

    Yahoo provides cleaner data when reachable. Stooq is the failsafe — its
    permissive policy on cloud IPs makes it reliable on GitHub Actions runners
    even when Yahoo is rate-limiting or blocking.
    """
    bars = fetch_yahoo_history(symbol, range_)
    if bars and len(bars) >= 200:
        print(f'    [Yahoo: {len(bars)} bars]')
        return bars
    print(f'    [Yahoo failed, trying Stooq…]')
    bars = fetch_stooq_history(symbol)
    if bars and len(bars) >= 200:
        print(f'    [Stooq: {len(bars)} bars]')
        return bars
    return None


def sma(values, period):
    if len(values) < period:
        return None
    return sum(values[-period:]) / period


def ema_series(values, period):
    out = [None] * len(values)
    if len(values) < period:
        return out
    k = 2 / (period + 1)
    val = sum(values[:period]) / period
    out[period - 1] = val
    for i in range(period, len(values)):
        val = values[i] * k + val * (1 - k)
        out[i] = val
    return out


def rsi_series(closes, period=14):
    """Wilder's RSI (the original, classic formulation)."""
    out = [None] * len(closes)
    if len(closes) < period + 1:
        return out
    gains, losses = 0.0, 0.0
    for i in range(1, period + 1):
        d = closes[i] - closes[i - 1]
        if d >= 0:
            gains += d
        else:
            losses -= d
    avg_g, avg_l = gains / period, losses / period
    out[period] = 100 if avg_l == 0 else 100 - 100 / (1 + avg_g / avg_l)
    for i in range(period + 1, len(closes)):
        d = closes[i] - closes[i - 1]
        g = d if d > 0 else 0
        l = -d if d < 0 else 0
        avg_g = (avg_g * (period - 1) + g) / period
        avg_l = (avg_l * (period - 1) + l) / period
        out[i] = 100 if avg_l == 0 else 100 - 100 / (1 + avg_g / avg_l)
    return out


def compute_veteran_signal(bars):
    """Compute the 6-rule veteran's buy signal from daily OHLCV bars."""
    if not bars or len(bars) < 200:
        return {'error': 'insufficient_data'}

    closes = [b['close'] for b in bars]
    highs = [b['high'] for b in bars]
    volumes = [b['volume'] for b in bars]
    last, prev = closes[-1], closes[-2]

    ma200 = sma(closes, 200)
    above_200 = last > ma200

    ma50 = sma(closes, 50)
    golden_cross = ma50 > ma200

    rsi = rsi_series(closes)
    cur_rsi = rsi[-1]
    recent_10 = [v for v in rsi[-10:] if v is not None]
    was_oversold = any(v < 35 for v in recent_10)
    rsi_bounce = was_oversold and cur_rsi > 30 and cur_rsi < 60

    ema12 = ema_series(closes, 12)
    ema26 = ema_series(closes, 26)
    macd_line = [
        (ema12[i] - ema26[i]) if (ema12[i] is not None and ema26[i] is not None) else None
        for i in range(len(closes))
    ]
    macd_valid = [v for v in macd_line if v is not None]
    sig_series = ema_series(macd_valid, 9)
    cur_macd, prev_macd = macd_line[-1], macd_line[-2]
    cur_sig = sig_series[-1]
    macd_bullish = cur_macd > cur_sig and cur_macd > prev_macd

    high_20 = max(highs[-20:])
    pullback_pct = ((high_20 - last) / high_20) * 100
    pullback = 3 <= pullback_pct <= 15

    avg_vol_20 = sma(volumes, 20)
    today_up = last > prev
    vol_confirm = today_up and volumes[-1] > avg_vol_20

    checks = [
        {'label': 'Above 200-day MA',    'met': bool(above_200),    'source': 'Weinstein'},
        {'label': 'Golden cross active', 'met': bool(golden_cross), 'source': '50 > 200 MA'},
        {'label': 'RSI bounce setup',    'met': bool(rsi_bounce),   'source': f'Wilder RSI {cur_rsi:.0f}'},
        {'label': 'MACD bullish',        'met': bool(macd_bullish), 'source': 'Appel'},
        {'label': 'Buyable pullback',    'met': bool(pullback),     'source': f'-{pullback_pct:.1f}% off high'},
        {'label': 'Volume confirms',     'met': bool(vol_confirm),  'source': 'Wyckoff'},
    ]
    score = sum(1 for c in checks if c['met'])

    if score >= 5:
        signal, status_text = 'strong-buy', '🟢 STRONG BUY'
        summary = ('Multiple veteran indicators align — the kind of setup professionals look for. '
                   'Still verify earnings calendar and your own thesis.')
        light_class = status_class = 'bright-green'
    elif score >= 3:
        signal, status_text = 'buy', '🟢 BUY'
        summary = ('Several bullish conditions present. Reasonable for a partial position; '
                   'consider scaling in rather than going all-in.')
        light_class = status_class = 'green'
    elif score == 2:
        signal, status_text = 'watch', '🟡 WATCH'
        summary = ('Some positives but not enough confirmation. '
                   'Wait for more conditions to align before committing capital.')
        light_class = status_class = 'yellow'
    else:
        signal, status_text = 'wait', '⚪ WAIT'
        summary = ("Conditions don't favor a new entry today. "
                   'Better setups typically appear within days or weeks — patience pays.')
        light_class = status_class = 'gray'

    return {
        'score':        score,
        'signal':       signal,
        'status_text':  status_text,
        'summary':      summary,
        'light_class':  light_class,
        'status_class': status_class,
        'checks':       checks,
        'as_of':        bars[-1]['date'],
        'last_close':   round(last, 2),
    }


def compute_long_term(bars):
    """Compute long-term metrics: CAGR, MA distance, 52-week range, DCA Bargain Meter."""
    if not bars or len(bars) < 50:
        return {'error': 'insufficient_data'}

    closes = [b['close'] for b in bars]
    dates = [datetime.strptime(b['date'], '%Y-%m-%d').replace(tzinfo=timezone.utc) for b in bars]
    n = len(closes)
    last = closes[-1]
    last_date = dates[-1]

    # Year-to-date
    cur_year = last_date.year
    ytd_idx = next((i for i, d in enumerate(dates) if d.year == cur_year), None)
    ytd_return = ((last / closes[ytd_idx]) - 1) * 100 if ytd_idx is not None else None

    # CAGR over N years
    def cagr_over(years):
        target = last_date - timedelta(days=int(365.25 * years))
        idx = next((i for i, d in enumerate(dates) if d >= target), None)
        if idx is None or idx >= n - 1:
            return None
        elapsed = (last_date - dates[idx]).total_seconds() / (365.25 * 86400)
        if elapsed < 0.5:
            return None
        return (((last / closes[idx]) ** (1 / elapsed)) - 1) * 100

    cagr_1 = cagr_over(1)
    cagr_3 = cagr_over(3)
    cagr_5 = cagr_over(5)

    # Moving averages
    ma200 = sma(closes, 200)
    ma50 = sma(closes, 50)
    ma200_dist = ((last / ma200) - 1) * 100 if ma200 else None
    in_uptrend = bool(ma200 and ma50 and ma50 > ma200)

    # 52-week range (252 trading days ≈ 1 year)
    recent_252 = closes[-252:]
    high_52 = max(recent_252)
    low_52 = min(recent_252)
    drawdown = ((last / high_52) - 1) * 100
    range_pos = ((last - low_52) / (high_52 - low_52)) * 100 if high_52 != low_52 else 50

    # RSI for DCA scoring
    rsi = rsi_series(closes)
    cur_rsi = rsi[-1]

    # ---- DCA Bargain Meter ----
    # Higher = better entry for ADDING to a long-term position
    dca_score = 0
    if cur_rsi is not None:
        if cur_rsi < 35:
            dca_score += 2
        elif cur_rsi < 50:
            dca_score += 1
    if drawdown < -20:
        dca_score += 2
    elif drawdown < -10:
        dca_score += 1
    if range_pos < 30:
        dca_score += 1
    if ma200_dist is not None and abs(ma200_dist) < 5:
        dca_score += 1
    # Critical safety: never accelerate buys when long-term trend is broken
    if not in_uptrend:
        dca_score = min(dca_score, 2)
    dca_score = max(0, min(5, round(dca_score)))

    if dca_score >= 5:
        dca_rating, dca_rating_class = 'EXCEPTIONAL VALUE', 'positive'
    elif dca_score == 4:
        dca_rating, dca_rating_class = 'BARGAIN', 'positive'
    elif dca_score == 3:
        dca_rating, dca_rating_class = 'ATTRACTIVE', 'positive'
    elif dca_score == 2:
        dca_rating, dca_rating_class = 'FAIR VALUE', 'warning'
    elif dca_score == 1:
        dca_rating, dca_rating_class = 'ELEVATED', 'warning'
    else:
        dca_rating, dca_rating_class = 'PREMIUM', 'negative'

    def r(v, places=2):
        return round(v, places) if v is not None else None

    return {
        'last':             r(last),
        'ytd_return':       r(ytd_return, 2),
        'cagr_1y':          r(cagr_1, 2),
        'cagr_3y':          r(cagr_3, 2),
        'cagr_5y':          r(cagr_5, 2),
        'ma200':            r(ma200),
        'ma50':             r(ma50),
        'ma200_dist':       r(ma200_dist, 2),
        'in_uptrend':       in_uptrend,
        'high_52w':         r(high_52),
        'low_52w':          r(low_52),
        'drawdown':         r(drawdown, 2),
        'range_pos':        r(range_pos, 1),
        'rsi':              r(cur_rsi, 1),
        'dca_score':        dca_score,
        'dca_rating':       dca_rating,
        'dca_rating_class': dca_rating_class,
        'as_of':            bars[-1]['date'],
    }


# ============================================================
# Main
# ============================================================

def main():
    started = datetime.now(timezone.utc)
    print(f'=== Building feed at {started.isoformat()} ===')
    print(f'User-Agent: {USER_AGENT}')

    feed = {
        'updated_utc':   started.isoformat(),
        'updated_human': started.strftime('%Y-%m-%d %H:%M UTC'),
        'macro':         {},
        'stocks':        {},
    }

    print('\n[1/4] Macro snapshot…')
    feed['macro'] = fetch_macro_snapshot()

    print('\n[2/4] SEC filings index…')
    all_filings = {}
    for sym in SYMBOLS:
        cik = CIK_MAP[sym]
        print(f'  {sym} (CIK {cik})…')
        all_filings[sym] = sec_recent_filings(cik)

    print('\n[3/4] Per-stock SEC + earnings data…')
    for sym in SYMBOLS:
        print(f'  {sym}: parsing Form 4s + earnings…')
        filings = all_filings[sym]
        form4s = [f for f in filings if f['form'] == '4'][:MAX_FORM4_PER_STOCK]
        material = filter_material_filings(filings)
        insider = summarize_insider_activity(form4s)
        earnings = fetch_next_earnings(sym)
        feed['stocks'][sym] = {
            'next_earnings':    earnings,
            'insider_activity': insider,
            'recent_filings':   material,
        }
        print(f'    {sym}: {insider["purchase_count"]} purchases / '
              f'{insider["sale_count"]} sales / '
              f'{len(material)} material filings')

    print('\n[4/4] Price history & technical signals…')
    for sym in SYMBOLS:
        print(f'  {sym}: fetching 5y of daily bars…')
        bars = fetch_price_history(sym, '5y')
        if bars and len(bars) >= 200:
            feed['stocks'][sym]['veteran_signal'] = compute_veteran_signal(bars)
            feed['stocks'][sym]['long_term'] = compute_long_term(bars)
            vs = feed['stocks'][sym]['veteran_signal']
            lt = feed['stocks'][sym]['long_term']
            print(f'    {sym}: signal={vs.get("signal", "?")} ({vs.get("score", "?")}/6) · '
                  f'DCA={lt.get("dca_score", "?")}/5 ({lt.get("dca_rating", "?")})')
        else:
            feed['stocks'][sym]['veteran_signal'] = {'error': 'fetch_failed'}
            feed['stocks'][sym]['long_term'] = {'error': 'fetch_failed'}
            print(f'    {sym}: FAILED to fetch price history')

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(feed, indent=2))
    elapsed = (datetime.now(timezone.utc) - started).total_seconds()
    print(f'\nWrote {OUTPUT_PATH} ({OUTPUT_PATH.stat().st_size:,} bytes) '
          f'in {elapsed:.1f}s')


if __name__ == '__main__':
    main()
