# restore_previous_hero_and_navbar.py
# Restores the iconic previous Navigation Bar and Hero Section on every page

import re

def get_navbar_html(active_page="Home"):
    nav_items = [
        ("Home", "index.html"),
        ("About", "about.html"),
        ("Service", "services.html"),
        ("Blog", "blog.html"),
        ("Contact", "contact.html")
    ]
    
    links_html = []
    for label, href in nav_items:
        active_cls = " active" if label.lower() == active_page.lower() else ""
        links_html.append(f'          <li><a href="{href}" class="nav-link{active_cls}">{label}</a></li>')
    links_str = "\n".join(links_html)

    return f'''  <!-- Top Emergency Ticker -->
  <div class="top-bar-emergency">
    <div class="container top-bar-flex">
      <div>🚨 <strong>24×7 Maternity &amp; Emergency Helpline:</strong> <a href="tel:+917010792745">+91 70107 92745</a> / <a href="tel:+919555334107">+91 95553 34107</a></div>
      <div>🏥 <span>OPD Hours: Mon–Sat: 10:00 AM – 2:00 PM &amp; 5:00 PM – 8:00 PM (Emergency Open 24×7)</span></div>
    </div>
  </div>

  <!-- Site Header (Navigation Bar matching Screenshot 1) -->
  <header class="site-header">
    <div class="container">
      <nav class="navbar">
        <a href="index.html" class="brand-logo" aria-label="Stackly Women's Health Center Home">
          <img src="assets/img/stackly-icon.webp" alt="Stackly" class="logo-s-mark">
          <div class="logo-text-group">
            <span class="logo-brand-name">STACKLY</span>
            <span class="logo-brand-sub">WOMEN'S HEALTH CENTER</span>
          </div>
        </a>

        <ul class="nav-menu">
{links_str}
        </ul>

        <div class="nav-actions">
          <a href="login.html" class="btn-login">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
            <span>Login</span>
          </a>
          <a href="signup.html" class="btn-signup">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="8.5" cy="7" r="4"></circle><line x1="20" y1="8" x2="20" y2="14"></line><line x1="23" y1="11" x2="17" y2="11"></line></svg>
            <span>Signup</span>
          </a>
          <button class="mobile-nav-toggle" id="mobileNavToggle" aria-label="Toggle navigation menu">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
          </button>
        </div>
      </nav>
    </div>
  </header>'''

# 1. RESTORE index.html
index_hero = '''    <!-- SECTION 1: HERO SECTION (Mithila Exact 4-Image Crossfade Carousel + Lead Form) -->
    <section class="section_hero">
      <div class="hero-image_wrap">
        <img src="assets/img/gen_hero-slide-1.webp" alt="Women's Health Care Hero 1" class="hero-carousel-img is-active">
        <img src="assets/img/gen_hero-slide-2.webp" alt="Women's Health Care Hero 2" class="hero-carousel-img">
        <img src="assets/img/gen_hero-slide-3.webp" alt="Women's Health Care Hero 3" class="hero-carousel-img">
        <img src="assets/img/gen_hero-slide-4.webp" alt="Women's Health Care Hero 4" class="hero-carousel-img">
      </div>
      <div class="hero_overlay-wrap">
        <div class="hero_overlay"></div>
      </div>

      <div class="container" style="position:relative;z-index:3;">
        <div class="hero_content_grid">
          <!-- Left Column: Copy & Primary Action -->
          <div class="home-hero_content">
            <h1>Best Obstetrician &amp; Gynaecologist in Women's Health Center</h1>
            <p class="home-hero_para">
              Providing comprehensive, supportive, and expert gynecology, obstetrics, and high-risk maternity care under the guidance of Dr. Shilpi Singh at Stackly Women's Health Center. Prioritizing your comfort, dignity, and clinical safety at every stage of life.
            </p>
            <div style="display:flex;align-items:center;gap:18px;flex-wrap:wrap;">
              <a href="contact.html#book" class="button_primary">
                <span>Book Appointment</span>
                <span class="btn-arrow-icon">➔</span>
              </a>
            </div>
          </div>

          <!-- Right Column: Lead Form Card -->
          <div class="lead-form_card">
            <div class="lead-form_head">
              <h2 class="lead-form_title">Book a visit</h2>
              <p class="lead-form_sub">Get a callback within 10 minutes</p>
            </div>
            <form class="lead-form" onsubmit="event.preventDefault(); showToast('Appointment request sent! Our clinical team will call you back within 10 minutes.'); this.reset();">
              <input class="lead-form_input" type="text" placeholder="Your name" required name="name">
              <input class="lead-form_input" type="tel" placeholder="Enter your phone number" required name="phone">
              <select class="lead-form_input" required>
                <option value="">Select Specialty / Concern</option>
                <option value="pregnancy">Pregnancy &amp; Painless Delivery</option>
                <option value="high-risk">High-Risk Pregnancy</option>
                <option value="laparoscopy">Laparoscopic Surgery</option>
                <option value="pcos">PCOS / PCOD &amp; Periods</option>
                <option value="fertility">Fertility Consultation</option>
              </select>
              <button class="lead-form_btn" type="submit">Request Callback</button>
              <div class="lead-form_note">No spam. A real person calls you back, fast.</div>
            </form>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 2: OUR INFO 3-BOX BAR (Mithila Hospital exact layout) -->
    <div class="container">
      <div class="our-info_wrap">
        <div class="our-info_list">
          <!-- Item 1: Get Appointment -->
          <a href="contact.html#book" class="our-info_item">
            <div class="our-info_item-header">
              <div class="our-info_icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09zM12 15l-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/></svg>
              </div>
              <h3 class="our-info_title">Get Appointment</h3>
            </div>
            <div class="our-info_item-body">
              <p class="our-info_item-para">Ready to prioritise your health? Book your visit today. Click here to choose your slot.</p>
            </div>
          </a>

          <!-- Item 2: Emergency Contact -->
          <div class="our-info_item">
            <div class="our-info_item-header">
              <div class="our-info_icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"></rect><polygon points="16 8 20 8 23 11 23 16 16 8"></polygon><circle cx="5.5" cy="18.5" r="2.5"></circle><circle cx="18.5" cy="18.5" r="2.5"></circle></svg>
              </div>
              <h3 class="our-info_title">Emergency Contact</h3>
            </div>
            <div class="our-info_item-body">
              <div class="our-info_item-para">Call : <a href="tel:+917010792745" style="color:var(--primary-plum);font-weight:700;">+91 70107 92745</a> / <a href="tel:+919555334107" style="color:var(--primary-plum);font-weight:700;">+91 95553 34107</a></div>
              <div class="our-info_item-para" style="margin-top:4px;">Email: <a href="mailto:info@thestackly.com" style="color:var(--primary-plum);">info@thestackly.com</a></div>
            </div>
          </div>

          <!-- Item 3: Operational Hours -->
          <div class="our-info_item is-last">
            <div class="our-info_item-header">
              <div class="our-info_icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
              </div>
              <h3 class="our-info_title">Operational Hours</h3>
            </div>
            <div class="our-info_item-body">
              <div class="our-info_item-para" style="font-weight:700;color:var(--primary-plum);">Open All Days</div>
              <div class="our-info_item-para">24 × 7 Emergency &amp; Maternity Care</div>
            </div>
          </div>
        </div>
      </div>
    </div>'''

with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Replace from <body> to <!-- SECTION 3: OUR STORY
idx_top = idx_content[:idx_content.find('<body>') + 6]
preloader_part = ''
if 'id="stacklyPreloader"' in idx_content:
    p_end = idx_content.find('</div>\n  </div>\n\n')
    if p_end != -1:
        preloader_part = idx_content[idx_content.find('<!-- STACKLY PRELOADER'):p_end + 18]
    else:
        p_end2 = idx_content.find('</div>\n  </div>')
        preloader_part = idx_content[idx_content.find('<!-- STACKLY PRELOADER'):p_end2 + 15]

sec3_idx = idx_content.find('<!-- SECTION 3: OUR STORY')
idx_bottom = idx_content[sec3_idx:]

new_index = idx_top + '\n\n' + preloader_part + '\n\n' + get_navbar_html('Home') + '\n\n' + index_hero + '\n\n' + idx_bottom
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_index)
print("Restored index.html Navbar and Hero section!")

# 2. RESTORE about.html
about_hero = '''    <!-- SECTION 1: ABOUT US PAGE HERO BANNER -->
    <section class="section_hero page-hero-banner" style="min-height:380px;padding:60px 0 80px 0;">
      <div class="hero-image_wrap">
        <img src="assets/img/facility-suite.webp" alt="Stackly Women's Health Center" class="hero-carousel-img is-active">
      </div>
      <div class="hero_overlay-wrap">
        <div class="hero_overlay" style="background:linear-gradient(90deg, rgba(61, 39, 51, 0.95) 0%, rgba(61, 39, 51, 0.85) 60%, rgba(61, 39, 51, 0.7) 100%);"></div>
      </div>
      <div class="container" style="position:relative;z-index:3;">
        <div class="hero_content_grid">
          <div>
            <div style="display:flex;align-items:center;gap:8px;font-size:14px;color:rgba(255,255,255,0.7);margin-bottom:12px;">
              <a href="index.html" style="color:#ffffff;">Home</a> <span>/</span> <span>About Us</span>
            </div>
            <h1 style="font-size:48px;font-weight:800;color:#ffffff;line-height:1.2;margin-bottom:16px;">
              Dedicated to Every Stage of a Woman's Health Journey
            </h1>
            <p style="font-size:17px;color:rgba(255,255,255,0.85);max-width:540px;line-height:1.6;">
              Rooted in empathy, clinical excellence, and state-of-the-art infrastructure. Meet the obstetric and laparoscopic team you can trust for life.
            </p>
          </div>
          <div style="background:rgba(255,255,255,0.95);border-radius:24px;padding:32px;box-shadow:0 16px 36px rgba(0,0,0,0.25);">
            <h3 style="font-size:22px;color:var(--primary-plum);font-weight:800;margin-bottom:12px;">Hospital At A Glance</h3>
            <div style="font-size:14px;color:var(--text-muted);display:flex;flex-direction:column;gap:10px;">
              <div>📍 <strong>Location:</strong> Salem's Premier Women's Facility</div>
              <div>🏥 <strong>Accreditation:</strong> NABH-Grade Level-3 NICU</div>
              <div>🕒 <strong>Hours:</strong> 24×7 Maternity &amp; Emergency OT</div>
              <div>👩‍⚕️ <strong>Board:</strong> 15+ Senior Obstetric Surgeons</div>
            </div>
          </div>
        </div>
      </div>
    </section>'''

with open('about.html', 'r', encoding='utf-8') as f:
    about_content = f.read()

about_top = about_content[:about_content.find('<body>') + 6]
about_preloader = ''
if 'id="stacklyPreloader"' in about_content:
    p_end = about_content.find('</div>\n  </div>')
    about_preloader = about_content[about_content.find('<!-- STACKLY PRELOADER'):p_end + 15]

sec2_about = about_content.find('<!-- SECTION 2: FOUNDING STORY')
about_bottom = about_content[sec2_about:]

new_about = about_top + '\n\n' + about_preloader + '\n\n' + get_navbar_html('About') + '\n\n' + about_hero + '\n\n' + about_bottom
with open('about.html', 'w', encoding='utf-8') as f:
    f.write(new_about)
print("Restored about.html Navbar and Hero section!")

# 3. RESTORE services.html
services_hero = '''    <!-- SECTION 1: SERVICES PAGE HERO BANNER -->
    <section class="section_hero page-hero-banner" style="min-height:380px;padding:60px 0 80px 0;">
      <div class="hero-image_wrap">
        <img src="assets/img/facility-ot.webp" alt="Stackly Clinical Specialties" class="hero-carousel-img is-active">
      </div>
      <div class="hero_overlay-wrap">
        <div class="hero_overlay" style="background:linear-gradient(90deg, rgba(61, 39, 51, 0.95) 0%, rgba(61, 39, 51, 0.85) 60%, rgba(61, 39, 51, 0.7) 100%);"></div>
      </div>
      <div class="container" style="position:relative;z-index:3;">
        <div class="hero_content_grid">
          <div>
            <div style="display:flex;align-items:center;gap:8px;font-size:14px;color:rgba(255,255,255,0.7);margin-bottom:12px;">
              <a href="index.html" style="color:#ffffff;">Home</a> <span>/</span> <span>Clinical Services</span>
            </div>
            <h1 style="font-size:48px;font-weight:800;color:#ffffff;line-height:1.2;margin-bottom:16px;">
              Specialized Care for Every Phase of Womanhood
            </h1>
            <p style="font-size:17px;color:rgba(255,255,255,0.85);max-width:540px;line-height:1.6;">
              From pain-free maternity and high-risk fetal medicine to keyhole laparoscopic surgeries and PCOS holistic wellness.
            </p>
          </div>
          <div style="background:rgba(255,255,255,0.95);border-radius:24px;padding:32px;box-shadow:0 16px 36px rgba(0,0,0,0.25);">
            <h3 style="font-size:22px;color:var(--primary-plum);font-weight:800;margin-bottom:12px;">24×7 Specialist Care</h3>
            <p style="font-size:14px;color:var(--text-muted);margin-bottom:18px;">Emergency maternity admission or specialist consultation booking available around the clock.</p>
            <a href="contact.html#book" class="button_primary" style="width:100%;justify-content:center;">Book Instant Consultation</a>
          </div>
        </div>
      </div>
    </section>'''

with open('services.html', 'r', encoding='utf-8') as f:
    services_content = f.read()

serv_top = services_content[:services_content.find('<body>') + 6]
serv_preloader = ''
if 'id="stacklyPreloader"' in services_content:
    p_end = services_content.find('</div>\n  </div>')
    serv_preloader = services_content[services_content.find('<!-- STACKLY PRELOADER'):p_end + 15]

sec2_serv = services_content.find('<!-- SECTION 3: BENTO SERVICE [ 02 ]')
# If section 2 was right before:
serv_bottom = services_content[sec2_serv:]

new_services = serv_top + '\n\n' + serv_preloader + '\n\n' + get_navbar_html('Service') + '\n\n' + services_hero + '\n\n' + serv_bottom
with open('services.html', 'w', encoding='utf-8') as f:
    f.write(new_services)
print("Restored services.html Navbar and Hero section!")

# 4. RESTORE blog.html
blog_hero = '''    <!-- SECTION 1: BLOG PAGE HERO BANNER -->
    <section class="section_hero page-hero-banner" style="min-height:360px;padding:60px 0 80px 0;">
      <div class="hero-image_wrap">
        <img src="assets/img/facility-ultrasound.webp" alt="Women's Health Blog" class="hero-carousel-img is-active">
      </div>
      <div class="hero_overlay-wrap">
        <div class="hero_overlay" style="background:linear-gradient(90deg, rgba(61, 39, 51, 0.95) 0%, rgba(61, 39, 51, 0.85) 60%, rgba(61, 39, 51, 0.7) 100%);"></div>
      </div>
      <div class="container" style="position:relative;z-index:3;">
        <div>
          <div style="display:flex;align-items:center;gap:8px;font-size:14px;color:rgba(255,255,255,0.7);margin-bottom:12px;">
            <a href="index.html" style="color:#ffffff;">Home</a> <span>/</span> <span>Health Journal</span>
          </div>
          <h1 style="font-size:46px;font-weight:800;color:#ffffff;line-height:1.2;margin-bottom:14px;">
            Doctor-Verified Insights &amp; Maternity Guides
          </h1>
          <p style="font-size:17px;color:rgba(255,255,255,0.85);max-width:620px;line-height:1.6;">
            Accurate, evidence-based articles authored by senior gynecologists and pediatricians to guide you through pregnancy, reproductive health, and wellness.
          </p>
        </div>
      </div>
    </section>'''

with open('blog.html', 'r', encoding='utf-8') as f:
    blog_content = f.read()

blog_top = blog_content[:blog_content.find('<body>') + 6]
blog_preloader = ''
if 'id="stacklyPreloader"' in blog_content:
    p_end = blog_content.find('</div>\n  </div>')
    blog_preloader = blog_content[blog_content.find('<!-- STACKLY PRELOADER'):p_end + 15]

sec5_blog = blog_content.find('<!-- SECTION 5: CLINICAL REVIEW BOARD')
blog_bottom = blog_content[sec5_blog:]

new_blog = blog_top + '\n\n' + blog_preloader + '\n\n' + get_navbar_html('Blog') + '\n\n' + blog_hero + '\n\n' + blog_bottom
with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(new_blog)
print("Restored blog.html Navbar and Hero section!")

# 5. RESTORE contact.html
contact_hero = '''    <!-- SECTION 1: CONTACT PAGE HERO BANNER -->
    <section class="section_hero page-hero-banner" style="min-height:360px;padding:60px 0 80px 0;">
      <div class="hero-image_wrap">
        <img src="assets/img/gen_hero-slide-1.webp" alt="Contact Stackly" class="hero-carousel-img is-active">
      </div>
      <div class="hero_overlay-wrap">
        <div class="hero_overlay" style="background:linear-gradient(90deg, rgba(61, 39, 51, 0.95) 0%, rgba(61, 39, 51, 0.85) 60%, rgba(61, 39, 51, 0.7) 100%);"></div>
      </div>
      <div class="container" style="position:relative;z-index:3;">
        <div>
          <div style="display:flex;align-items:center;gap:8px;font-size:14px;color:rgba(255,255,255,0.7);margin-bottom:12px;">
            <a href="index.html" style="color:#ffffff;">Home</a> <span>/</span> <span>Contact &amp; Emergency</span>
          </div>
          <h1 style="font-size:46px;font-weight:800;color:#ffffff;line-height:1.2;margin-bottom:14px;">
            We're Here for You, 24 Hours a Day, 7 Days a Week
          </h1>
          <p style="font-size:17px;color:rgba(255,255,255,0.85);max-width:620px;line-height:1.6;">
            Walk in for immediate obstetric triage, schedule a consultation with our senior specialists, or connect with our patient support desk.
          </p>
        </div>
      </div>
    </section>'''

with open('contact.html', 'r', encoding='utf-8') as f:
    contact_content = f.read()

contact_top = contact_content[:contact_content.find('<body>') + 6]
contact_preloader = ''
if 'id="stacklyPreloader"' in contact_content:
    p_end = contact_content.find('</div>\n  </div>')
    contact_preloader = contact_content[contact_content.find('<!-- STACKLY PRELOADER'):p_end + 15]

sec2_contact = contact_content.find('<!-- SECTION 2: 3 DIRECT CONTACT CHANNELS')
if sec2_contact == -1:
    sec2_contact = contact_content.find('<!-- SECTION 3: INTERACTIVE BOOKING')
contact_bottom = contact_content[sec2_contact:] if sec2_contact != -1 else contact_content[contact_content.find('<section class="section-padding"'):]

new_contact = contact_top + '\n\n' + contact_preloader + '\n\n' + get_navbar_html('Contact') + '\n\n' + contact_hero + '\n\n' + contact_bottom
with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(new_contact)
print("Restored contact.html Navbar and Hero section!")

# 6. RESTORE NAVBAR & HERO STYLING IN style.css
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Restore top-bar-emergency
css = re.sub(r'\.top-bar-emergency\s*\{[^}]*\}', '''.top-bar-emergency {
  background: #0e0f12;
  color: #d1d5db;
  font-size: 13px;
  padding: 7px 0;
  border-bottom: 1px solid #1f242d;
}''', css)

# Restore top-bar-flex a
css = re.sub(r'\.top-bar-flex a\s*\{[^}]*\}', '''.top-bar-flex a {
  color: #f59e0b;
  font-weight: 700;
}''', css)

# Restore site-header
css = re.sub(r'\.site-header\s*\{[^}]*\}', '''.site-header {
  position: sticky;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background-color: #ffffff;
  border-bottom: 1px solid #f1f2f4;
  box-shadow: 0 1px 6px rgba(0,0,0,0.03);
}''', css)

# Restore brand-logo and subtitle
css = re.sub(r'\.logo-brand-name\s*\{[^}]*\}', '''.logo-brand-name {
  font-size: 23px;
  font-weight: 900;
  letter-spacing: 0.8px;
  color: #111827;
  line-height: 1.1;
}''', css)

css = re.sub(r'\.logo-brand-sub\s*\{[^}]*\}', '''.logo-brand-sub {
  font-size: 10px;
  font-weight: 700;
  color: #f59e0b;
  letter-spacing: 1px;
  text-transform: uppercase;
}''', css)

# Restore nav-link active / hover
css = re.sub(r'\.nav-link\s*\{[^}]*\}', '''.nav-link {
  font-size: 15px;
  font-weight: 500;
  color: #374151;
  position: relative;
  padding: 8px 0;
  transition: var(--transition);
}''', css)

css = re.sub(r'\.nav-link:hover\s*\{[^}]*\}', '''.nav-link:hover {
  color: #f59e0b;
}''', css)

css = re.sub(r'\.nav-link\.active\s*\{[^}]*\}', '''.nav-link.active {
  color: #f59e0b;
  font-weight: 700;
}''', css)

css = re.sub(r'\.nav-link\.active::after\s*\{[^}]*\}', '''.nav-link.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 3px;
  background-color: #f59e0b;
  border-radius: 2px;
}''', css)

# Restore btn-login
css = re.sub(r'\.btn-login\s*\{[^}]*\}', '''.btn-login {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 22px;
  background-color: #ffffff;
  color: #1f2937;
  border: 1.5px solid #e5e7eb;
  border-radius: var(--radius-pill);
  font-size: 14px;
  font-weight: 600;
  transition: var(--transition);
}''', css)

css = re.sub(r'\.btn-login:hover\s*\{[^}]*\}', '''.btn-login:hover {
  border-color: #f59e0b;
  color: #d97706;
  background-color: #fffbeb;
}''', css)

# Restore btn-signup
css = re.sub(r'\.btn-signup\s*\{[^}]*\}', '''.btn-signup {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 9px 24px;
  background-color: #f59e0b;
  color: #111827;
  border: none;
  border-radius: var(--radius-pill);
  font-size: 14px;
  font-weight: 700;
  box-shadow: 0 4px 14px rgba(245, 158, 11, 0.35);
  transition: var(--transition);
}''', css)

css = re.sub(r'\.btn-signup:hover\s*\{[^}]*\}', '''.btn-signup:hover {
  background-color: #d97706;
  box-shadow: 0 6px 18px rgba(217, 119, 6, 0.45);
  transform: translateY(-1px);
}''', css)

# Restore Section Hero
css = re.sub(r'\.section_hero\s*\{[^}]*\}', '''.section_hero {
  position: relative;
  background-color: #3d2733;
  color: #ffffff;
  min-height: 600px;
  display: flex;
  align-items: center;
  overflow: hidden;
  padding: 90px 0 130px 0;
}''', css)

css = re.sub(r'\.hero_overlay\s*\{[^}]*\}', '''.hero_overlay {
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, rgba(61, 39, 51, 0.95) 0%, rgba(61, 39, 51, 0.85) 48%, rgba(61, 39, 51, 0.65) 100%);
}''', css)

# Lead form button
css = re.sub(r'\.lead-form_btn\s*\{[^}]*\}', '''.lead-form_btn {
  width: 100%;
  height: 50px;
  background-color: #3d2733;
  color: #ffffff;
  border: none;
  border-radius: var(--radius-md);
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 4px 14px rgba(61, 39, 51, 0.25);
  transition: var(--transition);
}''', css)

css = re.sub(r'\.lead-form_btn:hover\s*\{[^}]*\}', '''.lead-form_btn:hover {
  background-color: #24141e;
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(61, 39, 51, 0.35);
}''', css)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Restored original Navigation Bar and Hero styles in style.css!")
