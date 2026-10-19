# generate_all_dashboards.py
# Generates all 14 dashboard pages (7 User + 7 Admin) with 5 distinct UI/UX sections each
# Specifically tailored for Women's Health Center

import os

USER_MENU = [
    ("dashboard-user.html", "🏠", "My Health Dashboard"),
    ("user-vitals.html", "💓", "Telemetry & Vitals"),
    ("user-consultations.html", "📅", "Consultations & OPD"),
    ("user-scans.html", "📡", "4D Scans & Lab Reports"),
    ("user-maternity.html", "🤰", "Maternity Journey"),
    ("user-prescriptions.html", "💊", "Digital Prescriptions"),
    ("user-billing.html", "💳", "Insurance & Billing"),
    ("index.html", "🌐", "Hospital Public Site")
]

ADMIN_MENU = [
    ("dashboard-admin.html", "📊", "Executive Overview"),
    ("admin-queue.html", "🎫", "OPD Token Queue"),
    ("admin-surgery.html", "🔬", "OT & Surgery Roster"),
    ("admin-admissions.html", "🏥", "Bed Occupancy & Wards"),
    ("admin-nicu.html", "🍼", "Level-3 NICU Telemetry"),
    ("admin-lab.html", "🧪", "Diagnostic Laboratory"),
    ("admin-billing.html", "💳", "Revenue & TPA Claims"),
    ("index.html", "🌐", "Hospital Public Site")
]

def render_sidebar(active_file, is_admin):
    menu = ADMIN_MENU if is_admin else USER_MENU
    theme_cls = " admin-theme" if is_admin else ""
    subtitle = "HOSPITAL ADMIN COCKPIT" if is_admin else "CARE CLOUD PORTAL"
    subtitle_style = ' style="color:#967BB6;"' if is_admin else ''
    
    items = []
    for href, icon, title in menu:
        active_cls = " active" if href == active_file else ""
        items.append(f'        <li><a href="{href}" class="{active_cls}"><span>{icon}</span> <span>{title}</span></a></li>')
    menu_html = "\n".join(items)
    
    if is_admin:
        footer_badge = '''        <div class="user-profile-badge" style="background:#19042B;">
          <div class="user-profile-info">
            <div class="user-avatar-circle" style="background:#967BB6;color:#111;">DS</div>
            <div class="user-profile-text">
              <div class="user-profile-name">Dr. Shilpi Singh</div>
              <div class="user-profile-role">Chief Clinical Director</div>
            </div>
          </div>
          <button onclick="logoutUser()" class="btn-sidebar-logout">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4M16 17l5-5-5-5M21 12H9"/></svg>
            <span>LOGOUT ADMIN</span>
          </button>
        </div>'''
    else:
        footer_badge = '''        <div class="user-profile-badge">
          <div class="user-profile-info">
            <div class="user-avatar-circle">LM</div>
            <div class="user-profile-text">
              <div class="user-profile-name">Lingalamanasa123</div>
              <div class="user-profile-role">lingalamanasa123@gmail..</div>
            </div>
          </div>
          <button onclick="logoutUser()" class="btn-sidebar-logout">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4M16 17l5-5-5-5M21 12H9"/></svg>
            <span>LOGOUT</span>
          </button>
        </div>'''

    return f'''    <aside class="dash-sidebar{theme_cls}" id="dashSidebar">
      <div class="sidebar-header">
        <div style="display:flex;align-items:center;justify-content:space-between;">
          <a href="index.html" class="brand-logo">
            <img src="assets/img/stackly-icon.webp" alt="Stackly" class="logo-s-mark" style="height:32px;width:auto;">
            <span class="sidebar-brand-name">STACKLY</span>
          </a>
          <button id="closeDashSidebar" style="display:none;background:none;border:none;color:#fff;font-size:22px;cursor:pointer;">✕</button>
        </div>
        <div class="sidebar-subtitle"{subtitle_style}>{subtitle}</div>
      </div>

      <ul class="sidebar-menu">
{menu_html}
      </ul>

      <div class="sidebar-footer">
{footer_badge}
      </div>
    </aside>'''

def render_top_header(is_admin):
    badge_label = "ADMIN" if is_admin else "CARE"
    badge_bg = "#24063E" if is_admin else "#F3E8FF"
    badge_color = "#967BB6" if is_admin else "#3B0764"
    email = "director.shilpi@thestackly.com" if is_admin else "lingalamanasa123@gmail.com"
    initials = "ADM" if is_admin else "LM"
    initial_bg = "#24063E" if is_admin else "#967BB6"
    initial_color = "#967BB6" if is_admin else "#111"
    border = "border:1.5px solid #967BB6;" if is_admin else ""
    
    return f'''      <header class="dash-top-header">
        <div style="display:flex;align-items:center;gap:14px;">
          <button id="dashMenuToggle" class="mobile-nav-toggle" style="display:block;padding:4px;" aria-label="Toggle Dashboard Menu">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
          </button>

          <div class="mobile-dash-brand">
            <img src="assets/img/stackly-icon.webp" alt="Stackly" class="logo-s-mark" style="height:26px;width:auto;">
            <span style="font-size:18px;font-weight:900;color:#111827;">STACKLY</span>
            <span style="font-size:9px;background:{badge_bg};color:{badge_color};padding:2px 6px;border-radius:4px;font-weight:800;">{badge_label}</span>
          </div>
        </div>

        <div class="dash-header-user">
          <span class="dash-header-email hide-mobile">{email}</span>
          <div style="width:36px;height:36px;border-radius:50%;background:{initial_bg};color:{initial_color};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:13px;{border}">
            {initials}
          </div>
        </div>
      </header>'''

def build_html(title, desc, filename, is_admin, body_html):
    sidebar = render_sidebar(filename, is_admin)
    header = render_top_header(is_admin)
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Stackly Women's Health Center</title>
  <meta name="description" content="{desc}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="icon" type="image/webp" href="assets/img/logo.webp">
</head>
<body style="background:#FAF9F5;">

  <div class="dashboard-layout">
{sidebar}

    <main class="dash-main">
{header}

      <div class="dash-body">
{body_html}
      </div>
    </main>
  </div>

  <script src="assets/js/main.js"></script>
</body>
</html>'''

print("generate_all_dashboards.py core framework ready.")
