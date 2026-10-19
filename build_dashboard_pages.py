# build_dashboard_pages.py
# Generates separate user and admin dashboard pages with 5 rich UI/UX sections each
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

def render_user_sidebar(active_file):
    items = []
    for href, icon, title in USER_MENU:
        active_cls = " active" if href == active_file else ""
        items.append(f'        <li><a href="{href}" class="{active_cls}"><span>{icon}</span> <span>{title}</span></a></li>')
    menu_html = "\n".join(items)
    
    return f'''    <!-- Warm Golden Amber Sidebar -->
    <aside class="dash-sidebar" id="dashSidebar">
      <div class="sidebar-header">
        <div style="display:flex;align-items:center;justify-content:space-between;">
          <a href="index.html" class="brand-logo">
            <img src="assets/img/stackly-icon.webp" alt="Stackly" class="logo-s-mark" style="height:32px;width:auto;">
            <span class="sidebar-brand-name">STACKLY</span>
          </a>
          <button id="closeDashSidebar" style="display:none;background:none;border:none;color:#fff;font-size:22px;cursor:pointer;">✕</button>
        </div>
        <div class="sidebar-subtitle">CARE CLOUD PORTAL</div>
      </div>

      <ul class="sidebar-menu">
{menu_html}
      </ul>

      <!-- User Profile Card in Sidebar Footer -->
      <div class="sidebar-footer">
        <div class="user-profile-badge">
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
        </div>
      </div>
    </aside>'''

def render_admin_sidebar(active_file):
    items = []
    for href, icon, title in ADMIN_MENU:
        active_cls = " active" if href == active_file else ""
        items.append(f'        <li><a href="{href}" class="{active_cls}"><span>{icon}</span> <span>{title}</span></a></li>')
    menu_html = "\n".join(items)
    
    return f'''    <!-- Deep Navy Slate Sidebar -->
    <aside class="dash-sidebar admin-theme" id="dashSidebar">
      <div class="sidebar-header">
        <div style="display:flex;align-items:center;justify-content:space-between;">
          <a href="index.html" class="brand-logo">
            <img src="assets/img/stackly-icon.webp" alt="Stackly" class="logo-s-mark" style="height:32px;width:auto;">
            <span class="sidebar-brand-name">STACKLY</span>
          </a>
          <button id="closeDashSidebar" style="display:none;background:none;border:none;color:#fff;font-size:22px;cursor:pointer;">✕</button>
        </div>
        <div class="sidebar-subtitle" style="color:#f59e0b;">HOSPITAL ADMIN COCKPIT</div>
      </div>

      <ul class="sidebar-menu">
{menu_html}
      </ul>

      <!-- Admin User Badge -->
      <div class="sidebar-footer">
        <div class="user-profile-badge" style="background:#0f172a;">
          <div class="user-profile-info">
            <div class="user-avatar-circle" style="background:#f59e0b;color:#111;">DS</div>
            <div class="user-profile-text">
              <div class="user-profile-name">Dr. Shilpi Singh</div>
              <div class="user-profile-role">Chief Clinical Director</div>
            </div>
          </div>
          <button onclick="logoutUser()" class="btn-sidebar-logout">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4M16 17l5-5-5-5M21 12H9"/></svg>
            <span>LOGOUT ADMIN</span>
          </button>
        </div>
      </div>
    </aside>'''

def render_top_header(is_admin=False):
    badge_label = "ADMIN" if is_admin else "CARE"
    badge_bg = "#1e293b" if is_admin else "#fef3c7"
    badge_color = "#f59e0b" if is_admin else "#b45309"
    email = "director.shilpi@thestackly.com" if is_admin else "lingalamanasa123@gmail.com"
    initials = "ADM" if is_admin else "LM"
    initial_bg = "#1e293b" if is_admin else "#f59e0b"
    initial_color = "#f59e0b" if is_admin else "#111"
    border = "border:1.5px solid #f59e0b;" if is_admin else ""
    
    return f'''      <!-- Top Bar Header -->
      <header class="dash-top-header">
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

def build_page_template(title, desc, filename, is_admin, content_body):
    sidebar = render_admin_sidebar(filename) if is_admin else render_user_sidebar(filename)
    header = render_top_header(is_admin)
    theme_bg = "#0f172a" if is_admin else "#f8fafc"
    
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
<body style="background:#f8fafc;">

  <div class="dashboard-layout">
{sidebar}

    <!-- Main Content Area -->
    <main class="dash-main">
{header}

      <!-- Dashboard Body -->
      <div class="dash-body">
{content_body}
      </div>
    </main>
  </div>

  <script src="assets/js/main.js"></script>
</body>
</html>'''

print("Builder template initialized.")
