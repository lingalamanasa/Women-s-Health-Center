/* ==========================================================================
   STACKLY WOMEN'S HEALTH CENTER - JAVASCRIPT CONTROLLER
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  initPreloader();
  initMobileNav();
  initHeroCarousel();
  initStorySlider();
  initWobbleCards();
  initFaqAccordion();
  initForms();
  initAuthLogic();
  initDashboardFeatures();
});

// Also trigger immediate setup if document already running
if (document.readyState === 'interactive' || document.readyState === 'complete') {
  initPreloader();
  initMobileNav();
  initHeroCarousel();
  initWobbleCards();
  initDashboardFeatures();
}

/* --------------------------------------------------------------------------
   Hero Carousel Auto-Crossfade & Dynamic Scrolling Background
   -------------------------------------------------------------------------- */
let heroCarouselInitialized = false;
function initHeroCarousel() {
  if (heroCarouselInitialized) return;
  const heroWraps = document.querySelectorAll('.hero-image_wrap');
  if (!heroWraps.length) return;
  heroCarouselInitialized = true;

  heroWraps.forEach(wrap => {
    const heroImgs = wrap.querySelectorAll('.hero-carousel-img');
    if (heroImgs.length <= 1) return;

    let currentIdx = 0;
    if (!wrap.querySelector('.hero-carousel-img.is-active')) {
      heroImgs[0].classList.add('is-active');
    }

    setInterval(() => {
      heroImgs[currentIdx].classList.remove('is-active');
      currentIdx = (currentIdx + 1) % heroImgs.length;
      heroImgs[currentIdx].classList.add('is-active');
    }, 4200);
  });
}

/* --------------------------------------------------------------------------
   Our Story Interactive Slider with Real-time Progress Bars
   -------------------------------------------------------------------------- */
function initStorySlider() {
  const track = document.getElementById('storySliderTrack');
  const cards = document.querySelectorAll('.story-slide-card');
  const prevBtn = document.getElementById('storyPrevBtn');
  const nextBtn = document.getElementById('storyNextBtn');

  if (!cards.length) return;

  let activeIndex = 0;
  let autoTimer = null;

  function updateActiveCard(index) {
    activeIndex = (index + cards.length) % cards.length;
    cards.forEach((c, i) => {
      if (i === activeIndex) {
        c.classList.add('active');
        // fill progress up to this index
        const blocks = c.querySelectorAll('.our-story_item-progress_block');
        blocks.forEach((b, bi) => {
          if (bi <= i) {
            b.classList.add('is-progress');
          } else {
            b.classList.remove('is-progress');
          }
        });
      } else {
        c.classList.remove('active');
      }
    });

    if (track) {
      const cardWidth = cards[0].offsetWidth + 20;
      track.scrollTo({
        left: activeIndex * cardWidth,
        behavior: 'smooth'
      });
    }
  }

  function startStoryTimer() {
    stopStoryTimer();
    autoTimer = setInterval(() => {
      updateActiveCard(activeIndex + 1);
    }, 4500);
  }

  function stopStoryTimer() {
    if (autoTimer) clearInterval(autoTimer);
  }

  cards.forEach((card, idx) => {
    card.addEventListener('click', () => {
      updateActiveCard(idx);
      startStoryTimer();
    });
  });

  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      updateActiveCard(activeIndex - 1);
      startStoryTimer();
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      updateActiveCard(activeIndex + 1);
      startStoryTimer();
    });
  }

  const sliderWrap = document.querySelector('.story-slider-wrap');
  if (sliderWrap) {
    sliderWrap.addEventListener('mouseenter', stopStoryTimer);
    sliderWrap.addEventListener('mouseleave', startStoryTimer);
  }

  updateActiveCard(0);
  startStoryTimer();
}

/* --------------------------------------------------------------------------
   Springboard Mobile Navigation Drawer Controller
   -------------------------------------------------------------------------- */
let mobileNavInitialized = false;
function initMobileNav() {
  if (mobileNavInitialized) return;
  mobileNavInitialized = true;

  let drawer = document.getElementById('mobileDrawer');

  // If mobileDrawer does not exist in the DOM on this page, dynamically construct it
  if (!drawer) {
    drawer = document.createElement('div');
    drawer.id = 'mobileDrawer';
    drawer.className = 'mobile-drawer';
    drawer.setAttribute('role', 'dialog');
    drawer.setAttribute('aria-modal', 'true');
    drawer.setAttribute('aria-label', 'Mobile navigation menu');

    const currentPath = window.location.pathname.toLowerCase();
    const isHome = currentPath.endsWith('index.html') || currentPath === '/' || currentPath.endsWith('/women-s-health-center/') || (!currentPath.includes('.html') && !currentPath.includes('admin') && !currentPath.includes('user'));
    const isAbout = currentPath.includes('about');
    const isService = currentPath.includes('service');
    const isBlog = currentPath.includes('blog');
    const isContact = currentPath.includes('contact');

    drawer.innerHTML = `
      <div class="mobile-drawer-content">
        <div class="drawer-header">
          <div class="drawer-brand">
            <img src="assets/img/stackly-icon.webp" alt="Stackly" style="height:32px;width:auto;">
            <span class="drawer-brand-title">STACKLY</span>
          </div>
          <button id="closeMobileDrawer" class="drawer-close-btn" aria-label="Close navigation menu">✕</button>
        </div>

        <ul class="drawer-nav-list">
          <li class="springboard-item"><a href="index.html" class="drawer-nav-link ${isHome ? 'active' : ''}"><span>🏠 Home</span> <span>→</span></a></li>
          <li class="springboard-item"><a href="about.html" class="drawer-nav-link ${isAbout ? 'active' : ''}"><span>🏥 About Us</span> <span>→</span></a></li>
          <li class="springboard-item"><a href="services.html" class="drawer-nav-link ${isService ? 'active' : ''}"><span>🩺 Clinical Services</span> <span>→</span></a></li>
          <li class="springboard-item"><a href="blog.html" class="drawer-nav-link ${isBlog ? 'active' : ''}"><span>📰 Health Insights</span> <span>→</span></a></li>
          <li class="springboard-item"><a href="contact.html" class="drawer-nav-link ${isContact ? 'active' : ''}"><span>📍 Contact &amp; OPD</span> <span>→</span></a></li>
        </ul>

        <div class="drawer-actions-wrap">
          <a href="404.html" class="drawer-cta-btn springboard-item">
            <span>Book Appointment</span>
            <span>➔</span>
          </a>
          <div class="drawer-auth-row springboard-item">
            <a href="login.html" class="drawer-auth-btn login">Sign In</a>
            <a href="signup.html" class="drawer-auth-btn signup">Register</a>
          </div>
          <div class="drawer-emergency-info springboard-item">
            <span style="font-size:18px;">🚨</span>
            <div>
              <strong style="color:#19042B;">24/7 Maternity Emergency</strong><br>
              <a href="tel:+919876543210" style="color:#967BB6;font-weight:700;">+91 98765 43210</a>
            </div>
          </div>
        </div>
      </div>
    `;
    document.body.appendChild(drawer);
  }

  const toggleBtns = document.querySelectorAll('.mobile-nav-toggle, #mobileNavToggle');
  const closeBtn = document.getElementById('closeMobileDrawer');

  function openMenu() {
    drawer.classList.add('open');
    document.body.classList.add('menu-open');
    document.body.style.overflow = 'hidden';
    if (closeBtn) closeBtn.focus();
  }

  function closeMenu() {
    drawer.classList.remove('open');
    document.body.classList.remove('menu-open');
    document.body.style.overflow = '';
  }

  toggleBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      openMenu();
    });
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      closeMenu();
    });
  }

  // Close when clicking outside content (backdrop)
  drawer.addEventListener('click', (e) => {
    if (e.target === drawer) {
      closeMenu();
    }
  });

  // Close on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer.classList.contains('open')) {
      closeMenu();
    }
  });

  // Close when clicking any nav link
  const drawerLinks = drawer.querySelectorAll('.drawer-nav-link, .drawer-cta-btn, .drawer-auth-btn');
  drawerLinks.forEach(link => {
    link.addEventListener('click', () => {
      closeMenu();
    });
  });
}

/* --------------------------------------------------------------------------
   Wobble Card Entrance Animation (Scroll-Triggered via IntersectionObserver)
   -------------------------------------------------------------------------- */
let wobbleObserverInitialized = false;
function initWobbleCards() {
  if (wobbleObserverInitialized) return;

  // Respect reduced motion preference
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    return;
  }

  const cardSelectors = [
    '.our-info_item',
    '.story-slide-card',
    '.service_item-wrap',
    '.doctor_spotlight_card',
    '.ui-card',
    '.metric-card',
    '.action-card',
    '.dash-panel',
    '.faq-item',
    '.lead-form_card'
  ];

  const cards = document.querySelectorAll(cardSelectors.join(', '));
  if (!cards.length) return;
  wobbleObserverInitialized = true;

  cards.forEach(card => {
    card.classList.add('wobble-card-ready');
  });

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const target = entry.target;
        // Calculate stagger relative to sibling cards in parent
        const parent = target.parentElement;
        let index = 0;
        if (parent) {
          const siblings = Array.from(parent.children).filter(el => el.classList.contains('wobble-card-ready'));
          index = Math.max(0, siblings.indexOf(target));
        }
        const delay = Math.min(index * 0.08, 0.4);
        target.style.setProperty('--card-stagger-delay', `${delay}s`);
        target.classList.add('wobble-card-enter');
        obs.unobserve(target); // Animate once
      }
    });
  }, {
    threshold: 0.08,
    rootMargin: '0px 0px -30px 0px'
  });

  cards.forEach(card => observer.observe(card));
}

/* --------------------------------------------------------------------------
   FAQ Accordions
   -------------------------------------------------------------------------- */
function initFaqAccordion() {
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    if (question) {
      question.addEventListener('click', () => {
        const isActive = item.classList.contains('active');
        // Close others
        faqItems.forEach(other => other.classList.remove('active'));
        if (!isActive) {
          item.classList.add('active');
        }
      });
    }
  });
}

/* --------------------------------------------------------------------------
   Interactive Forms & Appointments
   -------------------------------------------------------------------------- */
function initForms() {
  const leadForms = document.querySelectorAll('.lead-form, .appointment-form');
  leadForms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const submitBtn = form.querySelector('button[type="submit"]');
      const originalText = submitBtn ? submitBtn.innerText : 'Submit';
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerText = 'Confirming Booking...';
      }

      setTimeout(() => {
        showToast('✓ Appointment Request Received! Our medical coordinator will call you within 10 minutes.');
        form.reset();
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerText = originalText;
        }
      }, 900);
    });
  });
}

/* --------------------------------------------------------------------------
   Authentication: Role Switcher & Sign In / Sign Up
   -------------------------------------------------------------------------- */
function initAuthLogic() {
  const roleButtons = document.querySelectorAll('.role-toggle-btn');
  let currentRole = 'user'; // default

  roleButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      roleButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentRole = btn.dataset.role || 'user';
      
      const roleNotice = document.getElementById('roleNotice');
      if (roleNotice) {
        if (currentRole === 'admin') {
          roleNotice.innerText = '🛡️ Signing in to Hospital Administrator & Clinical Cockpit';
        } else {
          roleNotice.innerText = '👤 Signing in to Patient Care Cloud & Telemetry Portal';
        }
      }
    });
  });

  // Login Form
  const loginForm = document.getElementById('loginForm');
  if (loginForm) {
    loginForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const emailInput = document.getElementById('loginEmail');
      const inputVal = emailInput && emailInput.value ? emailInput.value.trim() : (currentRole === 'admin' ? 'director.shilpi@thestackly.com' : 'lingalamanasa123@gmail.com');
      
      let email = inputVal;
      let userName = '';
      if (inputVal.includes('@')) {
        email = inputVal;
        const prefix = inputVal.split('@')[0];
        userName = prefix.charAt(0).toUpperCase() + prefix.slice(1);
      } else {
        userName = inputVal;
        email = inputVal.toLowerCase().replace(/\s+/g, '') + '@thestackly.com';
      }

      let initials = '';
      const parts = userName.trim().split(/\s+/);
      if (parts.length >= 2) {
        initials = (parts[0][0] + parts[1][0]).toUpperCase();
      } else {
        initials = userName.slice(0, 2).toUpperCase();
      }

      // Save session
      localStorage.setItem('stackly_user_email', email);
      localStorage.setItem('stackly_user_name', userName);
      localStorage.setItem('stackly_user_initials', initials);
      localStorage.setItem('stackly_user_role', currentRole);

      showToast(`Welcome! Signing you in as ${userName}...`);

      setTimeout(() => {
        if (currentRole === 'admin') {
          window.location.href = 'dashboard-admin.html';
        } else {
          window.location.href = 'dashboard-user.html';
        }
      }, 700);
    });
  }

  // Signup Form
  const signupForm = document.getElementById('signupForm');
  if (signupForm) {
    signupForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const fnInput = document.getElementById('signupFirstName');
      const lnInput = document.getElementById('signupLastName');
      const emailInput = document.getElementById('signupEmail');

      const fn = fnInput && fnInput.value ? fnInput.value.trim() : 'Manasa';
      const ln = lnInput && lnInput.value ? lnInput.value.trim() : 'Lingala';
      const email = emailInput && emailInput.value ? emailInput.value.trim() : 'lingalamanasa123@gmail.com';
      const userName = `${fn} ${ln}`.trim();
      const initials = (fn[0] + (ln ? ln[0] : (fn[1] || 'M'))).toUpperCase();

      localStorage.setItem('stackly_user_email', email);
      localStorage.setItem('stackly_user_name', userName);
      localStorage.setItem('stackly_user_initials', initials);
      localStorage.setItem('stackly_user_role', currentRole);

      showToast(`Account Created Successfully! Welcome ${userName}!`);

      setTimeout(() => {
        if (currentRole === 'admin') {
          window.location.href = 'dashboard-admin.html';
        } else {
          window.location.href = 'dashboard-user.html';
        }
      }, 700);
    });
  }
}

// Quick Autofill for Demo
window.fillDemoCredentials = function(role) {
  const userToggle = document.getElementById('toggleUser');
  const adminToggle = document.getElementById('toggleAdmin');
  const emailInput = document.getElementById('loginEmail');
  const passInput = document.getElementById('loginPassword');

  if (role === 'admin') {
    if (adminToggle) adminToggle.click();
    if (emailInput) emailInput.value = 'director.shilpi@thestackly.com';
    if (passInput) passInput.value = 'AdminPass2026!';
  } else {
    if (userToggle) userToggle.click();
    if (emailInput) emailInput.value = 'lingalamanasa123@gmail.com';
    if (passInput) passInput.value = 'PatientPass2026!';
  }
};

/* --------------------------------------------------------------------------
   Dynamic Dashboard User Sync (Auto-Syncs Logged-in Name, Email & Avatar)
   -------------------------------------------------------------------------- */
window.syncDashboardUserInfo = function() {
  const isDashboard = document.querySelector('.dash-sidebar, .dash-main');
  if (!isDashboard) return;

  const isAdminPage = window.location.pathname.includes('admin') || 
                      document.querySelector('.mobile-dash-brand span:last-child')?.textContent.includes('ADMIN');

  const userRole = localStorage.getItem('stackly_user_role') || (isAdminPage ? 'admin' : 'user');
  let currentEmail = localStorage.getItem('stackly_user_email');
  let currentName = localStorage.getItem('stackly_user_name');
  let currentInitials = localStorage.getItem('stackly_user_initials');

  if (isAdminPage && userRole === 'admin' && currentEmail && currentEmail !== 'lingalamanasa123@gmail.com') {
    // Admin has logged in with particular email
    if (!currentName) {
      const p = currentEmail.split('@')[0];
      currentName = p.charAt(0).toUpperCase() + p.slice(1);
    }
  } else if (isAdminPage && userRole !== 'admin') {
    // Default admin view
    currentEmail = 'director.shilpi@thestackly.com';
    currentName = 'Dr. Shilpi Singh';
    currentInitials = 'DS';
  } else {
    // User dashboard
    if (!currentEmail) currentEmail = 'lingalamanasa123@gmail.com';
    if (!currentName) {
      if (currentEmail.includes('@')) {
        const p = currentEmail.split('@')[0];
        currentName = p.charAt(0).toUpperCase() + p.slice(1);
      } else {
        currentName = currentEmail;
      }
    }
    if (!currentInitials) {
      const parts = currentName.trim().split(/\s+/);
      if (parts.length >= 2) {
        currentInitials = (parts[0][0] + parts[1][0]).toUpperCase();
      } else {
        currentInitials = currentName.slice(0, 2).toUpperCase();
      }
    }
  }

  // 1. Update Top-Right Header Email
  document.querySelectorAll('.dash-header-email').forEach(el => {
    el.textContent = currentEmail;
  });

  // 2. Update Top-Right Header Avatar Circle
  document.querySelectorAll('.dash-header-user > div').forEach(el => {
    el.textContent = currentInitials;
  });

  // 3. Update Welcome Greeting Title
  document.querySelectorAll('.dash-welcome-title').forEach(el => {
    if (el.textContent.includes('Welcome back') || el.hasAttribute('data-welcome') || el.classList.contains('dyn-welcome')) {
      el.innerHTML = `Welcome back, <span class="dyn-user-name">${currentName}</span> 👋`;
    }
  });

  // 4. Update Sidebar Profile Footer
  document.querySelectorAll('.user-profile-name').forEach(el => {
    el.textContent = currentName;
  });

  document.querySelectorAll('.user-profile-role').forEach(el => {
    if (el.textContent.includes('@') || el.classList.contains('user-role-email') || !isAdminPage) {
      el.textContent = currentEmail;
    }
  });

  document.querySelectorAll('.user-avatar-circle').forEach(el => {
    el.textContent = currentInitials;
  });
};

/* --------------------------------------------------------------------------
   Dashboard Features (User & Admin)
   -------------------------------------------------------------------------- */
function initDashboardFeatures() {
  syncDashboardUserInfo();

  // Mobile Dashboard Sidebar Toggle
  const dashMenuBtn = document.getElementById('dashMenuToggle');
  const dashSidebar = document.querySelector('.dash-sidebar');
  const closeSidebarBtn = document.getElementById('closeDashSidebar');

  if (dashMenuBtn && dashSidebar) {
    dashMenuBtn.addEventListener('click', () => {
      dashSidebar.classList.toggle('mobile-open');
    });
  }

  if (closeSidebarBtn && dashSidebar) {
    closeSidebarBtn.addEventListener('click', () => {
      dashSidebar.classList.remove('mobile-open');
    });
  }

  // Pill Reminder Checkbox simulator
  const pillCheckboxes = document.querySelectorAll('.pill-check');
  pillCheckboxes.forEach(box => {
    box.addEventListener('change', (e) => {
      const parent = box.closest('.pill-item');
      if (box.checked) {
        if (parent) parent.style.opacity = '0.5';
        showToast('✓ Dose marked as taken. Health timeline updated!');
      } else {
        if (parent) parent.style.opacity = '1';
      }
    });
  });
}

/* --------------------------------------------------------------------------
   Download Simulation / Booking Modals
   -------------------------------------------------------------------------- */
window.simulateDownloadReport = function(reportName) {
  showToast(`📥 Preparing encrypted download: ${reportName}.pdf...`);
  setTimeout(() => {
    showToast(`✓ Download Complete: ${reportName}.pdf (Verified 256-Bit SSL)`);
  }, 1200);
};

window.quickBookAction = function() {
  const modal = document.getElementById('bookingModal');
  if (modal) {
    modal.style.display = 'flex';
  } else {
    showToast('📅 Redirecting to Senior Doctor Scheduling Desk...');
    setTimeout(() => {
      window.location.href = 'contact.html#book';
    }, 500);
  }
};

window.closeBookingModal = function() {
  const modal = document.getElementById('bookingModal');
  if (modal) modal.style.display = 'none';
};

window.logoutUser = function() {
  localStorage.removeItem('stackly_user_email');
  localStorage.removeItem('stackly_user_name');
  localStorage.removeItem('stackly_user_initials');
  localStorage.removeItem('stackly_user_role');
  showToast('Logging out from Stackly Care Cloud...');
  setTimeout(() => {
    window.location.href = 'login.html';
  }, 600);
};

/* --------------------------------------------------------------------------
   Toast Notification System
   -------------------------------------------------------------------------- */
function showToast(message) {
  let toast = document.getElementById('stacklyToast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'stacklyToast';
    toast.style.position = 'fixed';
    toast.style.bottom = '30px';
    toast.style.left = '50%';
    toast.style.transform = 'translateX(-50%)';
    toast.style.background = '#111827';
    toast.style.color = '#ffffff';
    toast.style.padding = '14px 24px';
    toast.style.borderRadius = '9999px';
    toast.style.boxShadow = '0 10px 25px rgba(0,0,0,0.3)';
    toast.style.fontSize = '14px';
    toast.style.fontWeight = '600';
    toast.style.zIndex = '100000';
    toast.style.transition = 'all 0.3s ease';
    toast.style.display = 'flex';
    toast.style.alignItems = 'center';
    toast.style.gap = '10px';
    toast.style.border = '1px solid #f59e0b';
    document.body.appendChild(toast);
  }

  toast.innerText = message;
  toast.style.opacity = '1';
  toast.style.pointerEvents = 'auto';

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.pointerEvents = 'none';
  }, 3500);
}

/* --------------------------------------------------------------------------
   Stackly Luxury Preloader Controller
   -------------------------------------------------------------------------- */
let preloaderInitialized = false;
function initPreloader() {
  if (preloaderInitialized) return;
  const preloader = document.getElementById('stacklyPreloader');
  if (!preloader) return;
  preloaderInitialized = true;

  document.body.classList.add('preloader-active');

  const bar = document.getElementById('preloaderProgressBar');
  const status = document.getElementById('preloaderStatusText');

  const statusMessages = [
    'Initializing Care Cloud...',
    'Loading Clinical Profiles...',
    'Synchronizing Health Telemetry...',
    'Connecting 256-Bit SSL Gateway...',
    'Ready.'
  ];

  let progress = 18;
  let msgIndex = 0;
  if (bar) bar.style.width = '18%';

  const progressTimer = setInterval(() => {
    progress += Math.floor(Math.random() * 22) + 12;
    if (progress > 88) progress = 88;
    if (bar) bar.style.width = `${progress}%`;

    msgIndex = Math.min(msgIndex + 1, statusMessages.length - 2);
    if (status && statusMessages[msgIndex]) {
      status.innerText = statusMessages[msgIndex];
    }
  }, 120);

  const completeAndDismiss = () => {
    clearInterval(progressTimer);
    if (bar) bar.style.width = '100%';
    if (status) status.innerText = '✓ Connected';

    setTimeout(() => {
      preloader.classList.add('loaded');
      document.body.classList.remove('preloader-active');
      setTimeout(() => {
        if (preloader.parentNode) preloader.parentNode.removeChild(preloader);
      }, 600);
    }, 320);
  };

  // Dismiss either when window fully loads or after brief minimum show (650ms)
  if (document.readyState === 'complete') {
    setTimeout(completeAndDismiss, 650);
  } else {
    window.addEventListener('load', () => {
      setTimeout(completeAndDismiss, 600);
    });
    // Safety fallback
    setTimeout(completeAndDismiss, 1800);
  }
}

