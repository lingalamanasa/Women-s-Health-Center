# add_preloaders.py
import re

preloaders = {
    'index.html': ('STACKLY', "WOMEN'S HEALTH CENTER", 'Initializing Care Experience...'),
    'about.html': ('STACKLY', 'STACKLY ABOUT', 'Loading Doctors & Facilities...'),
    'services.html': ('STACKLY', 'STACKLY SERVICES', 'Loading Maternity & Surgical Suites...'),
    'blog.html': ('STACKLY', 'STACKLY BLOG', 'Loading Clinical Articles & Guides...'),
    'contact.html': ('STACKLY', 'STACKLY CONTACT', 'Connecting 24×7 Emergency Desk...')
}

CRITICAL_CSS = '''  <style id="stacklyPreloaderStyles">
    /* Critical Preloader Styles (Instant Render & Zero FOUC) */
    body.preloader-active { overflow: hidden !important; }
    .stackly-preloader {
      position: fixed;
      top: 0; left: 0;
      width: 100vw; height: 100vh;
      z-index: 999999;
      display: flex; align-items: center; justify-content: center;
      background: linear-gradient(135deg, #19042B 0%, #24063E 50%, #19042B 100%);
      opacity: 1; visibility: visible;
      transition: opacity 0.45s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.45s;
    }
    .stackly-preloader.loaded {
      opacity: 0; visibility: hidden; pointer-events: none;
    }
    .preloader-backdrop {
      position: absolute; top: 0; left: 0; width: 100%; height: 100%;
      background: radial-gradient(circle at center, rgba(150, 123, 182, 0.25) 0%, rgba(59, 7, 100, 0.4) 45%, transparent 75%);
      pointer-events: none;
    }
    .preloader-content {
      position: relative; z-index: 2;
      display: flex; flex-direction: column; align-items: center; text-align: center;
      padding: 32px 40px; max-width: 440px; width: 90%;
    }
    .preloader-logo-ring {
      position: relative; width: 100px; height: 100px;
      display: flex; align-items: center; justify-content: center;
      margin-bottom: 20px;
    }
    .preloader-orbit-spinner {
      position: absolute; top: -6px; left: -6px;
      width: calc(100% + 12px); height: calc(100% + 12px);
      border-radius: 50%;
      border: 2px solid transparent;
      border-top-color: #967BB6; border-right-color: #E6E6FA;
      animation: preloaderSpin 1.4s cubic-bezier(0.68, -0.55, 0.27, 1.55) infinite;
    }
    .preloader-orbit-spinner-2 {
      position: absolute; top: -16px; left: -16px;
      width: calc(100% + 32px); height: calc(100% + 32px);
      border-radius: 50%;
      border: 1.5px dashed rgba(245, 158, 11, 0.35);
      animation: preloaderSpinRev 3.2s linear infinite;
    }
    .preloader-icon-container {
      width: 76px; height: 76px; border-radius: 22px;
      background: rgba(255, 255, 255, 0.08);
      border: 1.5px solid rgba(150, 123, 182, 0.5);
      backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
      box-shadow: 0 8px 32px rgba(59, 7, 100, 0.35), inset 0 0 16px rgba(245, 158, 11, 0.1);
      display: flex; align-items: center; justify-content: center;
      position: relative; z-index: 2;
    }
    .preloader-logo-img {
      width: 42px !important; height: auto !important; max-width: 42px !important;
      animation: preloaderPulse 2.2s ease-in-out infinite;
      filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.4));
      display: block !important; margin: 0 auto !important;
    }
    .preloader-text-group {
      display: flex; flex-direction: column; align-items: center; margin-top: 6px;
    }
    .preloader-brand-title {
      font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
      font-size: 28px; font-weight: 900; letter-spacing: 3px;
      color: #FFFFF0; text-shadow: 0 4px 16px rgba(0, 0, 0, 0.6);
      line-height: 1.1; margin: 0;
    }
    .preloader-badge-tag {
      display: inline-flex; align-items: center; gap: 6px;
      margin-top: 10px; padding: 5px 16px; border-radius: 9999px;
      font-size: 11.5px; font-weight: 800; letter-spacing: 1.4px;
      text-transform: uppercase;
      background: rgba(150, 123, 182, 0.2); color: #E6E6FA;
      border: 1px solid rgba(245, 158, 11, 0.4);
      box-shadow: 0 0 16px rgba(150, 123, 182, 0.2);
      font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
    }
    .preloader-progress-container {
      width: 240px; height: 5px;
      background: rgba(255, 255, 255, 0.12);
      border-radius: 9999px;
      margin: 22px auto 12px auto;
      overflow: hidden; position: relative;
      border: 1px solid rgba(255, 255, 255, 0.08);
    }
    .preloader-progress-bar {
      height: 100%; width: 15%;
      background: linear-gradient(90deg, #967BB6, #E6E6FA, #967BB6);
      border-radius: 9999px;
      transition: width 0.35s ease-out;
      box-shadow: 0 0 12px rgba(150, 123, 182, 0.85);
    }
    .preloader-status-text {
      font-size: 12.5px; color: rgba(255, 255, 255, 0.75);
      letter-spacing: 0.6px; font-weight: 600; min-height: 20px;
      display: flex; align-items: center; justify-content: center; gap: 6px;
      font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
    }
    @keyframes preloaderSpin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
    @keyframes preloaderSpinRev {
      0% { transform: rotate(360deg); }
      100% { transform: rotate(-360deg); }
    }
    @keyframes preloaderPulse {
      0%, 100% { transform: scale(1); filter: drop-shadow(0 0 6px rgba(245, 158, 11, 0.4)); }
      50% { transform: scale(1.08); filter: drop-shadow(0 0 16px rgba(245, 158, 11, 0.85)); }
    }
  </style>'''

def make_preloader_html(title, tag, status):
    return f'''  <!-- STACKLY PRELOADER ANIMATION -->
  <div id="stacklyPreloader" class="stackly-preloader" aria-hidden="true">
    <div class="preloader-backdrop"></div>
    <div class="preloader-content">
      <div class="preloader-logo-ring">
        <div class="preloader-orbit-spinner"></div>
        <div class="preloader-orbit-spinner-2"></div>
        <div class="preloader-icon-container">
          <img src="assets/img/stackly-icon.webp" alt="Stackly" class="preloader-logo-img">
        </div>
      </div>
      <div class="preloader-text-group">
        <div class="preloader-brand-title">{title}</div>
        <div class="preloader-badge-tag">{tag}</div>
      </div>
      <div class="preloader-progress-container">
        <div class="preloader-progress-bar" id="preloaderProgressBar"></div>
      </div>
      <div class="preloader-status-text" id="preloaderStatusText">{status}</div>
    </div>
  </div>'''

for filename, (title, tag, status) in preloaders.items():
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clean old preloader styles if any
    content = re.sub(r'<style id="stacklyPreloaderStyles">.*?</style>', '', content, flags=re.DOTALL)
    # Clean old preloader html if any
    content = re.sub(r'<!-- STACKLY PRELOADER ANIMATION -->\s*<div id="stacklyPreloader".*?</div>\s*</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)

    # Insert critical CSS before </head>
    content = content.replace('</head>', CRITICAL_CSS + '\n</head>', 1)
    
    # Insert preloader html after <body>
    preloader_html = make_preloader_html(title, tag, status)
    content = content.replace('<body>', '<body>\n\n' + preloader_html, 1)

    # Add cache buster to style.css
    content = re.sub(r'href="assets/css/style\.css(\?v=\d+)?"', 'href="assets/css/style.css?v=7"', content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Enhanced {filename} with critical preloader CSS & markup [{tag}]')

print('All 5 pages successfully updated.')
