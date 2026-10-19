# build_all_content.py
# Generates all 14 distinct dashboard pages with 5 UI/UX sections each
from generate_all_dashboards import build_html

# ==============================================================================
# 1. USER: dashboard-user.html (My Health Dashboard)
# ==============================================================================
def create_user_home():
    content = '''
        <!-- 1. Welcome & Quick CTA Row -->
        <div class="dash-welcome-row">
          <div>
            <h1 class="dash-welcome-title">Welcome back, Lingalamanasa123 👋</h1>
            <p class="dash-welcome-sub">Your personal health summary, active clinical care plan, and pregnancy vitals telemetry at a glance.</p>
          </div>
          <a href="user-consultations.html" class="ui-btn-action primary" style="box-shadow:0 4px 14px rgba(245,158,11,0.35);">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
            <span>BOOK NEW CONSULT</span>
          </a>
        </div>

        <!-- 2. Four Quick Action Hubs -->
        <div class="action-cards-grid">
          <a href="user-consultations.html" class="action-card" style="text-decoration:none;">
            <div class="action-card-icon">👩‍⚕️</div>
            <div class="action-card-title">Consult Doctor</div>
            <div class="action-card-desc">Dr. Shilpi Singh (Senior OBG)</div>
          </a>
          <a href="user-maternity.html" class="action-card" style="text-decoration:none;">
            <div class="action-card-icon">🤰</div>
            <div class="action-card-title">Maternity Tracker</div>
            <div class="action-card-desc">Week 24 Day 3 • Trimester 2</div>
          </a>
          <a href="user-scans.html" class="action-card" style="text-decoration:none;">
            <div class="action-card-icon">📡</div>
            <div class="action-card-title">Download 4D Scan</div>
            <div class="action-card-desc">GE Voluson Anomaly Scan PDF</div>
          </a>
          <a href="user-prescriptions.html" class="action-card" style="text-decoration:none;">
            <div class="action-card-icon">💊</div>
            <div class="action-card-title">Pill Reminders</div>
            <div class="action-card-desc">Prenatal Iron &amp; Calcium 2/3</div>
          </a>
        </div>

        <!-- SECTION 1: Real-Time Maternal Health Telemetry KPI Row -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>💓</span> Section 1: Real-Time Maternal Health Telemetry</h3>
              <div class="ui-section-subtitle">Continuous clinical sync from connected Bluetooth vitals monitors</div>
            </div>
            <a href="user-vitals.html" class="ui-btn-action outline">View Detailed Biometrics →</a>
          </div>
          <div class="ui-grid-4">
            <div class="ui-card" style="padding:20px;border-left:4px solid #967BB6;">
              <div style="display:flex;justify-content:space-between;align-items:center;">
                <span style="font-size:12px;font-weight:700;color:#64748b;letter-spacing:0.5px;">BLOOD PRESSURE</span>
                <span class="ui-badge success"><span class="ui-pulse-dot"></span> Optimal</span>
              </div>
              <div style="font-size:28px;font-weight:900;color:#1E0533;margin:12px 0 4px 0;">118/76</div>
              <div style="font-size:12px;color:#64748b;">mmHg • Last synced 9:00 AM</div>
            </div>

            <div class="ui-card" style="padding:20px;border-left:4px solid #967BB6;">
              <div style="display:flex;justify-content:space-between;align-items:center;">
                <span style="font-size:12px;font-weight:700;color:#64748b;letter-spacing:0.5px;">RESTING HEART RATE</span>
                <span class="ui-badge success"><span class="ui-pulse-dot"></span> Normal</span>
              </div>
              <div style="font-size:28px;font-weight:900;color:#1E0533;margin:12px 0 4px 0;">74 bpm</div>
              <div style="font-size:12px;color:#64748b;">Maternal resting telemetry</div>
            </div>

            <div class="ui-card" style="padding:20px;border-left:4px solid #967BB6;">
              <div style="display:flex;justify-content:space-between;align-items:center;">
                <span style="font-size:12px;font-weight:700;color:#64748b;letter-spacing:0.5px;">FETAL KICK COUNTER</span>
                <span class="ui-badge amber">10/10 Reached</span>
              </div>
              <div style="font-size:28px;font-weight:900;color:#1E0533;margin:12px 0 4px 0;">10 Kicks</div>
              <div style="font-size:12px;color:#64748b;">Achieved in 1 hr 12 mins</div>
            </div>

            <div class="ui-card" style="padding:20px;border-left:4px solid #967BB6;">
              <div style="display:flex;justify-content:space-between;align-items:center;">
                <span style="font-size:12px;font-weight:700;color:#64748b;letter-spacing:0.5px;">NEXT CLINICAL VISIT</span>
                <span class="ui-badge blue">Tomorrow</span>
              </div>
              <div style="font-size:24px;font-weight:900;color:#1E0533;margin:12px 0 4px 0;">10:30 AM</div>
              <div style="font-size:12px;color:#64748b;">OPD Chamber 1 • Dr. Shilpi</div>
            </div>
          </div>
        </div>

        <!-- SECTION 2: Active Clinical Protocols & Antenatal Care Plan -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>📋</span> Section 2: Active Clinical Protocols &amp; Antenatal Care Plan</h3>
              <div class="ui-section-subtitle">Evidence-based clinical guidelines supervised by Dr. Shilpi Singh</div>
            </div>
            <button class="ui-btn-action outline" onclick="showToast('Protocol details requested.')">+ Modify Protocol</button>
          </div>
          <div class="ui-interactive-row">
            <div style="display:flex;align-items:center;gap:14px;">
              <span style="font-size:24px;background:#fef3c7;padding:10px;border-radius:12px;">🩺</span>
              <div>
                <h4 style="font-size:15px;font-weight:700;color:#24063E;">Trimester 2 Antenatal Clinical Protocol</h4>
                <p style="font-size:13px;color:#64748b;margin-top:2px;">Assigned by Dr. Shilpi Singh • Review cycle every 3 weeks • Ultrasound scheduled</p>
              </div>
            </div>
            <span class="ui-badge success">Active</span>
          </div>

          <div class="ui-interactive-row">
            <div style="display:flex;align-items:center;gap:14px;">
              <span style="font-size:24px;background:#eff6ff;padding:10px;border-radius:12px;">🩸</span>
              <div>
                <h4 style="font-size:15px;font-weight:700;color:#24063E;">Gestational Blood Glucose (OGTT) 3-Point Profile</h4>
                <p style="font-size:13px;color:#64748b;margin-top:2px;">Fasting: 88 mg/dL | 2-Hr Post-Prandial: 112 mg/dL • Negative for GDM</p>
              </div>
            </div>
            <span class="ui-badge success">Optimal</span>
          </div>

          <div class="ui-interactive-row">
            <div style="display:flex;align-items:center;gap:14px;">
              <span style="font-size:24px;background:#fdf2f8;padding:10px;border-radius:12px;">🍎</span>
              <div>
                <h4 style="font-size:15px;font-weight:700;color:#24063E;">High-Protein Maternal Nutritional Regimen</h4>
                <p style="font-size:13px;color:#64748b;margin-top:2px;">2,200 kcal/day with dietary fiber, iron fortification, and hydration tracker (3.2 L/day)</p>
              </div>
            </div>
            <span class="ui-badge plum">Following</span>
          </div>
        </div>

        <!-- SECTION 3: Today's Medication & Nutrient Tracker -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>💊</span> Section 3: Today's Medication &amp; Nutrient Adherence</h3>
              <div class="ui-section-subtitle">2 of 3 daily prenatal supplements completed today</div>
            </div>
            <a href="user-prescriptions.html" class="ui-btn-action outline">Prescription Details →</a>
          </div>
          <div class="ui-grid-3">
            <div class="ui-card" style="padding:18px;">
              <div style="display:flex;justify-content:space-between;align-items:center;">
                <span class="ui-badge success">✓ Taken (Morning)</span>
                <span style="font-size:11px;color:#64748b;">8:30 AM</span>
              </div>
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;margin:12px 0 4px 0;">Ferrous Ascorbate + Folic Acid</h4>
              <p style="font-size:12.5px;color:#64748b;">1 Tablet post-breakfast with Vitamin C (Orange juice)</p>
            </div>

            <div class="ui-card" style="padding:18px;">
              <div style="display:flex;justify-content:space-between;align-items:center;">
                <span class="ui-badge success">✓ Taken (Afternoon)</span>
                <span style="font-size:11px;color:#64748b;">1:45 PM</span>
              </div>
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;margin:12px 0 4px 0;">Calcium Carbonate + Vit D3 (500mg)</h4>
              <p style="font-size:12.5px;color:#64748b;">1 Tablet after lunch (separated 3 hrs from iron)</p>
            </div>

            <div class="ui-card" style="padding:18px;border:1.5px dashed #967BB6;background:#fffdfa;">
              <div style="display:flex;justify-content:space-between;align-items:center;">
                <span class="ui-badge amber">⏳ Pending Tonight</span>
                <span style="font-size:11px;color:#3B0764;">9:30 PM</span>
              </div>
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;margin:12px 0 4px 0;">Omega-3 DHA (200mg)</h4>
              <p style="font-size:12.5px;color:#64748b;">1 Capsule before bedtime with warm milk</p>
            </div>
          </div>
        </div>

        <!-- SECTION 4: 4D Ultrasound Vault & Laboratory Dossiers -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🔬</span> Section 4: Diagnostic Reports &amp; 4D Ultrasound Vault</h3>
              <div class="ui-section-subtitle">Certified DICOM ultrasound scans signed by Senior Fetal Medicine Sonologists</div>
            </div>
            <a href="user-scans.html" class="ui-btn-action primary">Open Complete Scan Vault →</a>
          </div>
          <div class="ui-grid-3">
            <div class="ui-card" style="padding:18px;">
              <div style="height:140px;border-radius:12px;overflow:hidden;margin-bottom:12px;background:#1E0533;">
                <img src="assets/img/facility-ultrasound.webp" alt="4D Scan Preview" style="width:100%;height:100%;object-fit:cover;">
              </div>
              <div style="display:flex;justify-content:space-between;align-items:center;">
                <span style="font-size:11px;font-weight:700;color:#967BB6;">GE VOLUSON E10</span>
                <span style="font-size:11px;color:#64748b;">Week 20 • TIFFA Scan</span>
              </div>
              <h4 style="font-size:14px;font-weight:800;color:#1E0533;margin:6px 0;">Fetal Anomaly &amp; 4D Facial Reconstruct</h4>
              <button onclick="showToast('Downloading High-Resolution DICOM & PDF Scan...')" class="ui-btn-action outline" style="width:100%;justify-content:center;margin-top:8px;">Download Scan PDF</button>
            </div>

            <div class="ui-card" style="padding:18px;">
              <div style="height:140px;border-radius:12px;overflow:hidden;margin-bottom:12px;background:#1E0533;">
                <img src="assets/img/service-ultrasound-real.webp" alt="Color Doppler Preview" style="width:100%;height:100%;object-fit:cover;">
              </div>
              <div style="display:flex;justify-content:space-between;align-items:center;">
                <span style="font-size:11px;font-weight:700;color:#967BB6;">COLOR DOPPLER</span>
                <span style="font-size:11px;color:#64748b;">Week 24 • Fetal Growth</span>
              </div>
              <h4 style="font-size:14px;font-weight:800;color:#1E0533;margin:6px 0;">Uterine &amp; Umbilical Artery Flow</h4>
              <button onclick="showToast('Downloading Doppler Vascular Telemetry Report...')" class="ui-btn-action outline" style="width:100%;justify-content:center;margin-top:8px;">Download Flow Report</button>
            </div>

            <div class="ui-card" style="padding:18px;">
              <div style="height:140px;border-radius:12px;overflow:hidden;margin-bottom:12px;background:#F3E8FF;display:flex;align-items:center;justify-content:center;font-size:42px;">
                🧬
              </div>
              <div style="display:flex;justify-content:space-between;align-items:center;">
                <span style="font-size:11px;font-weight:700;color:#967BB6;">GENETICS</span>
                <span style="font-size:11px;color:#64748b;">Week 12 • Biochemical</span>
              </div>
              <h4 style="font-size:14px;font-weight:800;color:#1E0533;margin:6px 0;">NIPT &amp; Dual Marker Screening</h4>
              <button onclick="showToast('Downloading Genetic Screening Certificate...')" class="ui-btn-action outline" style="width:100%;justify-content:center;margin-top:8px;">Download NIPT Dossier</button>
            </div>
          </div>
        </div>

        <!-- SECTION 5: Instant Doctor Connect & Clinical Emergency SOS -->
        <div class="ui-section-card" style="background:linear-gradient(135deg, #ffffff 0%, #fff7ed 100%);border:1px solid #fed7aa;">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span style="color:#3B0764;">🚨</span> Section 5: Instant Doctor Connect &amp; 24×7 Maternity SOS</h3>
              <div class="ui-section-subtitle">Direct hotline to Salem triage team and Dr. Shilpi Singh's emergency team</div>
            </div>
            <span class="ui-badge amber"><span class="ui-pulse-dot danger"></span> Emergency Ready</span>
          </div>
          <div class="ui-grid-3">
            <div class="ui-card" style="padding:20px;background:#ffffff;">
              <div style="font-size:32px;margin-bottom:8px;">📞</div>
              <h4 style="font-size:16px;font-weight:800;color:#1E0533;">24×7 Maternity SOS Hotline</h4>
              <p style="font-size:13px;color:#64748b;margin:6px 0 14px 0;">Immediate connection to labor ward triage and duty gynecologist.</p>
              <a href="tel:+917010792745" class="ui-btn-action primary" style="width:100%;justify-content:center;">Call +91 70107 92745</a>
            </div>

            <div class="ui-card" style="padding:20px;background:#ffffff;">
              <div style="font-size:32px;margin-bottom:8px;">💬</div>
              <h4 style="font-size:16px;font-weight:800;color:#1E0533;">Nurse Triage Direct Chat</h4>
              <p style="font-size:13px;color:#64748b;margin:6px 0 14px 0;">Ask quick clinical questions about symptoms, medications, or diet.</p>
              <button onclick="showToast('Opening Live Clinical Nurse Triage Session...')" class="ui-btn-action outline" style="width:100%;justify-content:center;">Start Nurse Chat</button>
            </div>

            <div class="ui-card" style="padding:20px;background:#ffffff;">
              <div style="font-size:32px;margin-bottom:8px;">🚑</div>
              <h4 style="font-size:16px;font-weight:800;color:#1E0533;">Hospital Ambulance Dispatch</h4>
              <p style="font-size:13px;color:#64748b;margin:6px 0 14px 0;">Equipped with mobile fetal monitoring and resuscitation gear.</p>
              <a href="tel:+919555334107" class="ui-btn-action plum" style="width:100%;justify-content:center;">Dispatch Ambulance</a>
            </div>
          </div>
        </div>
    '''
    return build_html("Patient Care Dashboard", "Stackly Women's Health Center Patient Portal", "dashboard-user.html", False, content)

print("create_user_home defined.")
