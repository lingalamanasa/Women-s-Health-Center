# apply_three_color_theme.py
# Applies the strict 3-color palette: Ivory, Lavender, and Deep Purple across the entire website.

import re
import os

IVORY = "#FFFFF0"
IVORY_SOFT = "#FAF9F5"
IVORY_CARD = "#FFFFFF"
IVORY_BORDER = "#EDE8DF"

LAVENDER = "#967BB6"
LAVENDER_VIBRANT = "#8B5CF6"
LAVENDER_LIGHT = "#F3E8FF"
LAVENDER_PASTEL = "#E6E6FA"
LAVENDER_BORDER = "#DDD6FE"
LAVENDER_MUTED = "#BDB0D0"

DEEP_PURPLE = "#3B0764"
DEEP_PURPLE_DARK = "#24063E"
DEEP_PURPLE_NIGHT = "#19042B"
DEEP_PURPLE_MID = "#581C87"
DEEP_PURPLE_TEXT = "#1E0533"

# 1. UPDATE style.css
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace Root Variables
root_replacement = f"""/* Strict 3-Color Luxury Medical Palette: Ivory, Lavender, Deep Purple */
  --primary-plum: {DEEP_PURPLE};        /* Deep Purple */
  --primary-plum-hover: {DEEP_PURPLE_DARK};  /* Darker Deep Purple */
  --plum-light: {LAVENDER_LIGHT};          /* Soft Lavender tint */
  --plum-border: {LAVENDER_BORDER};         /* Lavender border */

  --accent-gold: {LAVENDER};         /* Lavender accent */
  --accent-gold-hover: {LAVENDER_VIBRANT};   /* Vibrant Lavender hover */
  --accent-rose: {LAVENDER};         /* Lavender */
  --accent-peach: {IVORY_SOFT};        /* Warm Ivory */
  --accent-blush: {LAVENDER_LIGHT};        /* Soft Lavender */
  --accent-lavender: {LAVENDER_PASTEL};     /* Pure Pastel Lavender */
  --accent-sage: {IVORY};         /* Pure Ivory */

  --text-primary: {DEEP_PURPLE_TEXT};        /* Deep Purple main text */
  --text-muted: #5B446E;          /* Lavender-Purple muted text */
  --text-light: #8C75A1;          /* Soft Lavender text */
  --text-white: {IVORY};          /* Ivory text on dark surfaces */

  --bg-page: {IVORY_SOFT};             /* Ivory page background */
  --bg-card: {IVORY_CARD};             /* Ivory card background */

  --font-sans: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-mono: 'Fira Mono', 'SF Mono', Monaco, monospace;

  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 20px;
  --radius-xl: 28px;
  --radius-pill: 9999px;

  --shadow-sm: 0 2px 6px rgba(59, 7, 100, 0.04);
  --shadow-md: 0 8px 24px rgba(59, 7, 100, 0.08);
  --shadow-lg: 0 16px 40px rgba(59, 7, 100, 0.12);
  --shadow-glow: 0 6px 20px rgba(150, 123, 182, 0.35);
  --transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);"""

css = re.sub(r'/\* Mithila Women\'s Hospital Refined Color Palette \*/.*?--transition: all 0\.3s cubic-bezier\(0\.16, 1, 0\.3, 1\);', root_replacement, css, flags=re.DOTALL)

# Replace specific non-palette hexes in style.css:
# Golds/Ambers -> Lavender or Deep Purple
css = css.replace('#f59e0b', LAVENDER)
css = css.replace('#d97706', DEEP_PURPLE)
css = css.replace('#b45309', DEEP_PURPLE)
css = css.replace('#fbbf24', LAVENDER_PASTEL)
css = css.replace('#fcd34d', LAVENDER_PASTEL)
css = css.replace('#fde68a', LAVENDER_BORDER)
css = css.replace('#fef3c7', LAVENDER_LIGHT)
css = css.replace('#fffbeb', LAVENDER_LIGHT)
css = css.replace('#854d0e', DEEP_PURPLE)
css = css.replace('#92400e', DEEP_PURPLE)

# Greens/Blues -> Lavender or Deep Purple
css = css.replace('#10b981', LAVENDER)
css = css.replace('#22c55e', LAVENDER)
css = css.replace('#166534', DEEP_PURPLE)
css = css.replace('#15803d', DEEP_PURPLE)
css = css.replace('#f0fdf4', LAVENDER_LIGHT)
css = css.replace('#bbf7d0', LAVENDER_BORDER)
css = css.replace('#dcfce7', LAVENDER_LIGHT)

css = css.replace('#eff6ff', LAVENDER_LIGHT)
css = css.replace('#bfdbfe', LAVENDER_BORDER)
css = css.replace('#1e40af', DEEP_PURPLE)
css = css.replace('#3b82f6', LAVENDER)

# Slate / Dark Blues / Plums -> Deep Purple / Ivory
css = css.replace('#0f172a', DEEP_PURPLE_NIGHT)
css = css.replace('#1e293b', DEEP_PURPLE_DARK)
css = css.replace('#0e0f12', DEEP_PURPLE_NIGHT)
css = css.replace('#111827', DEEP_PURPLE_TEXT)
css = css.replace('#1f2937', DEEP_PURPLE_TEXT)
css = css.replace('#374151', DEEP_PURPLE_TEXT)
css = css.replace('#3d2733', DEEP_PURPLE)
css = css.replace('#291822', DEEP_PURPLE_DARK)
css = css.replace('#831843', DEEP_PURPLE)
css = css.replace('#fbcfe8', LAVENDER_BORDER)
css = css.replace('#fdf2f8', LAVENDER_LIGHT)

# Backgrounds to Ivory
css = css.replace('#f8fafc', IVORY_SOFT)
css = css.replace('#f1f5f9', IVORY_BORDER)
css = css.replace('#e2e8f0', LAVENDER_BORDER)
css = css.replace('#cbd5e1', LAVENDER_MUTED)

# Preloader colors in style.css
css = css.replace('linear-gradient(135deg, #170b14 0%, #291223 50%, #120810 100%)', f'linear-gradient(135deg, {DEEP_PURPLE_NIGHT} 0%, {DEEP_PURPLE_DARK} 50%, {DEEP_PURPLE_NIGHT} 100%)')
css = css.replace('rgba(245, 158, 11, 0.16)', 'rgba(150, 123, 182, 0.25)')
css = css.replace('rgba(61, 39, 51, 0.25)', 'rgba(59, 7, 100, 0.35)')

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated assets/css/style.css to Ivory, Lavender, and Deep Purple.")

# 2. UPDATE generate_all_dashboards.py
with open('generate_all_dashboards.py', 'r', encoding='utf-8') as f:
    dash_code = f.read()

# Update sidebars, headers, badges in generate_all_dashboards.py
dash_code = dash_code.replace("linear-gradient(180deg, #d97706 0%, #b45309 100%)", f"linear-gradient(180deg, {DEEP_PURPLE} 0%, {DEEP_PURPLE_DARK} 100%)")
dash_code = dash_code.replace("linear-gradient(180deg, #1e293b 0%, #0f172a 100%)", f"linear-gradient(180deg, {DEEP_PURPLE_NIGHT} 0%, #10021a 100%)")
dash_code = dash_code.replace("#f59e0b", LAVENDER)
dash_code = dash_code.replace("#b45309", DEEP_PURPLE)
dash_code = dash_code.replace("#1e293b", DEEP_PURPLE_DARK)
dash_code = dash_code.replace("#0f172a", DEEP_PURPLE_NIGHT)
dash_code = dash_code.replace("#fef3c7", LAVENDER_LIGHT)
dash_code = dash_code.replace("#f8fafc", IVORY_SOFT)

with open('generate_all_dashboards.py', 'w', encoding='utf-8') as f:
    f.write(dash_code)
print("Updated generate_all_dashboards.py.")

# 3. UPDATE build_all_content.py, build_user_pages.py, build_admin_pages.py
for script_file in ['build_all_content.py', 'build_user_pages.py', 'build_admin_pages.py']:
    with open(script_file, 'r', encoding='utf-8') as f:
        code = f.read()
    code = code.replace("#f59e0b", LAVENDER)
    code = code.replace("#d97706", DEEP_PURPLE)
    code = code.replace("#b45309", DEEP_PURPLE)
    code = code.replace("#10b981", LAVENDER)
    code = code.replace("#22c55e", LAVENDER)
    code = code.replace("#ef4444", DEEP_PURPLE)
    code = code.replace("#0f172a", DEEP_PURPLE_TEXT)
    code = code.replace("#1e293b", DEEP_PURPLE_DARK)
    code = code.replace("#f8fafc", IVORY_SOFT)
    code = code.replace("#f1f5f9", LAVENDER_LIGHT)
    code = code.replace("#e2e8f0", LAVENDER_BORDER)
    code = code.replace("#3b82f6", LAVENDER)
    code = code.replace("#6366f1", LAVENDER)
    code = code.replace("#ec4899", LAVENDER)
    code = code.replace("#8b5cf6", LAVENDER)
    with open(script_file, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"Updated {script_file}.")

# 4. REGENERATE ALL 14 DASHBOARD PAGES
import build_all_content
import build_user_pages
import build_admin_pages
import importlib
importlib.reload(build_all_content)
importlib.reload(build_user_pages)
importlib.reload(build_admin_pages)

pages = {
    'dashboard-user.html': build_all_content.create_user_home(),
    'user-vitals.html': build_user_pages.create_user_vitals(),
    'user-consultations.html': build_user_pages.create_user_consultations(),
    'user-scans.html': build_user_pages.create_user_scans(),
    'user-maternity.html': build_user_pages.create_user_maternity(),
    'user-prescriptions.html': build_user_pages.create_user_prescriptions(),
    'user-billing.html': build_user_pages.create_user_billing(),

    'dashboard-admin.html': build_admin_pages.create_admin_home(),
    'admin-queue.html': build_admin_pages.create_admin_queue(),
    'admin-surgery.html': build_admin_pages.create_admin_surgery(),
    'admin-admissions.html': build_admin_pages.create_admin_admissions(),
    'admin-nicu.html': build_admin_pages.create_admin_nicu(),
    'admin-lab.html': build_admin_pages.create_admin_lab(),
    'admin-billing.html': build_admin_pages.create_admin_billing(),
}

for name, html in pages.items():
    with open(name, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Re-generated {name} with Ivory, Lavender, Deep Purple palette.")

# 5. UPDATE add_preloaders.py AND RE-RUN
with open('add_preloaders.py', 'r', encoding='utf-8') as f:
    preload_code = f.read()

preload_code = preload_code.replace("linear-gradient(135deg, #170b14 0%, #291223 50%, #120810 100%)", f"linear-gradient(135deg, {DEEP_PURPLE_NIGHT} 0%, {DEEP_PURPLE_DARK} 50%, {DEEP_PURPLE_NIGHT} 100%)")
preload_code = preload_code.replace("rgba(245, 158, 11, 0.18)", "rgba(150, 123, 182, 0.25)")
preload_code = preload_code.replace("rgba(61, 39, 51, 0.3)", "rgba(59, 7, 100, 0.4)")
preload_code = preload_code.replace("#f59e0b", LAVENDER)
preload_code = preload_code.replace("#fbbf24", LAVENDER_PASTEL)
preload_code = preload_code.replace("rgba(245, 158, 11, 0.45)", "rgba(150, 123, 182, 0.5)")
preload_code = preload_code.replace("rgba(245, 158, 11, 0.25)", "rgba(59, 7, 100, 0.35)")
preload_code = preload_code.replace("rgba(245, 158, 11, 0.15)", "rgba(150, 123, 182, 0.2)")
preload_code = preload_code.replace("linear-gradient(90deg, #f59e0b, #fbbf24, #f59e0b)", f"linear-gradient(90deg, {LAVENDER}, {LAVENDER_PASTEL}, {LAVENDER})")
preload_code = preload_code.replace("rgba(245, 158, 11, 0.8)", "rgba(150, 123, 182, 0.85)")
preload_code = preload_code.replace("#ffffff", IVORY)

with open('add_preloaders.py', 'w', encoding='utf-8') as f:
    f.write(preload_code)

import subprocess
subprocess.run(['python', 'add_preloaders.py'], check=True)
print("Re-applied preloaders with Ivory, Lavender, Deep Purple palette.")

# 6. UPDATE PUBLIC PAGES AND AUTH PAGES
public_files = ['index.html', 'about.html', 'services.html', 'blog.html', 'contact.html', 'login.html', 'signup.html']
for pfile in public_files:
    if not os.path.exists(pfile):
        continue
    with open(pfile, 'r', encoding='utf-8') as f:
        phtml = f.read()

    phtml = phtml.replace('#f59e0b', LAVENDER)
    phtml = phtml.replace('#d97706', DEEP_PURPLE)
    phtml = phtml.replace('#b45309', DEEP_PURPLE)
    phtml = phtml.replace('#fbbf24', LAVENDER_PASTEL)
    phtml = phtml.replace('#fffbeb', LAVENDER_LIGHT)
    phtml = phtml.replace('#fef3c7', LAVENDER_LIGHT)
    phtml = phtml.replace('#0f172a', DEEP_PURPLE_NIGHT)
    phtml = phtml.replace('#1e293b', DEEP_PURPLE_DARK)
    phtml = phtml.replace('#3d2733', DEEP_PURPLE)
    phtml = phtml.replace('#291822', DEEP_PURPLE_DARK)
    phtml = phtml.replace('#f8fafc', IVORY_SOFT)

    with open(pfile, 'w', encoding='utf-8') as f:
        f.write(phtml)
    print(f"Updated {pfile} inline colors.")

print("All files updated to strict Ivory, Lavender, and Deep Purple palette!")
