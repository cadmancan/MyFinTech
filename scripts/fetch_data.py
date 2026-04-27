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
        data = http_get_json(url)
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
        data = http_get_json(url)
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

    print('\n[1/3] Macro snapshot…')
    feed['macro'] = fetch_macro_snapshot()

    print('\n[2/3] SEC filings index…')
    all_filings = {}
    for sym in SYMBOLS:
        cik = CIK_MAP[sym]
        print(f'  {sym} (CIK {cik})…')
        all_filings[sym] = sec_recent_filings(cik)

    print('\n[3/3] Per-stock data…')
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

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(feed, indent=2))
    elapsed = (datetime.now(timezone.utc) - started).total_seconds()
    print(f'\nWrote {OUTPUT_PATH} ({OUTPUT_PATH.stat().st_size:,} bytes) '
          f'in {elapsed:.1f}s')


if __name__ == '__main__':
    main()
