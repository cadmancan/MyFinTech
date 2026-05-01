# Investor Dashboard — Live Public Record Feed

This repo turns your dashboard into a self-updating tool. A small Python script runs every weekday after market close on GitHub Actions, pulls fresh public-record data, and commits it to `data/feed.json`. The dashboard reads it on load.

**Cost:** $0/month. **API keys:** none. **Maintenance:** none.

\---

## What it pulls

**Macro snapshot** (Yahoo Finance):

* VIX, 10-year Treasury yield, S\&P 500 — with daily change

**Per stock** (MU, AVGO, PLTR, TSLA, NVDA):

* **Next earnings date** (Yahoo Finance) — with countdown and DCA-timing reminder
* **Insider transactions** (SEC EDGAR Form 4) — last 90 days, parsed to separate **open-market purchases** (transaction code P, the actual signal) from **routine grants and option exercises** (codes A, M, F — excluded as noise)
* **Material filings** (SEC EDGAR) — recent 10-K, 10-Q, 8-K with direct links
* **Veteran's Buy Signal** — 6-rule technical analysis (Weinstein, Wilder, Appel, Minervini/O'Neil, Wyckoff, Dow Theory) computed from 5 years of daily bars
* **Long-Term Metrics** — YTD return, 1Y/3Y/5Y CAGR, distance from 200-MA, 52-week range position, drawdown, and the DCA Bargain Meter

All sources are public, official, and free. Price data uses Yahoo Finance with **Stooq.com as automatic fallback** if Yahoo throttles or blocks the request.

**Why server-side computation?** Earlier versions of the dashboard fetched price data directly from the browser. Yahoo's CORS policies are inconsistent and the public CORS proxies are unreliable, so signals would frequently fail to load. Moving the computation to the GitHub Actions runner (where there are no CORS restrictions) makes it work reliably forever — at the trade-off of data being at most \~24 hours stale, which is fine for long-term DCA decisions.

\---

## File structure

```
your-repo/
├── investor\_dashboard.html     ← the dashboard (open this in a browser)
├── data/
│   └── feed.json               ← updated daily by GitHub Actions
├── scripts/
│   └── fetch\_data.py           ← Python feed builder (stdlib only)
├── .github/workflows/
│   └── update.yml              ← runs the script daily
└── README.md                   ← this file
```

\---

## Setup

### Step 1 — Create a GitHub repo

1. Go to [github.com/new](https://github.com/new)
2. **Repository name:** anything you want (e.g. `investor-dashboard`)
3. **Visibility:**

   * **Public** if you want to use free GitHub Pages and bookmark a URL → recommended for ease of access
   * **Private** if you'd rather keep it locked down → you'll run the dashboard locally instead (Step 4 covers both)
4. Don't initialize with a README — we'll push our own
5. Click **Create repository**

### Step 2 — Push these files

If you have Git installed:

```bash
cd path/to/this/folder
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
git push -u origin main
```

Or use the GitHub web UI: drag and drop the files into the empty repo.

### Step 3 — Set the SEC contact email

The SEC requires automated tools to identify themselves with a contact email (so they can reach you if your script misbehaves). It just needs to be a working address — there's nothing to verify.

1. In your GitHub repo, go to **Settings → Secrets and variables → Actions**
2. Click **New repository secret**
3. Name: `CONTACT\_EMAIL`
4. Value: your email address
5. Click **Add secret**

### Step 4 — Choose how you'll view the dashboard

#### Option A — GitHub Pages (recommended, free, public repo only)

1. In your repo, go to **Settings → Pages**
2. Under **Source**, choose **Deploy from a branch**
3. Branch: **main**, folder: **/ (root)**
4. Click **Save**
5. Wait \~1 minute, then visit:
`https://YOUR-USERNAME.github.io/YOUR-REPO/investor\_dashboard.html`

Bookmark it. Open from any device. The page is just static HTML+JS — no server needed.

#### Option B — Local (works for private repos too)

```bash
# In the repo directory:
cd /path/to/repo

# Start a tiny local web server
python3 -m http.server 8000

# Open in your browser:
# http://localhost:8000/investor\_dashboard.html
```

You need the local server (rather than just opening the HTML file directly) because the dashboard fetches `./data/feed.json`, and browsers block `fetch()` on `file://` URLs for security.

To get fresh data while running locally, you'd run the script manually:

```bash
export CONTACT\_EMAIL="your-email@example.com"
python3 scripts/fetch\_data.py
```

Or set up a local cron job (macOS / Linux):

```bash
crontab -e
# Add: run weekdays at 5:30 PM local time
30 17 \* \* 1-5 cd /path/to/repo \&\& CONTACT\_EMAIL="your-email@example.com" python3 scripts/fetch\_data.py
```

### Step 5 — Trigger the first feed run

To populate the feed without waiting for the schedule:

1. Go to your repo's **Actions** tab
2. Click **Update Investor Feed** in the left sidebar
3. Click **Run workflow** → **Run workflow** (green button)
4. Wait \~2 minutes; you'll see a green checkmark when done
5. The workflow auto-commits the fresh `data/feed.json` to your repo
6. Refresh the dashboard — the Public Record panel should now show live data

After this initial run, the workflow runs automatically at 21:30 UTC on weekdays (5:30 PM ET / 4:30 PM ET depending on DST).

\---

## Optional: Finnhub intraday price layer

The Veteran's Buy Signal and DCA Bargain Meter are computed from yesterday's close — the right resolution for long-term DCA decisions. But sometimes it's useful to glance at today's intraday price too. The dashboard supports an optional layer that pulls live quotes from Finnhub's free tier (60 calls/min, no credit card required) and shows a small banner inside the Long-Term Metrics panel.

**Without setup, this layer simply doesn't appear** — the dashboard works exactly as it does today. With setup, you'll see a green pulsing dot and a row showing today's price, change %, and timestamp.

### Setup (5 minutes)

1. **Get a free Finnhub key** — sign up at [finnhub.io/register](https://finnhub.io/register). They'll show your key on the dashboard immediately. No credit card.
2. **In your repo on GitHub**, click **Add file → Create new file**.
3. **Filename:** `config.js` (exactly that — lowercase, no folders)
4. **Contents:**

```javascript
   window.FINNHUB\_API\_KEY = "paste\_your\_finnhub\_key\_here";
   ```

   Replace the placeholder with your actual key (still in quotes).

5. Scroll down. Click **Commit changes**.
6. Refresh your dashboard — the intraday banner should appear at the bottom of the Long-Term Metrics panel.

   ### Why this is in a separate file

   `config.js` is listed in `.gitignore`, which means **Git will refuse to commit it via local push**. But because GitHub's web UI bypasses gitignore, you CAN add it directly through the browser as described above. Either way works.

   ### Important security note for public repos

   If your repo is **public**, anyone visiting your GitHub Pages URL can view the page source and read your Finnhub key. The realistic worst case is they could burn through your 60-calls-per-minute rate limit, leaving the intraday banner broken until the limit resets — the rest of the dashboard keeps working fine. They cannot access your account, billing, or anything else, because Finnhub keys only authorize quote lookups.

   If this concerns you, either:

* Make the repo private (you'll lose GitHub Pages on free tier; run locally instead — see Option B above)
* Skip the Finnhub layer entirely; the dashboard already shows yesterday's close, which is what the signals are based on

  ### How to verify it's working

  After committing `config.js` and refreshing the dashboard, you should see at the bottom of the Long-Term Metrics panel:

  > 🟢 INTRADAY  $96.42  ▲ +$0.92 (+0.96%)  as of 2:34 PM ET · prev close $95.50 · via Finnhub

  If you see nothing, check the browser DevTools console (F12 → Console). Common issues:

* 401 Unauthorized → key was typed wrong
* "Invalid API call" → the symbol isn't supported on the free tier (all 5 of yours are)
* 429 Rate Limit → you've hit 60/min; wait a minute and refresh

  \---

  ## How it works

  ```
                  ┌──────────────────────────────┐
                  │    GitHub Actions runner     │
                  │   (weekdays at 21:30 UTC)    │
                  └──────────────┬───────────────┘
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │    scripts/fetch\_data.py     │
                  └──────────────┬───────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              ▼                  ▼                  ▼
       ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
       │ Yahoo Finance│   │   SEC EDGAR  │   │   SEC EDGAR  │
       │ Macro \& EPS  │   │   Filings    │   │   Form 4 XML │
       └──────────────┘   └──────────────┘   └──────────────┘
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │       data/feed.json         │
                  │   (committed to your repo)   │
                  └──────────────┬───────────────┘
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │   investor\_dashboard.html    │
                  │   fetch('./data/feed.json')  │
                  └──────────────────────────────┘
```

  The dashboard is purely static — no servers, no databases. The feed is just a JSON file that lives in your repo and gets updated by a scheduled job.

  \---

  ## Why these specific data points?

  **Open-market insider purchases (Form 4, code P)** are historically a moderately bullish signal — when a CEO or director buys their own company's stock with personal money, they have inside knowledge and conviction. The script deliberately filters out:

* **Code A** (grants/awards) — automatic compensation, no signal
* **Code M** (option exercises) — usually paired with immediate sales, not a discretionary buy
* **Code F** (tax withholding) — non-discretionary
* **Code G** (gifts) — neutral signal

  So when the dashboard says "3 insider purchases, $4.2M total," that means three executives chose to spend $4.2M of their own money buying shares — a much rarer and more meaningful event than the daily noise of grants and option exercises.

  **Material filings (8-K)** are required when something significant happens: acquisitions, executive changes, earnings warnings, bankruptcies, going-private deals. Worth knowing about.

  **Earnings dates** matter for DCA timing. Most disciplined long-term investors avoid adding new money in the 2–3 days before earnings (high implied volatility, often a coin-flip), and prefer to add 1–2 days after when the result is known and the volatility has resolved.

  \---

  ## Cost

|Service|Cost|
|-|-|
|GitHub Actions on a public repo|Free (unlimited minutes)|
|GitHub Actions on a private repo|Free (2,000 min/month — script uses \~3 min/day = \~75 min/month)|
|GitHub Pages|Free (public repos)|
|SEC EDGAR|Free, public-record|
|Yahoo Finance|Free|
|**Total**|**$0/month**|

\---

## Troubleshooting

**Workflow fails with 403 from SEC**
The `CONTACT\_EMAIL` secret isn't set. SEC blocks requests without proper user-agent identification. Repeat Step 3.

**Workflow fails with 429 (rate limit)**
The script throttles to \~7 req/sec (under SEC's 10/sec limit) but if you hit it, edit `scripts/fetch\_data.py` and change `time.sleep(0.15)` to `time.sleep(0.5)` in the `sec\_throttle()` function.

**Dashboard shows "Feed not configured"**
The page can't find `./data/feed.json`. Check that:

* The Actions workflow has run successfully (green check in Actions tab), OR
* You ran `python3 scripts/fetch\_data.py` locally
* The file path is exactly `data/feed.json` relative to the HTML

**Insider transactions look incomplete**
The Form 4 parser fetches each filing's XML individually. Some older filings have non-standard XML and may be skipped silently. The `purchase\_count` field reflects only open-market purchases (code P) — if you see "0 buys" but you know an executive recently exercised options, that's by design (the script excludes routine grants and exercises).

**Workflow runs at the wrong time**
The cron expression `30 21 \* \* 1-5` is in UTC. To change to a different time, edit `.github/workflows/update.yml`. Note: GitHub Actions schedules can run up to 30 minutes late under load — don't expect minute-precise execution.

**I want to add another stock**
Edit `scripts/fetch\_data.py`:

1. Add the symbol to `SYMBOLS`
2. Look up its CIK at [SEC EDGAR company search](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany)
3. Add it to `CIK\_MAP` (10-digit, zero-padded)

You'd also need to add a stock-view section in `investor\_dashboard.html` (mirroring how the existing 5 are structured) and a tab button.

\---

## License

Provided as-is for personal use. Educational only — not investment advice. The signals shown are technical analysis and public-record summaries; they don't account for your tax situation, risk tolerance, or full financial picture. Make your own decisions.



updated

