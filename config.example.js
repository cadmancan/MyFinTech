// =====================================================================
//  OPTIONAL: Finnhub intraday price layer
// =====================================================================
//
//  This file is an EXAMPLE. To enable intraday prices, copy it:
//
//      cp config.example.js config.js
//
//  Then edit config.js, replace YOUR_FINNHUB_KEY_HERE with your actual key.
//
//  Get a free Finnhub key at https://finnhub.io/register (free tier:
//  60 calls/min, no credit card required).
//
//  config.js is gitignored, so your key will NOT be committed to GitHub.
//  Without config.js, the dashboard works exactly as it does today —
//  intraday prices simply don't appear, and yesterday's close is shown.
//
//  WHY DON'T I JUST EDIT THIS FILE DIRECTLY?
//  Because config.example.js IS committed to the repo. If you put your
//  key here, anyone visiting your GitHub Pages URL can read it. Always
//  use config.js for real keys.
// =====================================================================

window.FINNHUB_API_KEY = "YOUR_FINNHUB_KEY_HERE";
