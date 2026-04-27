<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Personal Investor Dashboard</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    background: #0d1117;
    color: #e6edf3;
    min-height: 100vh;
    -webkit-font-smoothing: antialiased;
  }
  .header {
    background: #161b22;
    border-bottom: 1px solid #30363d;
    padding: 18px 28px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
  }
  .header-title {
    display: flex;
    align-items: center;
    gap: 14px;
  }
  .logo-mark {
    width: 34px;
    height: 34px;
    background: linear-gradient(135deg, #2f81f7, #1f6feb);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    font-size: 16px;
    color: white;
  }
  .header h1 {
    font-size: 18px;
    font-weight: 500;
    letter-spacing: -0.2px;
  }
  .header-meta {
    font-size: 12px;
    color: #8b949e;
  }
  .header-meta span {
    color: #2f81f7;
  }
  .ticker-bar {
    background: #0d1117;
    border-bottom: 1px solid #30363d;
    padding: 6px 0;
  }
  .tabs {
    display: flex;
    background: #161b22;
    border-bottom: 1px solid #30363d;
    padding: 0 28px;
    overflow-x: auto;
    scrollbar-width: none;
  }
  .tabs::-webkit-scrollbar { display: none; }
  .tab {
    background: transparent;
    border: none;
    color: #8b949e;
    padding: 14px 22px;
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    border-bottom: 2px solid transparent;
    transition: all 0.15s;
    font-family: inherit;
    white-space: nowrap;
  }
  .tab:hover {
    color: #e6edf3;
  }
  .tab.active {
    color: #2f81f7;
    border-bottom-color: #2f81f7;
  }
  .tab-symbol {
    font-weight: 600;
    margin-right: 6px;
  }
  .container {
    padding: 24px 28px;
    max-width: 1800px;
    margin: 0 auto;
  }
  .stock-view {
    display: none;
  }
  .stock-view.active {
    display: block;
  }
  .grid-top {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px;
    margin-bottom: 18px;
  }
  .grid-main {
    display: grid;
    grid-template-columns: 1fr 380px;
    gap: 18px;
    margin-bottom: 18px;
  }
  .grid-bottom {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px;
    margin-bottom: 18px;
  }
  @media (max-width: 1100px) {
    .grid-main, .grid-top, .grid-bottom { grid-template-columns: 1fr; }
  }
  .panel {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 10px;
    overflow: hidden;
  }
  .panel-header {
    padding: 14px 18px;
    border-bottom: 1px solid #30363d;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .panel-title {
    font-size: 13px;
    font-weight: 500;
    color: #e6edf3;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .panel-badge {
    font-size: 11px;
    color: #8b949e;
    background: #21262d;
    padding: 3px 8px;
    border-radius: 4px;
  }
  .panel-body {
    padding: 0;
    min-height: 200px;
  }
  .panel-body.padded { padding: 14px; }
  .signal-panel {
    min-height: 460px;
  }
  .chart-panel {
    min-height: 540px;
  }
  .info-panel {
    min-height: 250px;
  }
  .news-panel {
    min-height: 460px;
  }
  .fundamentals-panel {
    min-height: 460px;
  }
  .disclaimer {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 10px;
    padding: 18px 22px;
    margin-bottom: 18px;
    font-size: 13px;
    color: #8b949e;
    line-height: 1.6;
  }
  .disclaimer strong {
    color: #f0883e;
    font-weight: 500;
  }
  .legend {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 8px;
    padding: 14px 18px;
    background: #0d1117;
    border-top: 1px solid #30363d;
    font-size: 11px;
  }
  .legend-item {
    text-align: center;
    padding: 8px 4px;
    border-radius: 6px;
  }
  .legend-item .label {
    display: block;
    font-weight: 600;
    margin-bottom: 2px;
    font-size: 10px;
    letter-spacing: 0.4px;
  }
  .legend-item .desc {
    color: #8b949e;
    font-size: 10px;
  }
  .leg-strong-buy { background: rgba(35, 134, 54, 0.15); color: #3fb950; }
  .leg-buy { background: rgba(35, 134, 54, 0.08); color: #56d364; }
  .leg-neutral { background: rgba(139, 148, 158, 0.1); color: #8b949e; }
  .leg-sell { background: rgba(248, 81, 73, 0.08); color: #f85149; }
  .leg-strong-sell { background: rgba(248, 81, 73, 0.15); color: #ff6b6b; }
  .footer {
    text-align: center;
    padding: 20px;
    color: #6e7681;
    font-size: 11px;
    border-top: 1px solid #30363d;
    margin-top: 20px;
  }
  .footer a {
    color: #2f81f7;
    text-decoration: none;
  }
  .quick-links {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    padding: 12px 18px;
    background: #0d1117;
    border-top: 1px solid #30363d;
  }
  .quick-link {
    font-size: 11px;
    color: #2f81f7;
    text-decoration: none;
    padding: 4px 10px;
    border: 1px solid #30363d;
    border-radius: 4px;
    transition: all 0.15s;
  }
  .quick-link:hover {
    background: #21262d;
    border-color: #2f81f7;
  }
  /* Veteran's Buy Signal panel */
  .vet-panel {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 10px;
    margin-bottom: 18px;
    overflow: hidden;
    transition: border-color 0.3s;
  }
  .vet-panel.signal-buy { border-color: rgba(63, 185, 80, 0.5); }
  .vet-panel.signal-strong-buy {
    border-color: #3fb950;
    box-shadow: 0 0 0 1px rgba(63, 185, 80, 0.4);
  }
  .vet-panel.signal-watch { border-color: rgba(210, 153, 34, 0.5); }
  .vet-top {
    display: grid;
    grid-template-columns: auto 1fr auto;
    gap: 18px;
    align-items: center;
    padding: 18px 22px;
  }
  .vet-light {
    width: 56px;
    height: 56px;
    border-radius: 50%;
    background: #21262d;
    border: 2px solid #30363d;
    flex-shrink: 0;
    transition: all 0.3s;
  }
  .vet-light.green {
    background: radial-gradient(circle at 30% 30%, #56d364, #1f6f30);
    border-color: #3fb950;
    box-shadow: 0 0 24px rgba(63, 185, 80, 0.6), inset 0 -4px 12px rgba(0,0,0,0.3);
  }
  .vet-light.bright-green {
    background: radial-gradient(circle at 30% 30%, #7ee492, #238636);
    border-color: #56d364;
    box-shadow: 0 0 32px rgba(86, 211, 100, 0.8), inset 0 -4px 12px rgba(0,0,0,0.3);
    animation: vetPulse 2s ease-in-out infinite;
  }
  .vet-light.yellow {
    background: radial-gradient(circle at 30% 30%, #f0d062, #9e7a18);
    border-color: #d29922;
    box-shadow: 0 0 18px rgba(210, 153, 34, 0.5), inset 0 -4px 12px rgba(0,0,0,0.3);
  }
  .vet-light.gray {
    background: radial-gradient(circle at 30% 30%, #6e7681, #30363d);
    border-color: #484f58;
  }
  @keyframes vetPulse {
    0%, 100% { box-shadow: 0 0 32px rgba(86, 211, 100, 0.7), inset 0 -4px 12px rgba(0,0,0,0.3); }
    50% { box-shadow: 0 0 48px rgba(86, 211, 100, 1), inset 0 -4px 12px rgba(0,0,0,0.3); }
  }
  .vet-info-section { min-width: 0; }
  .vet-section-title {
    font-size: 11px;
    letter-spacing: 0.6px;
    color: #8b949e;
    text-transform: uppercase;
    margin-bottom: 4px;
  }
  .vet-section-title strong {
    color: #2f81f7;
    font-weight: 600;
  }
  .vet-status-text {
    font-size: 22px;
    font-weight: 600;
    margin-bottom: 4px;
    letter-spacing: -0.3px;
  }
  .vet-status-text.green { color: #3fb950; }
  .vet-status-text.bright-green { color: #56d364; }
  .vet-status-text.yellow { color: #d29922; }
  .vet-status-text.gray { color: #8b949e; }
  .vet-summary {
    font-size: 13px;
    color: #8b949e;
    line-height: 1.5;
  }
  .vet-score { text-align: right; }
  .vet-score-num {
    font-size: 32px;
    font-weight: 600;
    color: #e6edf3;
    line-height: 1;
  }
  .vet-score-label {
    font-size: 10px;
    color: #8b949e;
    margin-top: 4px;
    letter-spacing: 0.4px;
    text-transform: uppercase;
  }
  .vet-checks {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
    padding: 14px 22px;
    background: #0d1117;
    border-top: 1px solid #30363d;
  }
  @media (max-width: 800px) {
    .vet-checks { grid-template-columns: repeat(2, 1fr); }
    .vet-top { grid-template-columns: auto 1fr; }
    .vet-score { grid-column: 1 / -1; text-align: left; display: flex; align-items: baseline; gap: 8px; }
    .vet-score-num { font-size: 24px; }
  }
  .vet-check {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 12px;
    padding: 8px 10px;
    border-radius: 6px;
    background: #161b22;
    border: 1px solid #30363d;
    color: #6e7681;
  }
  .vet-check.met {
    background: rgba(35, 134, 54, 0.1);
    border-color: rgba(63, 185, 80, 0.3);
    color: #3fb950;
  }
  .vet-check-icon {
    width: 16px;
    height: 16px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 10px;
    font-weight: 700;
    flex-shrink: 0;
  }
  .vet-check.met .vet-check-icon { background: #238636; color: white; }
  .vet-check:not(.met) .vet-check-icon {
    background: #21262d;
    color: #6e7681;
    border: 1px solid #30363d;
  }
  .vet-check-label { flex: 1; }
  .vet-check-source {
    font-size: 10px;
    color: #6e7681;
    font-style: italic;
  }
  .vet-check.met .vet-check-source { color: rgba(63, 185, 80, 0.7); }
  .vet-attribution {
    padding: 12px 22px;
    background: #0d1117;
    border-top: 1px solid #30363d;
    font-size: 11px;
    color: #6e7681;
    line-height: 1.5;
  }
  .vet-attribution strong { color: #8b949e; font-weight: 500; }
  .vet-refresh {
    background: transparent;
    border: 1px solid #30363d;
    color: #8b949e;
    font-size: 11px;
    padding: 4px 10px;
    border-radius: 4px;
    cursor: pointer;
    margin-left: 10px;
    font-family: inherit;
  }
  .vet-refresh:hover { background: #21262d; color: #e6edf3; }

  /* Long-term metrics panel */
  .lt-panel {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 10px;
    margin-bottom: 18px;
    overflow: hidden;
  }
  .lt-header {
    padding: 14px 22px;
    border-bottom: 1px solid #30363d;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .lt-title { font-size: 11px; letter-spacing: 0.6px; color: #8b949e; text-transform: uppercase; }
  .lt-title strong { color: #2f81f7; font-weight: 600; }
  .lt-asof { font-size: 11px; color: #6e7681; }
  .lt-stats {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 1px;
    background: #30363d;
  }
  @media (max-width: 800px) { .lt-stats { grid-template-columns: repeat(3, 1fr); } }
  .lt-stat { background: #161b22; padding: 14px 12px; text-align: center; }
  .lt-stat-label {
    font-size: 10px; color: #8b949e;
    letter-spacing: 0.4px; text-transform: uppercase; margin-bottom: 6px;
  }
  .lt-stat-value {
    font-size: 18px; font-weight: 600; color: #e6edf3;
    font-variant-numeric: tabular-nums;
  }
  .lt-stat-value.positive { color: #3fb950; }
  .lt-stat-value.negative { color: #f85149; }
  .lt-stat-value.warning { color: #d29922; }
  .lt-range {
    padding: 16px 22px;
    border-top: 1px solid #30363d;
    border-bottom: 1px solid #30363d;
  }
  .lt-range-header {
    display: flex; justify-content: space-between;
    font-size: 12px; color: #8b949e; margin-bottom: 10px;
  }
  .lt-range-header strong { color: #e6edf3; font-weight: 500; }
  .lt-range-bar {
    height: 8px;
    background: linear-gradient(to right, rgba(63,185,80,0.3), rgba(210,153,34,0.25), rgba(248,81,73,0.3));
    border-radius: 4px;
    position: relative;
  }
  .lt-range-marker {
    position: absolute; top: -4px;
    width: 4px; height: 16px;
    background: #2f81f7;
    border-radius: 2px;
    transform: translateX(-50%);
    box-shadow: 0 0 8px rgba(47, 129, 247, 0.7);
    transition: left 0.4s;
  }
  .lt-range-labels {
    display: flex; justify-content: space-between;
    font-size: 11px; color: #6e7681; margin-top: 8px;
  }
  .lt-dca { padding: 16px 22px; }
  .lt-dca-header {
    display: flex; justify-content: space-between;
    align-items: center; margin-bottom: 12px;
  }
  .lt-dca-title { font-size: 13px; font-weight: 500; color: #e6edf3; }
  .lt-dca-rating { font-size: 13px; font-weight: 600; }
  .lt-dca-dots { display: flex; gap: 6px; margin-bottom: 10px; }
  .dca-dot {
    width: 22px; height: 22px;
    border-radius: 50%;
    background: #21262d; border: 1px solid #30363d;
  }
  .dca-dot.active {
    background: radial-gradient(circle at 30% 30%, #56d364, #1f6f30);
    border-color: #3fb950;
    box-shadow: 0 0 8px rgba(63, 185, 80, 0.4);
  }
  .lt-dca-explain { font-size: 11px; color: #6e7681; line-height: 1.6; }

  /* Public Record panel — fed by data/feed.json */
  .pr-panel {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 10px;
    margin-bottom: 18px;
    overflow: hidden;
  }
  .pr-header {
    padding: 14px 22px;
    border-bottom: 1px solid #30363d;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .pr-title {
    font-size: 11px; letter-spacing: 0.6px;
    color: #8b949e; text-transform: uppercase;
  }
  .pr-title strong { color: #2f81f7; font-weight: 600; }
  .pr-asof { font-size: 11px; color: #6e7681; }
  .pr-asof.stale { color: #d29922; }
  .pr-asof.missing { color: #f85149; }
  .pr-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1px;
    background: #30363d;
  }
  @media (max-width: 800px) { .pr-row { grid-template-columns: 1fr; } }
  .pr-cell { background: #161b22; padding: 16px 22px; }
  .pr-cell-label {
    font-size: 10px; color: #8b949e;
    letter-spacing: 0.4px; text-transform: uppercase;
    margin-bottom: 8px;
    display: flex; justify-content: space-between; align-items: center;
  }
  .pr-cell-label .pr-tag {
    background: rgba(47,129,247,0.1); color: #2f81f7;
    padding: 2px 8px; border-radius: 10px;
    font-size: 10px; font-weight: 600; letter-spacing: 0.3px;
  }
  .pr-cell-main {
    font-size: 18px; font-weight: 600; color: #e6edf3;
    margin-bottom: 4px;
  }
  .pr-cell-main.positive { color: #3fb950; }
  .pr-cell-main.negative { color: #f85149; }
  .pr-cell-sub { font-size: 12px; color: #8b949e; line-height: 1.5; }
  .pr-list { padding: 14px 22px; border-top: 1px solid #30363d; }
  .pr-list-title {
    font-size: 11px; letter-spacing: 0.4px;
    color: #8b949e; text-transform: uppercase;
    margin-bottom: 10px;
    display: flex; justify-content: space-between;
  }
  .pr-list-title a {
    color: #2f81f7; text-decoration: none;
    font-size: 11px; font-weight: 500;
    text-transform: none; letter-spacing: 0;
  }
  .pr-list-title a:hover { text-decoration: underline; }
  .pr-item {
    display: grid;
    grid-template-columns: 80px 1fr auto;
    gap: 12px; padding: 8px 0;
    font-size: 13px; color: #c9d1d9;
    border-bottom: 1px solid #21262d;
    align-items: baseline;
  }
  .pr-item:last-child { border-bottom: none; }
  .pr-item-date { color: #8b949e; font-size: 12px; font-variant-numeric: tabular-nums; }
  .pr-item-main a { color: #c9d1d9; text-decoration: none; }
  .pr-item-main a:hover { color: #2f81f7; }
  .pr-item-meta { color: #6e7681; font-size: 12px; font-variant-numeric: tabular-nums; }
  .pr-item-meta.buy { color: #3fb950; }
  .pr-item-meta.sell { color: #f85149; }
  .pr-empty {
    color: #6e7681; font-size: 12px;
    font-style: italic; padding: 4px 0;
  }
  .pr-setup {
    padding: 22px;
    text-align: center;
    color: #8b949e;
    font-size: 13px; line-height: 1.6;
  }
  .pr-setup a { color: #2f81f7; text-decoration: none; }
  .pr-setup a:hover { text-decoration: underline; }
  .pr-setup code {
    background: #21262d; padding: 2px 6px;
    border-radius: 4px; font-size: 12px;
    color: #c9d1d9;
  }

  /* Learn section */
  #learn-mode { display: none; }
  #learn-mode.active { display: block; }
  .learn-hero {
    background: linear-gradient(135deg, #161b22 0%, #1c2530 100%);
    border: 1px solid #30363d;
    border-radius: 10px;
    padding: 26px 32px;
    margin-bottom: 18px;
  }
  .learn-hero-tag {
    display: inline-block;
    font-size: 11px; letter-spacing: 0.6px;
    color: #2f81f7;
    background: rgba(47, 129, 247, 0.1);
    padding: 4px 10px;
    border-radius: 12px;
    margin-bottom: 12px;
    text-transform: uppercase;
    font-weight: 500;
  }
  .learn-hero h2 {
    font-size: 22px; font-weight: 500;
    margin-bottom: 12px; color: #e6edf3;
    letter-spacing: -0.3px;
  }
  .learn-hero p { font-size: 15px; line-height: 1.7; color: #c9d1d9; }
  .learn-hero-attr {
    font-size: 12px; color: #6e7681;
    margin-top: 14px; font-style: italic;
  }
  .learn-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px;
    margin-bottom: 18px;
  }
  @media (max-width: 900px) { .learn-grid { grid-template-columns: 1fr; } }
  .learn-card {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 10px;
    padding: 22px 24px;
  }
  .learn-card h3 {
    font-size: 15px; font-weight: 500;
    margin-bottom: 14px; color: #e6edf3;
    display: flex; align-items: center; gap: 8px;
  }
  .learn-card h3 .ico { font-size: 18px; }
  .learn-card p {
    font-size: 13px; line-height: 1.7;
    color: #c9d1d9; margin-bottom: 10px;
  }
  .learn-card ul { list-style: none; padding: 0; }
  .learn-card li {
    font-size: 13px; line-height: 1.6;
    color: #c9d1d9; padding: 10px 0;
    border-bottom: 1px solid #21262d;
    display: flex; align-items: flex-start; gap: 10px;
  }
  .learn-card li:last-child { border-bottom: none; padding-bottom: 0; }
  .learn-card li .num {
    background: #21262d;
    border: 1px solid #30363d;
    border-radius: 50%;
    width: 22px; height: 22px;
    display: flex; align-items: center; justify-content: center;
    font-size: 11px; font-weight: 600;
    flex-shrink: 0; color: #2f81f7;
  }
  .learn-card li strong.term {
    color: #e6edf3; font-weight: 500; display: block;
    margin-bottom: 2px;
  }

  /* DCA Calculator */
  .dca-calc {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 10px;
    padding: 24px 28px;
    margin-bottom: 18px;
  }
  .dca-calc h3 {
    font-size: 16px; font-weight: 500;
    margin-bottom: 6px; color: #e6edf3;
  }
  .dca-calc-sub {
    font-size: 12px; color: #8b949e; margin-bottom: 18px;
  }
  .dca-calc-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px; margin-bottom: 20px;
  }
  @media (max-width: 700px) { .dca-calc-grid { grid-template-columns: 1fr; } }
  .dca-input-group { display: flex; flex-direction: column; gap: 8px; }
  .dca-input-label {
    font-size: 12px; color: #8b949e;
    display: flex; justify-content: space-between;
  }
  .dca-input-label span:last-child {
    color: #2f81f7; font-weight: 600;
    font-variant-numeric: tabular-nums;
  }
  .dca-input-group input[type="range"] {
    width: 100%;
    -webkit-appearance: none; appearance: none;
    height: 4px; background: #30363d;
    border-radius: 2px; outline: none;
  }
  .dca-input-group input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 18px; height: 18px;
    background: #2f81f7;
    border-radius: 50%; cursor: pointer;
  }
  .dca-input-group input[type="range"]::-moz-range-thumb {
    width: 18px; height: 18px;
    background: #2f81f7;
    border-radius: 50%; cursor: pointer; border: none;
  }
  .dca-results {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1px;
    background: #30363d;
    border-radius: 8px; overflow: hidden;
  }
  @media (max-width: 700px) { .dca-results { grid-template-columns: 1fr; } }
  .dca-result {
    text-align: center;
    padding: 16px 12px;
    background: #0d1117;
  }
  .dca-result-label {
    font-size: 11px; color: #8b949e;
    text-transform: uppercase;
    letter-spacing: 0.4px; margin-bottom: 8px;
  }
  .dca-result-value {
    font-size: 22px; font-weight: 600;
    font-variant-numeric: tabular-nums;
  }
  .dca-result-value.invested { color: #c9d1d9; }
  .dca-result-value.growth { color: #3fb950; }
  .dca-result-value.total { color: #2f81f7; font-size: 24px; }

  /* Resources */
  .resources-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
  }
  @media (max-width: 800px) { .resources-grid { grid-template-columns: repeat(2, 1fr); } }
  @media (max-width: 500px) { .resources-grid { grid-template-columns: 1fr; } }
  .resource-link {
    display: block;
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 14px 16px;
    text-decoration: none;
    transition: all 0.15s;
  }
  .resource-link:hover {
    background: #21262d;
    border-color: #2f81f7;
    transform: translateY(-1px);
  }
  .resource-name {
    font-size: 13px; font-weight: 500;
    color: #2f81f7; margin-bottom: 4px;
  }
  .resource-desc {
    font-size: 11px; color: #8b949e; line-height: 1.4;
  }

  /* Glossary */
  .glossary {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 10px;
    padding: 22px 26px;
  }
  .glossary h3 {
    font-size: 16px; font-weight: 500;
    margin-bottom: 14px; color: #e6edf3;
  }
  .glossary-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0 24px;
  }
  @media (max-width: 700px) { .glossary-grid { grid-template-columns: 1fr; } }
  .glossary-item {
    padding: 10px 0;
    border-bottom: 1px solid #21262d;
  }
  .glossary-term {
    font-size: 13px; font-weight: 600;
    color: #2f81f7; margin-bottom: 4px;
  }
  .glossary-def { font-size: 12px; color: #c9d1d9; line-height: 1.5; }
  .section-heading {
    font-size: 13px; font-weight: 500;
    color: #8b949e; margin: 24px 4px 12px;
    text-transform: uppercase; letter-spacing: 0.6px;
  }
</style>
</head>
<body>

<div class="header">
  <div class="header-title">
    <div class="logo-mark">$</div>
    <div>
      <h1>Personal Investor Dashboard</h1>
      <div class="header-meta">Tracking <span>MU · AVGO · PLTR · TSLA · NVDA</span> · Data refreshes on page load</div>
    </div>
  </div>
  <div class="header-meta" id="last-updated">Last opened: <span id="timestamp"></span></div>
</div>

<!-- Live ticker tape -->
<div class="ticker-bar">
  <div class="tradingview-widget-container">
    <div class="tradingview-widget-container__widget"></div>
    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>
    {
      "symbols": [
        {"description": "Micron", "proName": "NASDAQ:MU"},
        {"description": "Broadcom", "proName": "NASDAQ:AVGO"},
        {"description": "Palantir", "proName": "NASDAQ:PLTR"},
        {"description": "Tesla", "proName": "NASDAQ:TSLA"},
        {"description": "NVIDIA", "proName": "NASDAQ:NVDA"},
        {"description": "S&P 500", "proName": "FOREXCOM:SPXUSD"},
        {"description": "Nasdaq 100", "proName": "FOREXCOM:NSXUSD"},
        {"description": "VIX", "proName": "CAPITALCOM:VIX"}
      ],
      "showSymbolLogo": true,
      "isTransparent": true,
      "displayMode": "adaptive",
      "colorTheme": "dark",
      "locale": "en"
    }
    </script>
  </div>
</div>

<!-- Tab navigation -->
<div class="tabs" id="tabs">
  <button class="tab active" data-symbol="MU"><span class="tab-symbol">MU</span>Micron</button>
  <button class="tab" data-symbol="AVGO"><span class="tab-symbol">AVGO</span>Broadcom</button>
  <button class="tab" data-symbol="PLTR"><span class="tab-symbol">PLTR</span>Palantir</button>
  <button class="tab" data-symbol="TSLA"><span class="tab-symbol">TSLA</span>Tesla</button>
  <button class="tab" data-symbol="NVDA"><span class="tab-symbol">NVDA</span>NVIDIA</button>
  <button class="tab" data-symbol="LEARN" style="margin-left:auto; border-left: 1px solid #30363d;"><span class="tab-symbol">📚</span>Learn</button>
</div>

<div class="container">

  <div id="stock-mode">

  <div class="disclaimer">
    <strong>How to read this dashboard:</strong> The "Signal" panel below aggregates real technical indicators — moving averages (MA5–MA200), RSI, MACD, Stochastic, ADX, CCI, Williams %R, Bull/Bear Power, and Ultimate Oscillator — into a single rating. These signals are <strong>technical analysis</strong>, not investment advice. They reflect short-term price momentum and trend strength, not company fundamentals or your tax situation. Use them as one input among many — combine with fundamentals (right panel), earnings dates, and your own thesis. Switch the Signal panel between 1m / 5m / 15m / 1h / 4h / 1D / 1W timeframes; daily and weekly are most useful for swing decisions.
  </div>

  <!-- Veteran's Buy Signal — dynamic panel, updates with active tab -->
  <div class="vet-panel" id="vet-panel">
    <div class="vet-top">
      <div class="vet-light gray" id="vet-light"></div>
      <div class="vet-info-section">
        <div class="vet-section-title">Veteran's Buy Signal · <strong id="vet-symbol">MU</strong> <span id="vet-asof" style="color:#6e7681; font-weight:400; text-transform:none; letter-spacing:0;"></span><button class="vet-refresh" id="vet-refresh" title="Refresh signals">↻ Refresh</button></div>
        <div class="vet-status-text gray" id="vet-status-text">LOADING</div>
        <div class="vet-summary" id="vet-summary">Fetching market data and computing signals…</div>
      </div>
      <div class="vet-score">
        <div class="vet-score-num" id="vet-score-num">—</div>
        <div class="vet-score-label">/ 6 signals</div>
      </div>
    </div>
    <div class="vet-checks" id="vet-checks"></div>
    <div class="vet-attribution">
      <strong>Indicators evaluated:</strong> Wilder RSI(14) bounce from oversold · Stan Weinstein 200-day MA rule · Appel MACD(12,26,9) bullish state · Minervini/O'Neil buyable pullback in uptrend · Wyckoff volume confirmation · Classic 50/200 MA golden cross. Data: Yahoo Finance daily bars. <strong>Educational only — not investment advice.</strong>
    </div>
  </div>

  <!-- Long-Term Metrics — for the patient, DCA-style investor -->
  <div class="lt-panel" id="lt-panel">
    <div class="lt-header">
      <span class="lt-title">Long-Term Metrics · <strong id="lt-symbol">MU</strong></span>
      <span class="lt-asof" id="lt-asof"></span>
    </div>
    <div class="lt-stats">
      <div class="lt-stat"><div class="lt-stat-label">Price</div><div class="lt-stat-value" id="lt-price">—</div></div>
      <div class="lt-stat"><div class="lt-stat-label">YTD</div><div class="lt-stat-value" id="lt-ytd">—</div></div>
      <div class="lt-stat"><div class="lt-stat-label">1Y CAGR</div><div class="lt-stat-value" id="lt-cagr1">—</div></div>
      <div class="lt-stat"><div class="lt-stat-label">3Y CAGR</div><div class="lt-stat-value" id="lt-cagr3">—</div></div>
      <div class="lt-stat"><div class="lt-stat-label">5Y CAGR</div><div class="lt-stat-value" id="lt-cagr5">—</div></div>
      <div class="lt-stat"><div class="lt-stat-label">From 200-MA</div><div class="lt-stat-value" id="lt-ma200d">—</div></div>
    </div>
    <div class="lt-range">
      <div class="lt-range-header">
        <span><strong id="lt-range-pos-text">—</strong> of 52-week range</span>
        <span id="lt-range-drawdown" style="color:#8b949e;">— from high</span>
      </div>
      <div class="lt-range-bar">
        <div class="lt-range-marker" id="lt-range-marker" style="left:50%;"></div>
      </div>
      <div class="lt-range-labels">
        <span id="lt-range-low">$—</span>
        <span id="lt-range-high">$—</span>
      </div>
    </div>
    <div class="lt-dca">
      <div class="lt-dca-header">
        <span class="lt-dca-title">💎 DCA Bargain Meter</span>
        <span class="lt-dca-rating" id="lt-dca-rating">—</span>
      </div>
      <div class="lt-dca-dots" id="lt-dca-dots">
        <div class="dca-dot"></div><div class="dca-dot"></div><div class="dca-dot"></div><div class="dca-dot"></div><div class="dca-dot"></div>
      </div>
      <div class="lt-dca-explain" id="lt-dca-explain">For long-term DCA investors: scores 4–5 dots = exceptionally attractive entry; 2–3 = fair value, continue normal DCA; 0–1 = price elevated, consider smaller adds. Based on RSI, distance from 200-MA, drawdown from 52-week high, and 52-week range position. Caps at 2 dots if long-term trend (50/200 MA) is broken — never accelerate buys into a falling knife.</div>
    </div>
  </div>

  <!-- Public Record — driven by data/feed.json (updated daily by GitHub Actions) -->
  <div class="pr-panel" id="pr-panel">
    <div class="pr-header">
      <span class="pr-title">Public Record · <strong id="pr-symbol">MU</strong></span>
      <span class="pr-asof" id="pr-asof">Loading…</span>
    </div>
    <div id="pr-body">
      <div class="pr-setup">
        Loading public record data from <code>./data/feed.json</code>…
      </div>
    </div>
  </div>

  <!-- ============ MU ============ -->
  <div class="stock-view active" data-view="MU">
    <div class="grid-top">
      <div class="panel">
        <div class="panel-header">
          <span class="panel-title">Symbol Overview</span>
          <span class="panel-badge">NASDAQ : MU</span>
        </div>
        <div class="panel-body info-panel">
          <div class="tradingview-widget-container" style="height:100%;">
            <div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-info.js" async>
            {"symbol":"NASDAQ:MU","colorTheme":"dark","isTransparent":true,"locale":"en","width":"100%"}
            </script>
          </div>
        </div>
      </div>
      <div class="panel">
        <div class="panel-header">
          <span class="panel-title">Mini Chart · 12 Month</span>
          <span class="panel-badge">Trend</span>
        </div>
        <div class="panel-body info-panel">
          <div class="tradingview-widget-container" style="height:100%;">
            <div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>
            {"symbol":"NASDAQ:MU","width":"100%","height":"100%","locale":"en","dateRange":"12M","colorTheme":"dark","isTransparent":true,"autosize":true,"largeChartUrl":""}
            </script>
          </div>
        </div>
      </div>
    </div>

    <div class="grid-main">
      <div class="panel chart-panel">
        <div class="panel-header">
          <span class="panel-title">Advanced Chart · MU</span>
          <span class="panel-badge">Live</span>
        </div>
        <div class="panel-body" style="height:540px;">
          <div class="tradingview-widget-container" style="height:100%;width:100%;">
            <div class="tradingview-widget-container__widget" style="height:100%;width:100%;"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js" async>
            {"autosize":true,"symbol":"NASDAQ:MU","interval":"D","timezone":"America/Los_Angeles","theme":"dark","style":"1","locale":"en","enable_publishing":false,"hide_side_toolbar":false,"allow_symbol_change":false,"studies":["STD;RSI","STD;MACD","STD;EMA"],"backgroundColor":"#0d1117"}
            </script>
          </div>
        </div>
      </div>

      <div class="panel signal-panel">
        <div class="panel-header">
          <span class="panel-title">⚡ Buy / Hold / Sell Signal</span>
          <span class="panel-badge">Tech analysis</span>
        </div>
        <div class="panel-body" style="height:380px;">
          <div class="tradingview-widget-container" style="height:100%;">
            <div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
            {"interval":"1D","width":"100%","isTransparent":true,"height":"100%","symbol":"NASDAQ:MU","showIntervalTabs":true,"displayMode":"single","locale":"en","colorTheme":"dark"}
            </script>
          </div>
        </div>
        <div class="legend">
          <div class="legend-item leg-strong-buy"><span class="label">STR BUY</span><span class="desc">Strong momentum up</span></div>
          <div class="legend-item leg-buy"><span class="label">BUY</span><span class="desc">Trending up</span></div>
          <div class="legend-item leg-neutral"><span class="label">NEUTRAL</span><span class="desc">No clear trend</span></div>
          <div class="legend-item leg-sell"><span class="label">SELL</span><span class="desc">Trending down</span></div>
          <div class="legend-item leg-strong-sell"><span class="label">STR SELL</span><span class="desc">Strong momentum down</span></div>
        </div>
      </div>
    </div>

    <div class="grid-bottom">
      <div class="panel fundamentals-panel">
        <div class="panel-header">
          <span class="panel-title">Fundamentals · MU</span>
          <span class="panel-badge">Quarterly</span>
        </div>
        <div class="panel-body" style="height:400px;">
          <div class="tradingview-widget-container" style="height:100%;">
            <div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-financials.js" async>
            {"isTransparent":true,"largeChartUrl":"","displayMode":"regular","width":"100%","height":"100%","colorTheme":"dark","symbol":"NASDAQ:MU","locale":"en"}
            </script>
          </div>
        </div>
      </div>
      <div class="panel news-panel">
        <div class="panel-header">
          <span class="panel-title">News & Headlines · MU</span>
          <span class="panel-badge">Latest</span>
        </div>
        <div class="panel-body" style="height:400px;">
          <div class="tradingview-widget-container" style="height:100%;">
            <div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>
            {"feedMode":"symbol","symbol":"NASDAQ:MU","isTransparent":true,"displayMode":"regular","width":"100%","height":"100%","colorTheme":"dark","locale":"en"}
            </script>
          </div>
        </div>
        <div class="quick-links">
          <a class="quick-link" href="https://finance.yahoo.com/quote/MU" target="_blank">Yahoo Finance</a>
          <a class="quick-link" href="https://www.google.com/finance/quote/MU:NASDAQ" target="_blank">Google Finance</a>
          <a class="quick-link" href="https://seekingalpha.com/symbol/MU" target="_blank">Seeking Alpha</a>
          <a class="quick-link" href="https://finviz.com/quote.ashx?t=MU" target="_blank">Finviz</a>
          <a class="quick-link" href="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=MU&type=10-K" target="_blank">SEC Filings</a>
        </div>
      </div>
    </div>
  </div>

  <!-- ============ AVGO ============ -->
  <div class="stock-view" data-view="AVGO">
    <div class="grid-top">
      <div class="panel">
        <div class="panel-header"><span class="panel-title">Symbol Overview</span><span class="panel-badge">NASDAQ : AVGO</span></div>
        <div class="panel-body info-panel">
          <div class="tradingview-widget-container" style="height:100%;"><div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-info.js" async>
            {"symbol":"NASDAQ:AVGO","colorTheme":"dark","isTransparent":true,"locale":"en","width":"100%"}
            </script>
          </div>
        </div>
      </div>
      <div class="panel">
        <div class="panel-header"><span class="panel-title">Mini Chart · 12 Month</span><span class="panel-badge">Trend</span></div>
        <div class="panel-body info-panel">
          <div class="tradingview-widget-container" style="height:100%;"><div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>
            {"symbol":"NASDAQ:AVGO","width":"100%","height":"100%","locale":"en","dateRange":"12M","colorTheme":"dark","isTransparent":true,"autosize":true}
            </script>
          </div>
        </div>
      </div>
    </div>
    <div class="grid-main">
      <div class="panel chart-panel">
        <div class="panel-header"><span class="panel-title">Advanced Chart · AVGO</span><span class="panel-badge">Live</span></div>
        <div class="panel-body" style="height:540px;">
          <div class="tradingview-widget-container" style="height:100%;width:100%;"><div class="tradingview-widget-container__widget" style="height:100%;width:100%;"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js" async>
            {"autosize":true,"symbol":"NASDAQ:AVGO","interval":"D","timezone":"America/Los_Angeles","theme":"dark","style":"1","locale":"en","enable_publishing":false,"studies":["STD;RSI","STD;MACD","STD;EMA"],"backgroundColor":"#0d1117"}
            </script>
          </div>
        </div>
      </div>
      <div class="panel signal-panel">
        <div class="panel-header"><span class="panel-title">⚡ Buy / Hold / Sell Signal</span><span class="panel-badge">Tech analysis</span></div>
        <div class="panel-body" style="height:380px;">
          <div class="tradingview-widget-container" style="height:100%;"><div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
            {"interval":"1D","width":"100%","isTransparent":true,"height":"100%","symbol":"NASDAQ:AVGO","showIntervalTabs":true,"displayMode":"single","locale":"en","colorTheme":"dark"}
            </script>
          </div>
        </div>
        <div class="legend">
          <div class="legend-item leg-strong-buy"><span class="label">STR BUY</span><span class="desc">Strong momentum up</span></div>
          <div class="legend-item leg-buy"><span class="label">BUY</span><span class="desc">Trending up</span></div>
          <div class="legend-item leg-neutral"><span class="label">NEUTRAL</span><span class="desc">No clear trend</span></div>
          <div class="legend-item leg-sell"><span class="label">SELL</span><span class="desc">Trending down</span></div>
          <div class="legend-item leg-strong-sell"><span class="label">STR SELL</span><span class="desc">Strong momentum down</span></div>
        </div>
      </div>
    </div>
    <div class="grid-bottom">
      <div class="panel fundamentals-panel">
        <div class="panel-header"><span class="panel-title">Fundamentals · AVGO</span><span class="panel-badge">Quarterly</span></div>
        <div class="panel-body" style="height:400px;">
          <div class="tradingview-widget-container" style="height:100%;"><div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-financials.js" async>
            {"isTransparent":true,"displayMode":"regular","width":"100%","height":"100%","colorTheme":"dark","symbol":"NASDAQ:AVGO","locale":"en"}
            </script>
          </div>
        </div>
      </div>
      <div class="panel news-panel">
        <div class="panel-header"><span class="panel-title">News & Headlines · AVGO</span><span class="panel-badge">Latest</span></div>
        <div class="panel-body" style="height:400px;">
          <div class="tradingview-widget-container" style="height:100%;"><div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>
            {"feedMode":"symbol","symbol":"NASDAQ:AVGO","isTransparent":true,"displayMode":"regular","width":"100%","height":"100%","colorTheme":"dark","locale":"en"}
            </script>
          </div>
        </div>
        <div class="quick-links">
          <a class="quick-link" href="https://finance.yahoo.com/quote/AVGO" target="_blank">Yahoo Finance</a>
          <a class="quick-link" href="https://www.google.com/finance/quote/AVGO:NASDAQ" target="_blank">Google Finance</a>
          <a class="quick-link" href="https://seekingalpha.com/symbol/AVGO" target="_blank">Seeking Alpha</a>
          <a class="quick-link" href="https://finviz.com/quote.ashx?t=AVGO" target="_blank">Finviz</a>
          <a class="quick-link" href="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=AVGO&type=10-K" target="_blank">SEC Filings</a>
        </div>
      </div>
    </div>
  </div>

  <!-- ============ PLTR ============ -->
  <div class="stock-view" data-view="PLTR">
    <div class="grid-top">
      <div class="panel">
        <div class="panel-header"><span class="panel-title">Symbol Overview</span><span class="panel-badge">NASDAQ : PLTR</span></div>
        <div class="panel-body info-panel">
          <div class="tradingview-widget-container" style="height:100%;"><div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-info.js" async>
            {"symbol":"NASDAQ:PLTR","colorTheme":"dark","isTransparent":true,"locale":"en","width":"100%"}
            </script>
          </div>
        </div>
      </div>
      <div class="panel">
        <div class="panel-header"><span class="panel-title">Mini Chart · 12 Month</span><span class="panel-badge">Trend</span></div>
        <div class="panel-body info-panel">
          <div class="tradingview-widget-container" style="height:100%;"><div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>
            {"symbol":"NASDAQ:PLTR","width":"100%","height":"100%","locale":"en","dateRange":"12M","colorTheme":"dark","isTransparent":true,"autosize":true}
            </script>
          </div>
        </div>
      </div>
    </div>
    <div class="grid-main">
      <div class="panel chart-panel">
        <div class="panel-header"><span class="panel-title">Advanced Chart · PLTR</span><span class="panel-badge">Live</span></div>
        <div class="panel-body" style="height:540px;">
          <div class="tradingview-widget-container" style="height:100%;width:100%;"><div class="tradingview-widget-container__widget" style="height:100%;width:100%;"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js" async>
            {"autosize":true,"symbol":"NASDAQ:PLTR","interval":"D","timezone":"America/Los_Angeles","theme":"dark","style":"1","locale":"en","enable_publishing":false,"studies":["STD;RSI","STD;MACD","STD;EMA"],"backgroundColor":"#0d1117"}
            </script>
          </div>
        </div>
      </div>
      <div class="panel signal-panel">
        <div class="panel-header"><span class="panel-title">⚡ Buy / Hold / Sell Signal</span><span class="panel-badge">Tech analysis</span></div>
        <div class="panel-body" style="height:380px;">
          <div class="tradingview-widget-container" style="height:100%;"><div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
            {"interval":"1D","width":"100%","isTransparent":true,"height":"100%","symbol":"NASDAQ:PLTR","showIntervalTabs":true,"displayMode":"single","locale":"en","colorTheme":"dark"}
            </script>
          </div>
        </div>
        <div class="legend">
          <div class="legend-item leg-strong-buy"><span class="label">STR BUY</span><span class="desc">Strong momentum up</span></div>
          <div class="legend-item leg-buy"><span class="label">BUY</span><span class="desc">Trending up</span></div>
          <div class="legend-item leg-neutral"><span class="label">NEUTRAL</span><span class="desc">No clear trend</span></div>
          <div class="legend-item leg-sell"><span class="label">SELL</span><span class="desc">Trending down</span></div>
          <div class="legend-item leg-strong-sell"><span class="label">STR SELL</span><span class="desc">Strong momentum down</span></div>
        </div>
      </div>
    </div>
    <div class="grid-bottom">
      <div class="panel fundamentals-panel">
        <div class="panel-header"><span class="panel-title">Fundamentals · PLTR</span><span class="panel-badge">Quarterly</span></div>
        <div class="panel-body" style="height:400px;">
          <div class="tradingview-widget-container" style="height:100%;"><div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-financials.js" async>
            {"isTransparent":true,"displayMode":"regular","width":"100%","height":"100%","colorTheme":"dark","symbol":"NASDAQ:PLTR","locale":"en"}
            </script>
          </div>
        </div>
      </div>
      <div class="panel news-panel">
        <div class="panel-header"><span class="panel-title">News & Headlines · PLTR</span><span class="panel-badge">Latest</span></div>
        <div class="panel-body" style="height:400px;">
          <div class="tradingview-widget-container" style="height:100%;"><div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>
            {"feedMode":"symbol","symbol":"NASDAQ:PLTR","isTransparent":true,"displayMode":"regular","width":"100%","height":"100%","colorTheme":"dark","locale":"en"}
            </script>
          </div>
        </div>
        <div class="quick-links">
          <a class="quick-link" href="https://finance.yahoo.com/quote/PLTR" target="_blank">Yahoo Finance</a>
          <a class="quick-link" href="https://www.google.com/finance/quote/PLTR:NASDAQ" target="_blank">Google Finance</a>
          <a class="quick-link" href="https://seekingalpha.com/symbol/PLTR" target="_blank">Seeking Alpha</a>
          <a class="quick-link" href="https://finviz.com/quote.ashx?t=PLTR" target="_blank">Finviz</a>
          <a class="quick-link" href="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=PLTR&type=10-K" target="_blank">SEC Filings</a>
        </div>
      </div>
    </div>
  </div>

  <!-- ============ TSLA ============ -->
  <div class="stock-view" data-view="TSLA">
    <div class="grid-top">
      <div class="panel">
        <div class="panel-header"><span class="panel-title">Symbol Overview</span><span class="panel-badge">NASDAQ : TSLA</span></div>
        <div class="panel-body info-panel">
          <div class="tradingview-widget-container" style="height:100%;"><div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-info.js" async>
            {"symbol":"NASDAQ:TSLA","colorTheme":"dark","isTransparent":true,"locale":"en","width":"100%"}
            </script>
          </div>
        </div>
      </div>
      <div class="panel">
        <div class="panel-header"><span class="panel-title">Mini Chart · 12 Month</span><span class="panel-badge">Trend</span></div>
        <div class="panel-body info-panel">
          <div class="tradingview-widget-container" style="height:100%;"><div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>
            {"symbol":"NASDAQ:TSLA","width":"100%","height":"100%","locale":"en","dateRange":"12M","colorTheme":"dark","isTransparent":true,"autosize":true}
            </script>
          </div>
        </div>
      </div>
    </div>
    <div class="grid-main">
      <div class="panel chart-panel">
        <div class="panel-header"><span class="panel-title">Advanced Chart · TSLA</span><span class="panel-badge">Live</span></div>
        <div class="panel-body" style="height:540px;">
          <div class="tradingview-widget-container" style="height:100%;width:100%;"><div class="tradingview-widget-container__widget" style="height:100%;width:100%;"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js" async>
            {"autosize":true,"symbol":"NASDAQ:TSLA","interval":"D","timezone":"America/Los_Angeles","theme":"dark","style":"1","locale":"en","enable_publishing":false,"studies":["STD;RSI","STD;MACD","STD;EMA"],"backgroundColor":"#0d1117"}
            </script>
          </div>
        </div>
      </div>
      <div class="panel signal-panel">
        <div class="panel-header"><span class="panel-title">⚡ Buy / Hold / Sell Signal</span><span class="panel-badge">Tech analysis</span></div>
        <div class="panel-body" style="height:380px;">
          <div class="tradingview-widget-container" style="height:100%;"><div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
            {"interval":"1D","width":"100%","isTransparent":true,"height":"100%","symbol":"NASDAQ:TSLA","showIntervalTabs":true,"displayMode":"single","locale":"en","colorTheme":"dark"}
            </script>
          </div>
        </div>
        <div class="legend">
          <div class="legend-item leg-strong-buy"><span class="label">STR BUY</span><span class="desc">Strong momentum up</span></div>
          <div class="legend-item leg-buy"><span class="label">BUY</span><span class="desc">Trending up</span></div>
          <div class="legend-item leg-neutral"><span class="label">NEUTRAL</span><span class="desc">No clear trend</span></div>
          <div class="legend-item leg-sell"><span class="label">SELL</span><span class="desc">Trending down</span></div>
          <div class="legend-item leg-strong-sell"><span class="label">STR SELL</span><span class="desc">Strong momentum down</span></div>
        </div>
      </div>
    </div>
    <div class="grid-bottom">
      <div class="panel fundamentals-panel">
        <div class="panel-header"><span class="panel-title">Fundamentals · TSLA</span><span class="panel-badge">Quarterly</span></div>
        <div class="panel-body" style="height:400px;">
          <div class="tradingview-widget-container" style="height:100%;"><div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-financials.js" async>
            {"isTransparent":true,"displayMode":"regular","width":"100%","height":"100%","colorTheme":"dark","symbol":"NASDAQ:TSLA","locale":"en"}
            </script>
          </div>
        </div>
      </div>
      <div class="panel news-panel">
        <div class="panel-header"><span class="panel-title">News & Headlines · TSLA</span><span class="panel-badge">Latest</span></div>
        <div class="panel-body" style="height:400px;">
          <div class="tradingview-widget-container" style="height:100%;"><div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>
            {"feedMode":"symbol","symbol":"NASDAQ:TSLA","isTransparent":true,"displayMode":"regular","width":"100%","height":"100%","colorTheme":"dark","locale":"en"}
            </script>
          </div>
        </div>
        <div class="quick-links">
          <a class="quick-link" href="https://finance.yahoo.com/quote/TSLA" target="_blank">Yahoo Finance</a>
          <a class="quick-link" href="https://www.google.com/finance/quote/TSLA:NASDAQ" target="_blank">Google Finance</a>
          <a class="quick-link" href="https://seekingalpha.com/symbol/TSLA" target="_blank">Seeking Alpha</a>
          <a class="quick-link" href="https://finviz.com/quote.ashx?t=TSLA" target="_blank">Finviz</a>
          <a class="quick-link" href="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=TSLA&type=10-K" target="_blank">SEC Filings</a>
        </div>
      </div>
    </div>
  </div>

  <!-- ============ NVDA ============ -->
  <div class="stock-view" data-view="NVDA">
    <div class="grid-top">
      <div class="panel">
        <div class="panel-header"><span class="panel-title">Symbol Overview</span><span class="panel-badge">NASDAQ : NVDA</span></div>
        <div class="panel-body info-panel">
          <div class="tradingview-widget-container" style="height:100%;"><div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-info.js" async>
            {"symbol":"NASDAQ:NVDA","colorTheme":"dark","isTransparent":true,"locale":"en","width":"100%"}
            </script>
          </div>
        </div>
      </div>
      <div class="panel">
        <div class="panel-header"><span class="panel-title">Mini Chart · 12 Month</span><span class="panel-badge">Trend</span></div>
        <div class="panel-body info-panel">
          <div class="tradingview-widget-container" style="height:100%;"><div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>
            {"symbol":"NASDAQ:NVDA","width":"100%","height":"100%","locale":"en","dateRange":"12M","colorTheme":"dark","isTransparent":true,"autosize":true}
            </script>
          </div>
        </div>
      </div>
    </div>
    <div class="grid-main">
      <div class="panel chart-panel">
        <div class="panel-header"><span class="panel-title">Advanced Chart · NVDA</span><span class="panel-badge">Live</span></div>
        <div class="panel-body" style="height:540px;">
          <div class="tradingview-widget-container" style="height:100%;width:100%;"><div class="tradingview-widget-container__widget" style="height:100%;width:100%;"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js" async>
            {"autosize":true,"symbol":"NASDAQ:NVDA","interval":"D","timezone":"America/Los_Angeles","theme":"dark","style":"1","locale":"en","enable_publishing":false,"studies":["STD;RSI","STD;MACD","STD;EMA"],"backgroundColor":"#0d1117"}
            </script>
          </div>
        </div>
      </div>
      <div class="panel signal-panel">
        <div class="panel-header"><span class="panel-title">⚡ Buy / Hold / Sell Signal</span><span class="panel-badge">Tech analysis</span></div>
        <div class="panel-body" style="height:380px;">
          <div class="tradingview-widget-container" style="height:100%;"><div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
            {"interval":"1D","width":"100%","isTransparent":true,"height":"100%","symbol":"NASDAQ:NVDA","showIntervalTabs":true,"displayMode":"single","locale":"en","colorTheme":"dark"}
            </script>
          </div>
        </div>
        <div class="legend">
          <div class="legend-item leg-strong-buy"><span class="label">STR BUY</span><span class="desc">Strong momentum up</span></div>
          <div class="legend-item leg-buy"><span class="label">BUY</span><span class="desc">Trending up</span></div>
          <div class="legend-item leg-neutral"><span class="label">NEUTRAL</span><span class="desc">No clear trend</span></div>
          <div class="legend-item leg-sell"><span class="label">SELL</span><span class="desc">Trending down</span></div>
          <div class="legend-item leg-strong-sell"><span class="label">STR SELL</span><span class="desc">Strong momentum down</span></div>
        </div>
      </div>
    </div>
    <div class="grid-bottom">
      <div class="panel fundamentals-panel">
        <div class="panel-header"><span class="panel-title">Fundamentals · NVDA</span><span class="panel-badge">Quarterly</span></div>
        <div class="panel-body" style="height:400px;">
          <div class="tradingview-widget-container" style="height:100%;"><div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-financials.js" async>
            {"isTransparent":true,"displayMode":"regular","width":"100%","height":"100%","colorTheme":"dark","symbol":"NASDAQ:NVDA","locale":"en"}
            </script>
          </div>
        </div>
      </div>
      <div class="panel news-panel">
        <div class="panel-header"><span class="panel-title">News & Headlines · NVDA</span><span class="panel-badge">Latest</span></div>
        <div class="panel-body" style="height:400px;">
          <div class="tradingview-widget-container" style="height:100%;"><div class="tradingview-widget-container__widget"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>
            {"feedMode":"symbol","symbol":"NASDAQ:NVDA","isTransparent":true,"displayMode":"regular","width":"100%","height":"100%","colorTheme":"dark","locale":"en"}
            </script>
          </div>
        </div>
        <div class="quick-links">
          <a class="quick-link" href="https://finance.yahoo.com/quote/NVDA" target="_blank">Yahoo Finance</a>
          <a class="quick-link" href="https://www.google.com/finance/quote/NVDA:NASDAQ" target="_blank">Google Finance</a>
          <a class="quick-link" href="https://seekingalpha.com/symbol/NVDA" target="_blank">Seeking Alpha</a>
          <a class="quick-link" href="https://finviz.com/quote.ashx?t=NVDA" target="_blank">Finviz</a>
          <a class="quick-link" href="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=NVDA&type=10-K" target="_blank">SEC Filings</a>
        </div>
      </div>
    </div>
  </div>

  </div> <!-- /stock-mode -->

  <!-- ============ LEARN MODE ============ -->
  <div id="learn-mode">

    <!-- Daily Wisdom hero -->
    <div class="learn-hero">
      <span class="learn-hero-tag" id="wisdom-tag">Daily Wisdom</span>
      <h2 id="wisdom-title">Loading today's lesson…</h2>
      <p id="wisdom-body"></p>
      <div class="learn-hero-attr" id="wisdom-attr"></div>
    </div>

    <!-- Core principles -->
    <div class="section-heading">Core principles for the long-term investor</div>
    <div class="learn-grid">
      <div class="learn-card">
        <h3><span class="ico">⏳</span>Time beats timing</h3>
        <p>Decades of S&amp;P 500 data show that missing just the 10 best days over a 20-year period roughly halves your total return. The catch: those best days often come during volatile periods near market lows — exactly when nervous investors panic-sell. For most people, staying invested through downturns isn't just easier — it's mathematically optimal.</p>
      </div>
      <div class="learn-card">
        <h3><span class="ico">📐</span>The DCA math advantage</h3>
        <p>When you buy fixed dollar amounts on a fixed schedule, you automatically buy more shares when prices are low and fewer when prices are high. Over time, your average cost per share will be <em>lower</em> than the average price during the period — a built-in advantage that requires zero forecasting skill, just discipline.</p>
      </div>
      <div class="learn-card">
        <h3><span class="ico">💸</span>Costs compound too</h3>
        <p>A 1% annual expense ratio reduces a 30-year portfolio by roughly 25%. The difference between an index fund at 0.05% and an actively managed fund at 1.0% is staggering over decades. John Bogle called this the "tyranny of compounding costs" — the same compounding that grows your money also grows the costs eroding it.</p>
      </div>
      <div class="learn-card">
        <h3><span class="ico">📈</span>Patience pays disproportionately</h3>
        <p>$10,000 invested at 8% becomes about $46K in 20 years and about $216K in 40 years. Most of the wealth shows up in the final decade. Investors who quit early — or panic-sell during downturns — forfeit the largest gains. The geometry of compounding rewards endurance over cleverness.</p>
      </div>
    </div>

    <!-- DCA Calculator -->
    <div class="dca-calc">
      <h3>📊 DCA Compound Calculator</h3>
      <p class="dca-calc-sub">See what consistent monthly investing compounds into. All sliders are interactive — adjust to model your situation.</p>
      <div class="dca-calc-grid">
        <div class="dca-input-group">
          <div class="dca-input-label"><span>Monthly contribution</span><span id="dca-amount-out">$500</span></div>
          <input type="range" id="dca-amount" min="50" max="5000" step="50" value="500">
        </div>
        <div class="dca-input-group">
          <div class="dca-input-label"><span>Years invested</span><span id="dca-years-out">20 years</span></div>
          <input type="range" id="dca-years" min="1" max="40" step="1" value="20">
        </div>
        <div class="dca-input-group">
          <div class="dca-input-label"><span>Annual return</span><span id="dca-return-out">8.0%</span></div>
          <input type="range" id="dca-return" min="2" max="15" step="0.5" value="8">
        </div>
      </div>
      <div class="dca-results">
        <div class="dca-result">
          <div class="dca-result-label">Total invested</div>
          <div class="dca-result-value invested" id="dca-invested">—</div>
        </div>
        <div class="dca-result">
          <div class="dca-result-label">Investment growth</div>
          <div class="dca-result-value growth" id="dca-growth">—</div>
        </div>
        <div class="dca-result">
          <div class="dca-result-label">Final portfolio value</div>
          <div class="dca-result-value total" id="dca-final">—</div>
        </div>
      </div>
      <p class="dca-calc-sub" style="margin-top:14px;">For context: the S&amp;P 500 has averaged ~10% nominal returns over the last century (~7% real, after inflation). Most planners use 6–8% as a conservative real return baseline. This is a simplified projection — actual year-to-year returns will vary widely.</p>
    </div>

    <!-- Behavioral pitfalls + DCA mistakes -->
    <div class="section-heading">Avoid these traps</div>
    <div class="learn-grid">
      <div class="learn-card">
        <h3><span class="ico">🧠</span>5 behavioral pitfalls</h3>
        <ul>
          <li><span class="num">1</span><div><strong class="term">Recency bias</strong>Treating recent events as a reliable guide to the future. After a crash, expecting more crashes; after a rally, expecting more rallies. Markets rarely look like they just looked.</div></li>
          <li><span class="num">2</span><div><strong class="term">Loss aversion</strong>Behavioral economics shows losses feel about twice as painful as equivalent gains feel pleasant. This causes selling winners too early and holding losers too long — exactly backwards.</div></li>
          <li><span class="num">3</span><div><strong class="term">Action bias</strong>The compulsion to "do something" during volatile markets. With a long time horizon, the best action is usually no action — but that's psychologically the hardest one.</div></li>
          <li><span class="num">4</span><div><strong class="term">Anchoring</strong>Fixating on what you paid for a stock instead of what it's likely worth going forward. Sunk costs should not influence forward decisions, but they almost always do.</div></li>
          <li><span class="num">5</span><div><strong class="term">Confirmation bias</strong>Reading only news that supports your existing position. Actively seek out the bear case for stocks you own — that's where the actual risks live.</div></li>
        </ul>
      </div>
      <div class="learn-card">
        <h3><span class="ico">⚠️</span>5 common DCA mistakes</h3>
        <ul>
          <li><span class="num">1</span><div><strong class="term">Pausing during downturns</strong>This is the worst possible time to stop — you're literally getting more shares per dollar. The math of DCA only works if you stick to it through the scary periods. That's the entire point.</div></li>
          <li><span class="num">2</span><div><strong class="term">Concentration risk</strong>DCA-ing only into one or two names. Even great companies can lose half their value or more. Single-stock DCA is fundamentally different from diversified DCA into a broad index.</div></li>
          <li><span class="num">3</span><div><strong class="term">Ignoring fees</strong>Even small per-trade commissions or high fund expense ratios compound to thousands over decades. Use commission-free brokers and watch every basis point in fund fees.</div></li>
          <li><span class="num">4</span><div><strong class="term">Skipping tax-advantaged accounts</strong>Filling a taxable brokerage before maxing 401(k) match, HSA, or Roth IRA leaves money on the table — sometimes literally tens of thousands over a career.</div></li>
          <li><span class="num">5</span><div><strong class="term">Forgetting to rebalance</strong>Over time, allocations drift. Periodic rebalancing forces you to sell what's gotten expensive and buy what's gotten cheap — a free, mechanical edge.</div></li>
        </ul>
      </div>
    </div>

    <!-- Authoritative free sources -->
    <div class="section-heading">Free authoritative sources · public record &amp; official data</div>
    <div class="resources-grid">
      <a href="https://www.berkshirehathaway.com/letters/letters.html" target="_blank" class="resource-link">
        <div class="resource-name">Berkshire Hathaway Letters</div>
        <div class="resource-desc">Buffett's annual shareholder letters back to 1965. The most-cited investing primary source there is — and they're free.</div>
      </a>
      <a href="https://www.sec.gov/edgar/searchedgar/companysearch" target="_blank" class="resource-link">
        <div class="resource-name">SEC EDGAR</div>
        <div class="resource-desc">Every public company's filings: 10-K (annual), 10-Q (quarterly), 8-K (material events), insider Form 4 transactions.</div>
      </a>
      <a href="https://fred.stlouisfed.org/" target="_blank" class="resource-link">
        <div class="resource-name">FRED · St. Louis Fed</div>
        <div class="resource-desc">Free data on rates, inflation, GDP, employment, money supply — the macro backdrop for every investment decision.</div>
      </a>
      <a href="https://www.bogleheads.org/wiki/Main_Page" target="_blank" class="resource-link">
        <div class="resource-name">Bogleheads Wiki</div>
        <div class="resource-desc">Community-built reference on index investing, asset allocation, and tax-efficient placement — Bogle's philosophy applied.</div>
      </a>
      <a href="https://www.bls.gov/cpi/" target="_blank" class="resource-link">
        <div class="resource-name">BLS · Inflation data</div>
        <div class="resource-desc">Bureau of Labor Statistics CPI reports — what inflation is actually doing to your purchasing power right now.</div>
      </a>
      <a href="https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics" target="_blank" class="resource-link">
        <div class="resource-name">Treasury Yield Curve</div>
        <div class="resource-desc">Daily Treasury yields (1-month through 30-year). The risk-free rate against which all investments are measured.</div>
      </a>
      <a href="https://www.investor.gov/" target="_blank" class="resource-link">
        <div class="resource-name">Investor.gov · SEC</div>
        <div class="resource-desc">SEC's official educational hub. Especially useful for fraud warnings, fee comparisons, and BrokerCheck.</div>
      </a>
      <a href="https://www.finra.org/investors/learn-to-invest" target="_blank" class="resource-link">
        <div class="resource-name">FINRA Education</div>
        <div class="resource-desc">Industry self-regulator. BrokerCheck, fund analyzer, and risk meter tools are genuinely useful and free.</div>
      </a>
      <a href="https://www.morningstar.com/" target="_blank" class="resource-link">
        <div class="resource-name">Morningstar</div>
        <div class="resource-desc">Independent fund research. Star ratings have known limits, but their analyst write-ups and X-ray tools are valuable.</div>
      </a>
    </div>

    <div class="section-heading">Direct filings · your portfolio companies</div>
    <div class="resources-grid">
      <a href="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=MU&type=10-K" target="_blank" class="resource-link">
        <div class="resource-name">MU · Micron 10-K filings</div>
        <div class="resource-desc">Annual reports — most comprehensive document a company files. Always read the Risk Factors section.</div>
      </a>
      <a href="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=AVGO&type=10-K" target="_blank" class="resource-link">
        <div class="resource-name">AVGO · Broadcom 10-K filings</div>
        <div class="resource-desc">Annual reports — covers business model, customer concentration, and management's own commentary.</div>
      </a>
      <a href="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=PLTR&type=10-K" target="_blank" class="resource-link">
        <div class="resource-name">PLTR · Palantir 10-K filings</div>
        <div class="resource-desc">Annual reports — tracks customer concentration, contract durations, government vs commercial revenue mix.</div>
      </a>
      <a href="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=TSLA&type=10-K" target="_blank" class="resource-link">
        <div class="resource-name">TSLA · Tesla 10-K filings</div>
        <div class="resource-desc">Annual reports — production guidance, regulatory credits, energy/auto segment breakdown.</div>
      </a>
      <a href="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=NVDA&type=10-K" target="_blank" class="resource-link">
        <div class="resource-name">NVDA · NVIDIA 10-K filings</div>
        <div class="resource-desc">Annual reports — segment revenue, customer concentration, geographic exposure (especially China).</div>
      </a>
    </div>

    <!-- Glossary -->
    <div class="section-heading">Glossary · the terms that actually matter</div>
    <div class="glossary">
      <div class="glossary-grid">
        <div class="glossary-item"><div class="glossary-term">CAGR</div><div class="glossary-def">Compound Annual Growth Rate — the constant annual rate that turns your starting value into your ending value over a period. Smooths out year-to-year volatility for cleaner comparison.</div></div>
        <div class="glossary-item"><div class="glossary-term">DCA</div><div class="glossary-def">Dollar-Cost Averaging — investing fixed dollar amounts on a fixed schedule regardless of price. Mathematically guarantees a lower average cost than the period's average price.</div></div>
        <div class="glossary-item"><div class="glossary-term">P/E Ratio</div><div class="glossary-def">Price-to-Earnings ratio. Stock price divided by annual earnings per share. Tells you what investors will pay for $1 of profit. Lower can mean cheaper or troubled — context matters.</div></div>
        <div class="glossary-item"><div class="glossary-term">EPS</div><div class="glossary-def">Earnings Per Share — net income divided by share count. Forward EPS uses estimates; trailing EPS uses past 12 months. Both useful for different reasons.</div></div>
        <div class="glossary-item"><div class="glossary-term">Free Cash Flow</div><div class="glossary-def">Cash from operations minus capital expenditures. Harder to manipulate than earnings. Buffett famously focuses on this over reported profits.</div></div>
        <div class="glossary-item"><div class="glossary-term">Beta</div><div class="glossary-def">Stock's volatility relative to the market. 1.0 = moves with market; 1.5 = swings 50% more; 0.5 = half as much. High beta = more pain in downturns, more gains in rallies.</div></div>
        <div class="glossary-item"><div class="glossary-term">Moat</div><div class="glossary-def">Buffett's term for a sustainable competitive advantage: brand power, network effects, switching costs, or genuine cost advantages. Wide moats produce durable returns.</div></div>
        <div class="glossary-item"><div class="glossary-term">Margin of Safety</div><div class="glossary-def">Graham's principle: only buy when market price is significantly below your estimate of intrinsic value. The gap is your buffer against mistakes and bad luck.</div></div>
        <div class="glossary-item"><div class="glossary-term">200-day MA</div><div class="glossary-def">200-day moving average — rolling average closing price over the last 200 trading days (~10 months). Stan Weinstein's classic long-term trend filter.</div></div>
        <div class="glossary-item"><div class="glossary-term">RSI</div><div class="glossary-def">Relative Strength Index — oscillates 0–100. Above 70 often overbought; below 30 often oversold. Wilder developed it in 1978; still widely used today.</div></div>
        <div class="glossary-item"><div class="glossary-term">MACD</div><div class="glossary-def">Moving Average Convergence Divergence — momentum indicator showing the relationship between two EMAs. Cross above signal line is bullish; cross below is bearish.</div></div>
        <div class="glossary-item"><div class="glossary-term">Golden Cross</div><div class="glossary-def">When the 50-day MA crosses above the 200-day MA — historically a long-term bullish signal. Death Cross is the opposite (bearish).</div></div>
        <div class="glossary-item"><div class="glossary-term">Drawdown</div><div class="glossary-def">The peak-to-trough decline of an investment. Maximum drawdown is the worst such decline historically. Useful for understanding worst-case scenarios.</div></div>
        <div class="glossary-item"><div class="glossary-term">Sharpe Ratio</div><div class="glossary-def">Return per unit of risk taken. Higher is better. Specifically: (return − risk-free rate) / standard deviation. Compares investments on a risk-adjusted basis.</div></div>
        <div class="glossary-item"><div class="glossary-term">Dividend Yield</div><div class="glossary-def">Annual dividends per share divided by stock price. A 3% yield means $3 in dividends per $100 invested annually. Beware of unusually high yields — often signals trouble.</div></div>
        <div class="glossary-item"><div class="glossary-term">Volatility</div><div class="glossary-def">Statistical measure of how much price swings around its average. Often confused with risk, but for long-term investors they're not the same thing.</div></div>
      </div>
    </div>

  </div> <!-- /learn-mode -->

</div>

<div class="footer">
  Data provided by <a href="https://www.tradingview.com/" target="_blank">TradingView</a> · For personal use only · Not investment advice
</div>

<script>
  // ================ Tab switching ================
  const tabs = document.querySelectorAll('.tab');
  const views = document.querySelectorAll('.stock-view');
  const stockMode = document.getElementById('stock-mode');
  const learnMode = document.getElementById('learn-mode');
  let activeSymbol = 'MU';

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const sym = tab.getAttribute('data-symbol');
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      if (sym === 'LEARN') {
        stockMode.style.display = 'none';
        learnMode.classList.add('active');
      } else {
        stockMode.style.display = '';
        learnMode.classList.remove('active');
        views.forEach(v => v.classList.remove('active'));
        document.querySelector(`.stock-view[data-view="${sym}"]`).classList.add('active');
        activeSymbol = sym;
        renderVetPanel(sym);
        renderLtPanel(sym);
        renderPrPanel(sym);
      }
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  });

  // ================ Timestamp ================
  document.getElementById('timestamp').textContent = new Date().toLocaleString('en-US', {
    weekday: 'short', month: 'short', day: 'numeric',
    hour: 'numeric', minute: '2-digit', timeZoneName: 'short'
  });

  // ================ Data Engine ================
  // Veteran's Buy Signal and Long-Term Metrics are pre-computed daily by
  // scripts/fetch_data.py on GitHub Actions and stored in data/feed.json.
  // The browser just reads and renders — no Yahoo CORS issues.
  const SYMBOLS = ['MU', 'AVGO', 'PLTR', 'TSLA', 'NVDA'];

  function fmtPct(v) {
    if (v == null || isNaN(v)) return '—';
    const sign = v >= 0 ? '+' : '';
    return sign + Number(v).toFixed(1) + '%';
  }
  function pctClass(v) {
    if (v == null || isNaN(v)) return '';
    return v >= 0 ? 'positive' : 'negative';
  }

  // ---- Veteran panel render: reads publicFeed.stocks[symbol].veteran_signal ----
  function renderVetPanel(symbol) {
    const panel = document.getElementById('vet-panel');
    const lightEl = document.getElementById('vet-light');
    const statusEl = document.getElementById('vet-status-text');
    const summaryEl = document.getElementById('vet-summary');
    const scoreEl = document.getElementById('vet-score-num');
    const checksEl = document.getElementById('vet-checks');
    const symbolEl = document.getElementById('vet-symbol');
    const asofEl = document.getElementById('vet-asof');
    symbolEl.textContent = symbol;

    const sig = publicFeed && publicFeed.stocks && publicFeed.stocks[symbol]
                ? publicFeed.stocks[symbol].veteran_signal : null;

    if (!publicFeed) {
      panel.className = 'vet-panel';
      lightEl.className = 'vet-light gray';
      statusEl.className = 'vet-status-text gray';
      statusEl.textContent = 'LOADING';
      summaryEl.textContent = 'Loading signals from feed…';
      scoreEl.textContent = '—'; asofEl.textContent = ''; checksEl.innerHTML = '';
      return;
    }
    if (publicFeed._error || !sig || sig.error) {
      panel.className = 'vet-panel';
      lightEl.className = 'vet-light gray';
      statusEl.className = 'vet-status-text gray';
      statusEl.textContent = 'DATA UNAVAILABLE';
      const reason = publicFeed._error
        ? 'data/feed.json is missing — run the GitHub Actions workflow at least once to populate it.'
        : 'Signals not in the feed yet — re-run the GitHub Actions workflow to refresh.';
      summaryEl.textContent = reason;
      scoreEl.textContent = '—'; asofEl.textContent = ''; checksEl.innerHTML = '';
      return;
    }

    panel.className = 'vet-panel signal-' + sig.signal;
    lightEl.className = 'vet-light ' + sig.light_class;
    statusEl.className = 'vet-status-text ' + sig.status_class;
    statusEl.textContent = sig.status_text;
    summaryEl.textContent = sig.summary;
    scoreEl.textContent = sig.score;
    asofEl.textContent = ' · as of ' + sig.as_of + ' · $' + sig.last_close.toFixed(2);
    checksEl.innerHTML = sig.checks.map(c => `
      <div class="vet-check ${c.met ? 'met' : ''}">
        <span class="vet-check-icon">${c.met ? '✓' : '✕'}</span>
        <span class="vet-check-label">${c.label}</span>
        <span class="vet-check-source">${c.source}</span>
      </div>`).join('');
  }

  // ---- Long-Term Metrics panel render ----
  function renderLtPanel(symbol) {
    document.getElementById('lt-symbol').textContent = symbol;
    const setText = (id, text, cls) => {
      const el = document.getElementById(id);
      el.textContent = text;
      if (cls != null) el.className = 'lt-stat-value ' + cls;
    };
    const blank = () => {
      setText('lt-price', '—'); setText('lt-ytd', '—');
      setText('lt-cagr1', '—'); setText('lt-cagr3', '—');
      setText('lt-cagr5', '—'); setText('lt-ma200d', '—');
      document.getElementById('lt-asof').textContent = '';
      document.getElementById('lt-range-pos-text').textContent = '—';
      document.getElementById('lt-range-drawdown').textContent = '—';
      document.getElementById('lt-range-low').textContent = '$—';
      document.getElementById('lt-range-high').textContent = '$—';
      document.getElementById('lt-range-marker').style.left = '50%';
      document.getElementById('lt-dca-rating').textContent = '—';
      document.getElementById('lt-dca-rating').className = 'lt-dca-rating';
      Array.from(document.getElementById('lt-dca-dots').children).forEach(d => d.classList.remove('active'));
    };

    const lt = publicFeed && publicFeed.stocks && publicFeed.stocks[symbol]
               ? publicFeed.stocks[symbol].long_term : null;

    if (!publicFeed || !lt || lt.error) {
      blank();
      return;
    }

    setText('lt-price', '$' + Number(lt.last).toFixed(2));
    setText('lt-ytd',   fmtPct(lt.ytd_return), pctClass(lt.ytd_return));
    setText('lt-cagr1', fmtPct(lt.cagr_1y),    pctClass(lt.cagr_1y));
    setText('lt-cagr3', fmtPct(lt.cagr_3y),    pctClass(lt.cagr_3y));
    setText('lt-cagr5', fmtPct(lt.cagr_5y),    pctClass(lt.cagr_5y));
    setText('lt-ma200d', fmtPct(lt.ma200_dist), pctClass(lt.ma200_dist));
    document.getElementById('lt-asof').textContent = 'as of ' + lt.as_of;

    const pos = Math.max(0, Math.min(100, lt.range_pos));
    document.getElementById('lt-range-marker').style.left = pos + '%';
    document.getElementById('lt-range-pos-text').textContent = pos.toFixed(0) + '%';
    document.getElementById('lt-range-drawdown').textContent = fmtPct(lt.drawdown) + ' from 52w high';
    document.getElementById('lt-range-low').textContent  = '$' + Number(lt.low_52w).toFixed(2);
    document.getElementById('lt-range-high').textContent = '$' + Number(lt.high_52w).toFixed(2);

    const ratingEl = document.getElementById('lt-dca-rating');
    ratingEl.textContent = lt.dca_rating;
    ratingEl.className = 'lt-dca-rating';
    ratingEl.style.color = lt.dca_rating_class === 'positive' ? '#3fb950'
                          : lt.dca_rating_class === 'warning' ? '#d29922' : '#f85149';
    Array.from(document.getElementById('lt-dca-dots').children).forEach((d, i) => {
      if (i < lt.dca_score) d.classList.add('active');
      else d.classList.remove('active');
    });
  }

  // ---- Refresh button: re-pulls feed.json (no client-side fetching) ----
  async function refreshAllPanels() {
    await loadPublicFeed();   // re-fetches feed.json with no-cache
    renderVetPanel(activeSymbol);
    renderLtPanel(activeSymbol);
  }

  document.getElementById('vet-refresh').addEventListener('click', refreshAllPanels);

  // ================ Public Record feed ================
  // Loads from ./data/feed.json (built daily by scripts/fetch_data.py via GitHub Actions)
  let publicFeed = null;

  async function loadPublicFeed() {
    try {
      const res = await fetch('./data/feed.json', { cache: 'no-store' });
      if (!res.ok) throw new Error('HTTP ' + res.status);
      publicFeed = await res.json();
    } catch (e) {
      publicFeed = { _error: e.message };
    }
    renderVetPanel(activeSymbol);
    renderLtPanel(activeSymbol);
    renderPrPanel(activeSymbol);
  }

  function fmtMoneyShort(n) {
    if (n == null) return '—';
    const abs = Math.abs(n);
    if (abs >= 1e9) return '$' + (n / 1e9).toFixed(1) + 'B';
    if (abs >= 1e6) return '$' + (n / 1e6).toFixed(1) + 'M';
    if (abs >= 1e3) return '$' + (n / 1e3).toFixed(0) + 'K';
    return '$' + Math.round(n);
  }

  function fmtDate(iso) {
    if (!iso) return '—';
    const d = new Date(iso + 'T00:00:00Z');
    return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
  }

  function daysBetween(iso) {
    if (!iso) return null;
    const target = new Date(iso + 'T00:00:00Z');
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    return Math.round((target - today) / 86400000);
  }

  function renderPrPanel(symbol) {
    const symEl = document.getElementById('pr-symbol');
    const asofEl = document.getElementById('pr-asof');
    const bodyEl = document.getElementById('pr-body');
    symEl.textContent = symbol;

    // No feed loaded yet
    if (!publicFeed) {
      asofEl.textContent = 'Loading…';
      asofEl.className = 'pr-asof';
      bodyEl.innerHTML = '<div class="pr-setup">Loading public record data…</div>';
      return;
    }

    // Feed unavailable — show setup hint
    if (publicFeed._error) {
      asofEl.textContent = 'Feed not configured';
      asofEl.className = 'pr-asof missing';
      bodyEl.innerHTML = `
        <div class="pr-setup">
          The Public Record panel pulls fresh insider transactions, recent SEC filings, and earnings dates daily.<br><br>
          To enable it, set up the feed builder by following the steps in <code>README.md</code> in your repo. The page expects to find <code>./data/feed.json</code> in the same directory.<br><br>
          <span style="color:#6e7681;">Reason: ${publicFeed._error}</span>
        </div>`;
      return;
    }

    // Check freshness
    const updatedDate = new Date(publicFeed.updated_utc);
    const ageHours = (Date.now() - updatedDate.getTime()) / 3600000;
    const ageStr = ageHours < 1 ? '<1h ago'
                  : ageHours < 24 ? Math.round(ageHours) + 'h ago'
                  : Math.round(ageHours / 24) + 'd ago';
    asofEl.textContent = 'Updated ' + ageStr;
    asofEl.className = ageHours > 96 ? 'pr-asof stale' : 'pr-asof';

    const stock = (publicFeed.stocks || {})[symbol];
    if (!stock) {
      bodyEl.innerHTML = '<div class="pr-setup">No data for ' + symbol + ' in the feed.</div>';
      return;
    }

    // Earnings cell
    const earnings = stock.next_earnings;
    const days = daysBetween(earnings);
    let earningsHTML;
    if (earnings && days != null) {
      let daysText, daysCls = '';
      if (days < 0) { daysText = `reported ${-days}d ago`; }
      else if (days === 0) { daysText = 'today'; daysCls = 'negative'; }
      else if (days <= 7) { daysText = `in ${days} days`; daysCls = 'negative'; }
      else if (days <= 30) { daysText = `in ${days} days`; }
      else { daysText = `in ${days} days`; }
      earningsHTML = `
        <div class="pr-cell">
          <div class="pr-cell-label">Next earnings <span class="pr-tag">SEC</span></div>
          <div class="pr-cell-main ${daysCls}">${fmtDate(earnings)}</div>
          <div class="pr-cell-sub">${daysText} · DCA tip: avoid adding 2–3 days before earnings (volatility) and prefer adding 1–2 days after</div>
        </div>`;
    } else {
      earningsHTML = `
        <div class="pr-cell">
          <div class="pr-cell-label">Next earnings <span class="pr-tag">SEC</span></div>
          <div class="pr-cell-main">—</div>
          <div class="pr-cell-sub">Earnings date not currently published</div>
        </div>`;
    }

    // Insider summary cell
    const ins = stock.insider_activity || {};
    const purCount = ins.purchase_count || 0;
    const sellCount = ins.sale_count || 0;
    const purValue = ins.purchase_value || 0;
    const sellValue = ins.sale_value || 0;
    const netCls = purCount > sellCount ? 'positive' : sellCount > purCount ? 'negative' : '';
    const netLabel = purCount > sellCount ? 'Net buying' : sellCount > purCount ? 'Net selling' : 'Quiet';

    const insiderHTML = `
      <div class="pr-cell">
        <div class="pr-cell-label">Insider activity · last 90 days <span class="pr-tag">Form 4</span></div>
        <div class="pr-cell-main ${netCls}">${netLabel}</div>
        <div class="pr-cell-sub">
          <span style="color:#3fb950;">▲ ${purCount} buy${purCount === 1 ? '' : 's'} · ${fmtMoneyShort(purValue)}</span>
          &nbsp;·&nbsp;
          <span style="color:#f85149;">▼ ${sellCount} sale${sellCount === 1 ? '' : 's'} · ${fmtMoneyShort(sellValue)}</span>
          <br>${ins.unique_purchasers || 0} insider${ins.unique_purchasers === 1 ? '' : 's'} buying · open-market only (excludes grants &amp; option exercises)
        </div>
      </div>`;

    // Recent insider purchases list
    const purs = (ins.purchases || []).slice(0, 5);
    let purchasesList = '';
    if (purs.length) {
      purchasesList = purs.map(p => `
        <div class="pr-item">
          <span class="pr-item-date">${fmtDate(p.date)}</span>
          <span class="pr-item-main"><a href="${p.url}" target="_blank">${p.name || 'Insider'} <span style="color:#6e7681;">· ${p.role || ''}</span></a></span>
          <span class="pr-item-meta buy">${fmtMoneyShort(p.value)}</span>
        </div>`).join('');
    } else {
      purchasesList = '<div class="pr-empty">No open-market insider purchases in the last 90 days</div>';
    }

    // Recent material filings
    const filings = (stock.recent_filings || []).slice(0, 5);
    let filingsList = '';
    if (filings.length) {
      filingsList = filings.map(f => `
        <div class="pr-item">
          <span class="pr-item-date">${fmtDate(f.date)}</span>
          <span class="pr-item-main"><a href="${f.url}" target="_blank">${f.type} · ${f.description}</a></span>
          <span class="pr-item-meta">EDGAR</span>
        </div>`).join('');
    } else {
      filingsList = '<div class="pr-empty">No 10-K, 10-Q, or 8-K filings in the last 90 days</div>';
    }

    bodyEl.innerHTML = `
      <div class="pr-row">${earningsHTML}${insiderHTML}</div>
      <div class="pr-list">
        <div class="pr-list-title">
          <span>Recent insider purchases</span>
          <a href="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=${symbol}&type=4&dateb=&owner=include&count=40" target="_blank">View all on EDGAR →</a>
        </div>
        ${purchasesList}
      </div>
      <div class="pr-list">
        <div class="pr-list-title">
          <span>Recent material filings</span>
          <a href="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=${symbol}&type=&dateb=&owner=include&count=40" target="_blank">View all on EDGAR →</a>
        </div>
        ${filingsList}
      </div>`;
  }

  // ================ Daily Wisdom Library ================
  // 30 lessons paraphrased from public-domain investing principles. Rotates by day-of-year.
  const WISDOM = [
    { tag: 'Time vs Timing', title: 'The case against market timing', body: 'Decades of S&P 500 data show that an investor who missed just the 10 best days over a 20-year period saw their total return cut nearly in half. Those best days often cluster during the most volatile periods — exactly when nervous investors capitulate. For most people, the math says: stay invested, don\'t flinch.', attr: 'Based on JPMorgan, Morningstar, and Vanguard studies.' },
    { tag: 'The Lost Decade', title: 'Why DCA earns its keep in bad decades', body: 'From 2000 through 2009, the S&P 500 had essentially zero total return. Lump-sum investors at the 2000 peak sat underwater for a decade. But those who continued buying every month through that period built up shares at a vastly lower average cost — and reaped enormous rewards in the bull market that followed. This is exactly the case for DCA discipline.', attr: 'Based on S&P 500 total return data, 2000–2009.' },
    { tag: 'Compounding', title: 'The Rule of 72', body: 'Want to know how long it takes for money to double? Divide 72 by your annual return rate. At 7% returns, money doubles every ~10.3 years. At 10%, every ~7.2 years. At 4%, every ~18 years. This is why time horizon matters more than most realize — and why every basis point of return compounds dramatically over decades.', attr: 'Classic finance shortcut, dating back to Luca Pacioli (1494).' },
    { tag: 'Costs', title: 'The tyranny of compounding costs', body: 'A 1% annual expense ratio reduces a 30-year portfolio by approximately 25%. The difference between an index fund at 0.05% and an actively managed fund at 1.0% is enormous over decades. The same compounding that grows your money also grows the costs eroding it. Watch fees like a hawk — they\'re the closest thing to a guaranteed return.', attr: 'Principle articulated by John Bogle, founder of Vanguard.' },
    { tag: 'Trend Filter', title: 'The Golden Cross', body: 'When the 50-day moving average crosses above the 200-day moving average, traders call it a Golden Cross — a long-term bullish trend filter dating back to Robert Rhea\'s Dow Theory work. The opposite (Death Cross) signals long-term weakness. Useful as one filter among many, not a complete strategy.', attr: 'Classic technical analysis from Dow Theory.' },
    { tag: 'Retirement Risk', title: 'Sequence of returns risk', body: 'Two retirees with identical average returns can have wildly different outcomes. The one who hits a bear market early in retirement may run out of money; the one who gets the same crash late may not. This is why portfolio composition matters far more as you approach the withdrawal phase of life.', attr: 'Studied extensively by Wade Pfau and others.' },
    { tag: 'Behavioral', title: 'Recency bias', body: 'Humans weight recent events too heavily. After a crash, we expect more crashes; after a rally, we expect more rallies. The hardest mental discipline for long-term investors is recognizing that the future rarely looks like the recent past. Financial markets mean-revert in ways our intuition resists.', attr: 'Behavioral finance research, Tversky & Kahneman.' },
    { tag: 'Behavioral', title: 'Loss aversion', body: 'Behavioral economics consistently shows losses feel approximately twice as painful as equivalent gains feel pleasant. This causes investors to sell winners too quickly and hold losers too long — exactly the opposite of optimal behavior. Knowing this bias exists is the first step to fighting it.', attr: 'Kahneman & Tversky, Prospect Theory (1979).' },
    { tag: 'Asset Allocation', title: 'The biggest decision you\'ll make', body: 'Multiple studies suggest that asset allocation — your mix of stocks, bonds, and cash — explains the vast majority of long-term portfolio variance. Stock-picking matters far less than most assume. Get the big-picture allocation right and the rest is largely details.', attr: 'Brinson, Hood & Beebower (1986); replicated many times since.' },
    { tag: 'Valuation', title: 'The Buffett Indicator', body: 'Total US stock market capitalization divided by GDP. Above 100% has historically suggested overvaluation; below 70% has suggested undervaluation. Currently a useful rough gauge of overall market valuation, though Buffett himself notes it\'s imperfect and changes with interest rate regimes.', attr: 'Popularized by Warren Buffett in a 2001 Fortune article.' },
    { tag: 'Fundamentals', title: 'P/E ratio in context', body: 'Price divided by earnings tells you what investors will pay for $1 of profit. A P/E of 20 means $20 for $1 of earnings. Lower can mean cheaper or troubled. Sector matters: tech P/Es are typically higher than utilities. Compare to history and peers, not absolute thresholds.', attr: 'Standard fundamental analysis.' },
    { tag: 'Fundamentals', title: 'Free cash flow vs earnings', body: 'Earnings can be massaged through accounting decisions — depreciation schedules, revenue recognition, one-time charges. Free cash flow (cash from operations minus capital expenditures) is much harder to manipulate. Buffett famously studies free cash flow more than reported earnings.', attr: 'Buffett\'s methodology, articulated in many shareholder letters.' },
    { tag: 'Diversification', title: 'Why sector mix matters', body: 'Even within stocks, holding different sectors reduces volatility. When tech crashed in 2000–2002, defensive sectors like consumer staples and utilities held up. Mixing growth, value, defensive, and cyclical exposure smooths returns without significantly reducing them long-term.', attr: 'Modern Portfolio Theory; Markowitz (1952).' },
    { tag: 'Diversification', title: 'Mean reversion across decades', body: 'Hot asset classes tend to cool; cold ones tend to revive. US vs international stocks have traded leadership decade by decade. After 15 years of US dominance, international may have its turn — or not. This is why total diversification often beats chasing recent winners.', attr: 'Long-term capital market history.' },
    { tag: 'Retirement', title: 'The 4% rule', body: 'Bengen\'s 1994 study suggested withdrawing 4% of your initial portfolio (adjusted yearly for inflation) had a roughly 95% success rate over 30-year retirements. Not gospel — recent research suggests 3.5% is more conservative — but a useful baseline for retirement planning.', attr: 'William Bengen (1994); subsequently refined by Trinity study.' },
    { tag: 'Tax Strategy', title: 'Account priority order', body: 'General order: capture employer 401(k) match first (free money), then max HSA if eligible (triple tax advantage), then Roth IRA, then more 401(k), then taxable brokerage. The exact order depends on your tax bracket — but free money should always come first.', attr: 'Standard financial planning sequence.' },
    { tag: 'Tax Strategy', title: 'Roth vs Traditional IRA basics', body: 'Roth IRA: pay taxes now, withdraw tax-free in retirement. Traditional IRA: deduct now, pay taxes on withdrawals. Younger workers and those in lower tax brackets often benefit from Roth\'s tax-free growth. Higher earners closer to retirement may favor Traditional. Many people use both.', attr: 'IRS rules; consult a tax professional.' },
    { tag: 'Tax Strategy', title: 'Tax loss harvesting', body: 'Selling investments at a loss to offset capital gains can save thousands in taxes annually. The IRS wash sale rule prohibits buying the substantially identical security within 30 days before or after the sale. Done right, this is one of the highest-ROI activities in personal finance.', attr: 'IRS Section 1091 (wash sale rule).' },
    { tag: 'Income', title: 'Power of dividend reinvestment', body: 'Over the past century, reinvested dividends have provided roughly 40% of the S&P 500\'s total returns. The compounding of reinvested distributions over decades is enormous. Most brokerages offer automatic dividend reinvestment (DRIP) for free — turn it on unless you specifically need the cash.', attr: 'Based on Ibbotson and S&P long-term data.' },
    { tag: 'Value Investing', title: 'Margin of safety', body: 'Benjamin Graham\'s core principle: only buy when the market price is significantly below your estimate of the company\'s intrinsic value. The gap is your buffer against valuation errors and bad luck. Never assume your analysis is perfect — always demand a discount.', attr: 'Benjamin Graham, "The Intelligent Investor" (1949).' },
    { tag: 'Quality', title: 'Economic moats', body: 'Buffett\'s term for sustainable competitive advantages: brand power (Coca-Cola), network effects (Visa), switching costs (Microsoft Office), or genuine cost advantages (GEICO). Durable moats produce durable returns. The wider and deeper, the better.', attr: 'Concept popularized by Warren Buffett.' },
    { tag: 'Behavioral', title: 'Survivorship bias', body: 'Studying only successful companies and investors tells you almost nothing useful. The graveyard of failed strategies contains the actual lessons. This is why "what successful investors did" can mislead — for every Buffett, there were thousands who applied similar methods and went bust.', attr: 'Statistical bias; widely studied.' },
    { tag: 'Risk', title: 'Volatility ≠ risk', body: 'For long-term investors, short-term price swings aren\'t risk — they\'re noise. Permanent capital impairment (companies going bankrupt, frauds, terminal decline) is the actual risk. The two get conflated constantly, leading investors to flee perfectly fine investments during temporary drawdowns.', attr: 'Articulated by Buffett, Howard Marks, and others.' },
    { tag: 'Risk', title: 'Beta basics', body: 'Beta measures a stock\'s volatility relative to the market. Beta of 1.0 = moves with the market. Beta of 1.5 = swings 50% more. Beta of 0.5 = half as much. High-beta stocks deliver more pain in downturns and more glory in rallies — useful to know what you\'re holding.', attr: 'Capital Asset Pricing Model (CAPM).' },
    { tag: 'Index Investing', title: 'The active management problem', body: 'SPIVA reports consistently show that over 15–20 year periods, roughly 85–90% of actively managed US large-cap funds underperform their benchmark index after fees. This is the empirical case for low-cost index investing. Stock-picking is hard; consistently beating the index over decades is harder still.', attr: 'S&P SPIVA reports, published semi-annually.' },
    { tag: 'Crisis', title: 'The 2008 lesson', body: 'The S&P 500 fell ~57% peak to trough by March 2009. Anyone who panic-sold near the lows missed the subsequent decade-long bull market that delivered nearly 600% gains. Those who continued DCA-ing through the crisis fared even better. Discipline beat panic, dramatically.', attr: 'S&P 500 historical data, 2007–2019.' },
    { tag: 'Earnings', title: 'Earnings season patterns', body: 'Companies report results within ~6 weeks of quarter-end. Stocks often move more on forward guidance than on the actual quarter\'s numbers — markets price the future, not the past. A quarter that "beats" can still send shares lower if guidance disappoints.', attr: 'Standard observation across earnings cycles.' },
    { tag: 'Insiders', title: 'Insider buying signals', body: 'When executives buy their own company\'s stock with personal money (filed publicly via SEC Form 4), it\'s historically been a moderately bullish signal. They have inside knowledge, and putting personal money behind it carries weight. Insider selling is murkier — many sell for tax or diversification reasons.', attr: 'Based on academic studies; Lakonishok & Lee (2001).' },
    { tag: 'Capital Allocation', title: 'Share buybacks', body: 'When companies repurchase their own shares, share count drops and per-share earnings rise. Buybacks help shareholders most when done at undervalued prices — and unfortunately, companies often buy back when share prices are highest. Watch when, not just whether.', attr: 'Buffett has written extensively on this; see Berkshire letters.' },
    { tag: 'Risk Management', title: 'Position sizing rule of thumb', body: 'A widely-used principle: no single position should be so large that a 50% drop would devastate your portfolio. Common rules include: max 5–10% in any single stock for diversified investors. The most painful losses come from concentration in stories that turned out wrong.', attr: 'Risk management heuristic, widely taught.' }
  ];

  function renderDailyWisdom() {
    const today = new Date();
    const start = new Date(today.getFullYear(), 0, 0);
    const dayOfYear = Math.floor((today - start) / 86400000);
    const idx = dayOfYear % WISDOM.length;
    const w = WISDOM[idx];
    document.getElementById('wisdom-tag').textContent = `Daily Wisdom · ${w.tag}`;
    document.getElementById('wisdom-title').textContent = w.title;
    document.getElementById('wisdom-body').textContent = w.body;
    document.getElementById('wisdom-attr').textContent = w.attr;
  }
  renderDailyWisdom();

  // ================ DCA Calculator ================
  function fmtMoney(n) {
    return '$' + n.toLocaleString('en-US', { maximumFractionDigits: 0 });
  }
  function updateDcaCalc() {
    const amount = parseFloat(document.getElementById('dca-amount').value);
    const years = parseInt(document.getElementById('dca-years').value);
    const ret = parseFloat(document.getElementById('dca-return').value);

    document.getElementById('dca-amount-out').textContent = fmtMoney(amount);
    document.getElementById('dca-years-out').textContent = years + (years === 1 ? ' year' : ' years');
    document.getElementById('dca-return-out').textContent = ret.toFixed(1) + '%';

    // Future value of annuity formula: FV = PMT * (((1+r)^n - 1) / r)
    const monthlyRate = (ret / 100) / 12;
    const months = years * 12;
    const fv = monthlyRate === 0
      ? amount * months
      : amount * (Math.pow(1 + monthlyRate, months) - 1) / monthlyRate;
    const invested = amount * months;
    const growth = fv - invested;

    document.getElementById('dca-invested').textContent = fmtMoney(invested);
    document.getElementById('dca-growth').textContent = fmtMoney(growth);
    document.getElementById('dca-final').textContent = fmtMoney(fv);
  }
  ['dca-amount', 'dca-years', 'dca-return'].forEach(id =>
    document.getElementById(id).addEventListener('input', updateDcaCalc)
  );
  updateDcaCalc();

  // Kick off data load
  loadPublicFeed().then(() => {
    renderVetPanel(activeSymbol);
    renderLtPanel(activeSymbol);
  });
</script>

</body>
</html>
