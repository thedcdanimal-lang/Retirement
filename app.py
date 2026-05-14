import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Advanced Quantitative Retirement Planner – Moved",
    page_icon="🏦",
    layout="centered",
)

# Hide default Streamlit chrome so the dark background is seamless
st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background: #0d1b2a !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    [data-testid="stHeader"],
    [data-testid="stToolbar"],
    [data-testid="stStatusWidget"],
    footer { display: none !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

NEW_URL = "https://nesteggexpress-fed-retire-sim.hf.space"

# Use components.html() — renders a real iframe so CSS/HTML is never sanitized
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Source+Sans+3:wght@400;600&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

  body {{
    background: #0d1b2a;
    font-family: 'Source Sans 3', sans-serif;
    color: #e8dcc8;
    min-height: 100vh;
    display: flex;
    align-items: flex-start;
    justify-content: center;
    padding: 2.5rem 1.5rem 4rem;
  }}

  /* ---------- card ---------- */
  .alert-card {{
    background: linear-gradient(135deg, #112233 0%, #0d1b2a 60%, #0a2540 100%);
    border: 1px solid rgba(200, 160, 80, 0.35);
    border-radius: 16px;
    padding: 3rem 3.5rem 2.8rem;
    max-width: 720px;
    width: 100%;
    box-shadow:
      0 0 0 1px rgba(200,160,80,0.08),
      0 32px 80px rgba(0,0,0,0.55),
      inset 0 1px 0 rgba(255,255,255,0.05);
    position: relative;
    overflow: hidden;
    animation: fadeUp 0.7s ease both;
  }}

  .alert-card::before {{
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 220px; height: 220px;
    background: radial-gradient(circle, rgba(200,160,80,0.12) 0%, transparent 70%);
    pointer-events: none;
  }}

  /* ---------- badge ---------- */
  .badge {{
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    background: rgba(200, 160, 80, 0.12);
    border: 1px solid rgba(200, 160, 80, 0.4);
    border-radius: 999px;
    padding: 0.3rem 1rem;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #c8a050;
    margin-bottom: 1.6rem;
  }}
  .badge-dot {{
    width: 7px; height: 7px;
    border-radius: 50%;
    background: #c8a050;
    animation: pulse 1.8s ease-in-out infinite;
  }}

  /* ---------- headline ---------- */
  .headline {{
    font-family: 'Playfair Display', serif;
    font-size: 2.1rem;
    line-height: 1.2;
    color: #f0e4c8;
    margin: 0 0 0.7rem;
    letter-spacing: -0.01em;
  }}
  .headline span {{ color: #c8a050; }}

  /* ---------- body text ---------- */
  .body-text {{
    font-size: 1.05rem;
    line-height: 1.7;
    color: #b0a898;
    margin-bottom: 2.2rem;
  }}

  /* ---------- URL box ---------- */
  .url-box {{
    background: rgba(0, 0, 0, 0.3);
    border: 1px solid rgba(200, 160, 80, 0.25);
    border-left: 3px solid #c8a050;
    border-radius: 8px;
    padding: 0.9rem 1.2rem;
    font-family: 'Courier New', monospace;
    font-size: 0.95rem;
    color: #c8a050;
    word-break: break-all;
    margin-bottom: 2rem;
    letter-spacing: 0.02em;
  }}

  /* ---------- CTA button ---------- */
  .cta-wrap {{ text-align: center; margin-bottom: 2rem; }}
  .cta-btn {{
    display: inline-block;
    background: linear-gradient(135deg, #c8a050 0%, #a07830 100%);
    color: #0d1b2a;
    font-family: 'Source Sans 3', sans-serif;
    font-weight: 700;
    font-size: 1.05rem;
    letter-spacing: 0.04em;
    text-decoration: none;
    padding: 0.85rem 2.6rem;
    border-radius: 8px;
    transition: filter 0.2s, transform 0.15s, box-shadow 0.2s;
    box-shadow: 0 4px 24px rgba(200,160,80,0.25);
  }}
  .cta-btn:hover {{
    filter: brightness(1.12);
    transform: translateY(-2px);
    box-shadow: 0 8px 32px rgba(200,160,80,0.38);
    color: #0d1b2a;
  }}

  /* ---------- divider ---------- */
  .divider {{
    border: none;
    border-top: 1px solid rgba(200,160,80,0.15);
    margin: 1.5rem 0 1.4rem;
  }}

  /* ---------- footer note ---------- */
  .footer-note {{
    font-size: 0.85rem;
    color: #6a6055;
    text-align: center;
    line-height: 1.5;
  }}
  .footer-note a {{
    color: #8a7850;
    text-decoration: none;
  }}
  .footer-note a:hover {{ color: #c8a050; text-decoration: underline; }}

  /* ---------- animations ---------- */
  @keyframes fadeUp {{
    from {{ opacity: 0; transform: translateY(24px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
  }}
  @keyframes pulse {{
    0%, 100% {{ opacity: 1;   transform: scale(1); }}
    50%       {{ opacity: 0.5; transform: scale(0.75); }}
  }}

  @media (max-width: 600px) {{
    .alert-card {{ padding: 2rem 1.5rem; }}
    .headline {{ font-size: 1.6rem; }}
  }}
</style>
</head>
<body>
  <div class="alert-card">

    <div class="badge">
      <div class="badge-dot"></div>
      Important Update
    </div>

    <h1 class="headline">
      The <span>Advanced Quantitative<br>Retirement Planner</span><br>
      has a new home.
    </h1>

    <p class="body-text">
      We've significantly improved the planner and moved it to a faster,
      more reliable server. Please update any bookmarks and share the new
      address with your colleagues.
    </p>

    <div class="url-box">&#128279;&nbsp;&nbsp;{NEW_URL}</div>

    <div class="cta-wrap">
      <a class="cta-btn" href="{NEW_URL}" target="_blank" rel="noopener noreferrer">
        Open the New Planner &rarr;
      </a>
    </div>

    <hr class="divider">

    <p class="footer-note">
      This page will remain up temporarily to redirect returning users.<br>
      Please visit
      <a href="{NEW_URL}" target="_blank">{NEW_URL}</a>
      going forward.
    </p>

  </div>
</body>
</html>
"""

components.html(html_content, height=560, scrolling=False)