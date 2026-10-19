# build_admin_pages.py
# Generates all 7 Admin Dashboard pages with 5 UI/UX sections each
# Specifically tailored for Women's Health Center Hospital Administration
from generate_all_dashboards import build_html

# ==============================================================================
# 1. ADMIN: dashboard-admin.html (Executive Overview)
# ==============================================================================
def create_admin_home():
    content = '''
        <div class="dash-welcome-row">
          <div>
            <h1 class="dash-welcome-title">Hospital Executive Cockpit 📊</h1>
            <p class="dash-welcome-sub">Salem Women's Health Center operational census, OT status, NICU telemetry, and clinical throughput.</p>
          </div>
          <div style="display:flex;gap:12px;flex-wrap:wrap;">
            <button onclick="showToast('Hospital census report exported as encrypted CSV/PDF.')" class="ui-btn-action outline">Export Census</button>
            <a href="admin-queue.html" class="ui-btn-action primary">+ CALL NEXT OPD TOKEN</a>
          </div>
        </div>

        <!-- Section 1: Live Operational Telemetry KPIs -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🏥</span> Section 1: Hospital Operational Telemetry &amp; Bed Census</h3>
              <div class="ui-section-subtitle">Real-time telemetry across Salem Main Center and Outpatient Chambers</div>
            </div>
            <span class="ui-badge success"><span class="ui-pulse-dot"></span> All Theaters Online</span>
          </div>
          <div class="ui-grid-4">
            <div class="ui-card" style="padding:20px;border-left:4px solid #967BB6;">
              <span style="font-size:12px;font-weight:700;color:#64748b;">ACTIVE INPATIENTS</span>
              <div style="font-size:32px;font-weight:900;color:#1E0533;margin:8px 0 2px 0;">38 / 48</div>
              <span style="font-size:12px;color:#967BB6;">79% Bed Occupancy (Healthy)</span>
            </div>
            <div class="ui-card" style="padding:20px;border-left:4px solid #967BB6;">
              <span style="font-size:12px;font-weight:700;color:#64748b;">NORMAL DELIVERY RATE</span>
              <div style="font-size:32px;font-weight:900;color:#1E0533;margin:8px 0 2px 0;">90.4 %</div>
              <span style="font-size:12px;color:#3B0764;">Physiological birth priority</span>
            </div>
            <div class="ui-card" style="padding:20px;border-left:4px solid #967BB6;">
              <span style="font-size:12px;font-weight:700;color:#64748b;">LEVEL-3 NICU CENSUS</span>
              <div style="font-size:32px;font-weight:900;color:#1E0533;margin:8px 0 2px 0;">8 / 12</div>
              <span style="font-size:12px;color:#967BB6;">4 Ventilated / 4 Phototherapy</span>
            </div>
            <div class="ui-card" style="padding:20px;border-left:4px solid #967BB6;">
              <span style="font-size:12px;font-weight:700;color:#64748b;">EMERGENCY SOS READINESS</span>
              <div style="font-size:32px;font-weight:900;color:#1E0533;margin:8px 0 2px 0;">&lt; 2.1 Min</div>
              <span style="font-size:12px;color:#967BB6;">Crash C-Section Response Time</span>
            </div>
          </div>
        </div>

        <!-- Section 2: Doctor Chamber Queue Monitor -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>👩‍⚕️</span> Section 2: Specialist Chamber Live OPD Status</h3>
              <div class="ui-section-subtitle">Real-time patient flow across 4 active consultation chambers</div>
            </div>
            <a href="admin-queue.html" class="ui-btn-action outline">Manage Live Queue Board →</a>
          </div>
          <div class="ui-grid-4">
            <div class="ui-card" style="padding:18px;">
              <div style="display:flex;justify-content:space-between;">
                <span class="ui-badge success">Chamber 1 Active</span>
                <span style="font-size:11px;font-weight:700;color:#967BB6;">Token #11</span>
              </div>
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;margin:10px 0 2px 0;">Dr. Shilpi Singh</h4>
              <p style="font-size:12px;color:#64748b;">Obstetrics &amp; Gynaecology Surgery</p>
              <div style="margin-top:10px;font-size:12px;color:#334155;">Queue: <strong>14 Patients</strong> (Est wait 18m)</div>
            </div>

            <div class="ui-card" style="padding:18px;">
              <div style="display:flex;justify-content:space-between;">
                <span class="ui-badge success">Chamber 2 Active</span>
                <span style="font-size:11px;font-weight:700;color:#967BB6;">Token #08</span>
              </div>
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;margin:10px 0 2px 0;">Dr. Ananya Sen</h4>
              <p style="font-size:12px;color:#64748b;">Reproductive Medicine &amp; Laparoscopy</p>
              <div style="margin-top:10px;font-size:12px;color:#334155;">Queue: <strong>8 Patients</strong> (Est wait 12m)</div>
            </div>

            <div class="ui-card" style="padding:18px;">
              <div style="display:flex;justify-content:space-between;">
                <span class="ui-badge success">Chamber 3 Active</span>
                <span style="font-size:11px;font-weight:700;color:#967BB6;">Token #06</span>
              </div>
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;margin:10px 0 2px 0;">Dr. Meera Nair</h4>
              <p style="font-size:12px;color:#64748b;">Fetal Medicine &amp; 4D Sonology</p>
              <div style="margin-top:10px;font-size:12px;color:#334155;">Queue: <strong>6 Patients</strong> (Ultrasound ongoing)</div>
            </div>

            <div class="ui-card" style="padding:18px;">
              <div style="display:flex;justify-content:space-between;">
                <span class="ui-badge amber">Chamber 4</span>
                <span style="font-size:11px;font-weight:700;color:#3B0764;">Token #04</span>
              </div>
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;margin:10px 0 2px 0;">Dr. Priya Sharma</h4>
              <p style="font-size:12px;color:#64748b;">Adolescent &amp; Hormonal Care</p>
              <div style="margin-top:10px;font-size:12px;color:#334155;">Queue: <strong>5 Patients</strong> (Est wait 10m)</div>
            </div>
          </div>
        </div>

        <!-- Section 3: OT & Emergency Laparoscopy Status -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🔬</span> Section 3: Modular Surgical Theaters Live Readiness</h3>
              <div class="ui-section-subtitle">Laminar airflow, HEPA filter positive pressure, and autoclave batch sterility</div>
            </div>
            <a href="admin-surgery.html" class="ui-btn-action outline">View Complete Surgery Roster →</a>
          </div>
          <div class="ui-grid-3">
            <div class="ui-card" style="padding:18px;border-top:4px solid #3B0764;">
              <div style="display:flex;justify-content:space-between;">
                <span style="font-weight:800;color:#1E0533;">OT 1 — MAJOR OBSTETRICS</span>
                <span class="ui-badge amber"><span class="ui-pulse-dot danger"></span> In Surgery</span>
              </div>
              <div style="margin:10px 0;font-size:13.5px;color:#334155;">
                Procedure: <strong>Elective Lower Segment C-Section (LSCS)</strong><br>
                Surgeon: <strong>Dr. Shilpi Singh</strong> • Anesthetist: Dr. Raman
              </div>
              <div style="font-size:12px;color:#64748b;">Time Elapsed: 32 mins • Fetal Delivery Completed • Baby in NICU care</div>
            </div>

            <div class="ui-card" style="padding:18px;border-top:4px solid #967BB6;">
              <div style="display:flex;justify-content:space-between;">
                <span style="font-weight:800;color:#1E0533;">OT 2 — MODULAR LAPAROSCOPY</span>
                <span class="ui-badge success">Ready for Prep</span>
              </div>
              <div style="margin:10px 0;font-size:13.5px;color:#334155;">
                Procedure: <strong>Keyhole Laparoscopic Cystectomy (7cm Dermoid)</strong><br>
                Lead Surgeon: <strong>Dr. Ananya Sen</strong> • Start: 2:00 PM
              </div>
              <div style="font-size:12px;color:#64748b;">Laminar Airflow: Class 100 • Sterile Batch #B-48192 Validated</div>
            </div>

            <div class="ui-card" style="padding:18px;border-top:4px solid #967BB6;">
              <div style="display:flex;justify-content:space-between;">
                <span style="font-weight:800;color:#1E0533;">OT 3 — MINOR DAYCARE &amp; D&amp;C</span>
                <span class="ui-badge blue">Standby Available</span>
              </div>
              <div style="margin:10px 0;font-size:13.5px;color:#334155;">
                Procedure: <strong>Hysteroscopic Endometrial Biopsy</strong><br>
                Scheduled: 4:30 PM • Sterilization turnaround complete
              </div>
              <div style="font-size:12px;color:#64748b;">Crash Cart Checked • O-Negative Blood Bank units reserved</div>
            </div>
          </div>
        </div>

        <!-- Section 4: Bed Occupancy & Inpatient Ward Census -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🛌</span> Section 4: Maternity Ward &amp; LDRP Suite Census</h3>
              <div class="ui-section-subtitle">Real-time room occupancy and maternal recovery status</div>
            </div>
            <a href="admin-admissions.html" class="ui-btn-action outline">Manage Ward Admissions →</a>
          </div>
          <div class="ui-grid-4">
            <div class="ui-card" style="padding:16px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">LDRP LUXURY SUITES</span>
              <div style="font-size:26px;font-weight:900;color:#1E0533;margin:6px 0;">7 / 8 Occupied</div>
              <span style="font-size:12px;color:#967BB6;">Suite 108 Available</span>
            </div>
            <div class="ui-card" style="padding:16px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">POST-OP DELUXE ROOMS</span>
              <div style="font-size:26px;font-weight:900;color:#1E0533;margin:6px 0;">12 / 14 Occupied</div>
              <span style="font-size:12px;color:#967BB6;">2 Discharges at 3 PM</span>
            </div>
            <div class="ui-card" style="padding:16px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">SEMI-PRIVATE WARDS</span>
              <div style="font-size:26px;font-weight:900;color:#1E0533;margin:6px 0;">11 / 14 Occupied</div>
              <span style="font-size:12px;color:#967BB6;">3 Beds Available</span>
            </div>
            <div class="ui-card" style="padding:16px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">LEVEL-3 NICU CRIBS</span>
              <div style="font-size:26px;font-weight:900;color:#1E0533;margin:6px 0;">8 / 12 Occupied</div>
              <span style="font-size:12px;color:#967BB6;">4 Incubators Standby</span>
            </div>
          </div>
        </div>

        <!-- Section 5: TPA Cashless Insurance & Financial Telemetry -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>💳</span> Section 5: Hospital Daily Financial Telemetry &amp; TPA Claims</h3>
              <div class="ui-section-subtitle">Real-time collections, pre-authorization settlements, and cashless approvals</div>
            </div>
            <a href="admin-billing.html" class="ui-btn-action primary">Open Financial Ledger →</a>
          </div>
          <div class="ui-grid-4">
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">TODAY'S COLLECTIONS</span>
              <div style="font-size:26px;font-weight:900;color:#967BB6;margin:6px 0;">₹ 3,42,800</div>
              <span style="font-size:12px;color:#967BB6;">+14.2% vs yesterday</span>
            </div>
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">CASHLESS TPA APPROVED</span>
              <div style="font-size:26px;font-weight:900;color:#1E0533;margin:6px 0;">₹ 2,15,000</div>
              <span style="font-size:12px;color:#64748b;">Star Health, HDFC, MediBuddy</span>
            </div>
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">PHARMACY POS REVENUE</span>
              <div style="font-size:26px;font-weight:900;color:#1E0533;margin:6px 0;">₹ 78,400</div>
              <span style="font-size:12px;color:#64748b;">114 Prescriptions Filled</span>
            </div>
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">PENDING PRE-AUTH CLAIMS</span>
              <div style="font-size:26px;font-weight:900;color:#967BB6;margin:6px 0;">4 Claims</div>
              <span style="font-size:12px;color:#3B0764;">Avg Turnaround: 24 mins</span>
            </div>
          </div>
        </div>
    '''
    return build_html("Hospital Admin Cockpit", "Executive Healthcare Administration Telemetry", "dashboard-admin.html", True, content)


# ==============================================================================
# 2. ADMIN: admin-queue.html (OPD Token Queue)
# ==============================================================================
def create_admin_queue():
    content = '''
        <div class="dash-welcome-row">
          <div>
            <h1 class="dash-welcome-title">OPD Token Queue &amp; Chamber Dispatch 🎫</h1>
            <p class="dash-welcome-sub">Live token display, doctor chamber triage, walk-in registration, and patient flow management.</p>
          </div>
          <button onclick="showToast('Issued Emergency Walk-In Token #15 to Chamber 1.')" class="ui-btn-action primary">
            <span>+ ISSUE EMERGENCY TOKEN</span>
          </button>
        </div>

        <!-- Section 1: Live OPD Token Broadcast Board -->
        <div class="ui-section-card" style="background:#1E0533;color:#ffffff;border:none;">
          <div class="ui-section-title-wrap" style="border-bottom:1px solid #24063E;">
            <div class="ui-section-title-group">
              <h3 style="color:#ffffff;"><span>📺</span> Section 1: Live OPD Token Public Broadcast Display</h3>
              <div class="ui-section-subtitle" style="color:#94a3b8;">Central waiting lounge LED screen feed</div>
            </div>
            <span class="ui-badge amber"><span class="ui-pulse-dot amber"></span> Broadcasting Live</span>
          </div>
          <div class="ui-grid-4">
            <div style="background:#24063E;padding:20px;border-radius:14px;border:1px solid #334155;text-align:center;">
              <div style="font-size:12px;color:#94a3b8;font-weight:700;">CHAMBER 1 (DR. SHILPI)</div>
              <div style="font-size:48px;font-weight:900;color:#967BB6;margin:8px 0;">#11</div>
              <div style="font-size:13px;color:#967BB6;font-weight:700;">IN CONSULTATION</div>
            </div>
            <div style="background:#24063E;padding:20px;border-radius:14px;border:1px solid #334155;text-align:center;">
              <div style="font-size:12px;color:#94a3b8;font-weight:700;">CHAMBER 2 (DR. ANANYA)</div>
              <div style="font-size:48px;font-weight:900;color:#967BB6;margin:8px 0;">#08</div>
              <div style="font-size:13px;color:#967BB6;font-weight:700;">IN CONSULTATION</div>
            </div>
            <div style="background:#24063E;padding:20px;border-radius:14px;border:1px solid #334155;text-align:center;">
              <div style="font-size:12px;color:#94a3b8;font-weight:700;">CHAMBER 3 (DR. MEERA)</div>
              <div style="font-size:48px;font-weight:900;color:#967BB6;margin:8px 0;">#06</div>
              <div style="font-size:13px;color:#967BB6;font-weight:700;">4D SCANNING</div>
            </div>
            <div style="background:#24063E;padding:20px;border-radius:14px;border:1px solid #334155;text-align:center;">
              <div style="font-size:12px;color:#94a3b8;font-weight:700;">CHAMBER 4 (DR. PRIYA)</div>
              <div style="font-size:48px;font-weight:900;color:#967BB6;margin:8px 0;">#04</div>
              <div style="font-size:13px;color:#967BB6;font-weight:700;">IN CONSULTATION</div>
            </div>
          </div>
        </div>

        <!-- Section 2: Specialist Chamber Allocation & Daily Duty Roster -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>👩‍⚕️</span> Section 2: Specialist Chamber Allocation &amp; Session Timers</h3>
              <div class="ui-section-subtitle">Real-time throughput and average consultation duration</div>
            </div>
          </div>
          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;">Chamber 1 — Dr. Shilpi Singh (Obstetrics Director)</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">Currently with: Priya Sundaram • Duration: 14 mins • 3 High-Risk Pregnancies queued</p>
            </div>
            <div style="display:flex;gap:10px;">
              <button onclick="showToast('Calling Next Token in Chamber 1...')" class="ui-btn-action primary">Call Next Token</button>
            </div>
          </div>

          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;">Chamber 2 — Dr. Ananya Sen (Laparoscopy &amp; Infertility)</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">Currently with: Malathi Venkat • Duration: 11 mins • Pre-op counselling</p>
            </div>
            <div style="display:flex;gap:10px;">
              <button onclick="showToast('Calling Next Token in Chamber 2...')" class="ui-btn-action outline">Call Next Token</button>
            </div>
          </div>
        </div>

        <!-- Section 3: Obstetric Triage & Emergency Fast-Track Engine -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🚨</span> Section 3: Obstetric Triage &amp; Emergency Walk-In Prioritizer</h3>
              <div class="ui-section-subtitle">MEOWS (Modified Early Obstetric Warning Score) automated sorting</div>
            </div>
            <span class="ui-badge success">Zero Critical Delays</span>
          </div>
          <div class="ui-interactive-row" style="background:#fff7ed;border-color:#fed7aa;">
            <div>
              <h4 style="font-size:15px;font-weight:800;color:#9a3412;">Priority Triage #1: Labor Pain (38 Weeks) • Cervix 4cm Dilated</h4>
              <p style="font-size:13px;color:#3B0764;margin-top:2px;">Patient: Kavitha R. • Transferred immediately to LDRP Suite 104 • Dr. Shilpi notified</p>
            </div>
            <span class="ui-badge amber">Fast-Tracked to LDRP</span>
          </div>
        </div>

        <!-- Section 4: Token Management & Next Patient Trigger -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🕹️</span> Section 4: Nurse Reception Token Control Console</h3>
              <div class="ui-section-subtitle">Reassign chambers, skip absent tokens, or hold patient for lab results</div>
            </div>
          </div>
          <div class="ui-grid-3">
            <div class="ui-card" style="padding:18px;">
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;margin-bottom:8px;">Recall Token #10</h4>
              <p style="font-size:12.5px;color:#64748b;margin-bottom:12px;">Sound announcement bell in Main Waiting Area for Token #10.</p>
              <button onclick="showToast('Announcement triggered: Token #10 please proceed to Chamber 1.')" class="ui-btn-action outline" style="width:100%;justify-content:center;">Sound Recall Chime</button>
            </div>

            <div class="ui-card" style="padding:18px;">
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;margin-bottom:8px;">Transfer Token to Chamber 3</h4>
              <p style="font-size:12.5px;color:#64748b;margin-bottom:12px;">Route patient directly to Dr. Meera for urgent 4D fetal scan.</p>
              <button onclick="showToast('Token reassigned to Ultrasound Chamber 3.')" class="ui-btn-action outline" style="width:100%;justify-content:center;">Transfer to Scan</button>
            </div>

            <div class="ui-card" style="padding:18px;">
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;margin-bottom:8px;">Print Physical OPD Slip</h4>
              <p style="font-size:12.5px;color:#64748b;margin-bottom:12px;">Thermal receipt printer at Reception Desk 1.</p>
              <button onclick="showToast('Thermal OPD slip printed on Counter 1.')" class="ui-btn-action primary" style="width:100%;justify-content:center;">Print Token Slip</button>
            </div>
          </div>
        </div>

        <!-- Section 5: OPD Daily Analytics & Peak Hours Heatmap -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>📈</span> Section 5: OPD Patient Volume Heatmap &amp; Turnaround Times</h3>
              <div class="ui-section-subtitle">Average wait time today: 16.4 mins (Goal &lt; 20 mins)</div>
            </div>
            <span class="ui-badge success">Target Met</span>
          </div>
          <div class="ui-grid-4">
            <div class="ui-card" style="padding:16px;text-align:center;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">TOTAL OPD PATIENTS</span>
              <div style="font-size:28px;font-weight:900;color:#1E0533;margin:6px 0;">86 Today</div>
              <span style="font-size:12px;color:#967BB6;">54 Completed • 32 Active</span>
            </div>
            <div class="ui-card" style="padding:16px;text-align:center;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">AVG CONSULTATION TIME</span>
              <div style="font-size:28px;font-weight:900;color:#1E0533;margin:6px 0;">14.2 Mins</div>
              <span style="font-size:12px;color:#64748b;">Unhurried clinical care</span>
            </div>
            <div class="ui-card" style="padding:16px;text-align:center;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">PEAK RUSH HOURS</span>
              <div style="font-size:24px;font-weight:900;color:#967BB6;margin:8px 0;">10am – 12pm</div>
              <span style="font-size:12px;color:#64748b;">All 4 Chambers Staffed</span>
            </div>
            <div class="ui-card" style="padding:16px;text-align:center;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">PATIENT SATISFACTION</span>
              <div style="font-size:28px;font-weight:900;color:#967BB6;margin:6px 0;">99.2 %</div>
              <span style="font-size:12px;color:#967BB6;">Google &amp; Tablet Feedback</span>
            </div>
          </div>
        </div>
    '''
    return build_html("OPD Token Queue", "Doctor Chamber Dispatch & Queue System", "admin-queue.html", True, content)


# ==============================================================================
# 3. ADMIN: admin-surgery.html (OT & Surgery Roster)
# ==============================================================================
def create_admin_surgery():
    content = '''
        <div class="dash-welcome-row">
          <div>
            <h1 class="dash-welcome-title">OT &amp; Surgical Theater Roster 🔬</h1>
            <p class="dash-welcome-sub">Modular operating theaters, keyhole laparoscopy scheduling, and sterile laminar flow sentinels.</p>
          </div>
          <button onclick="showToast('Opening Emergency Surgical Roster Scheduler...')" class="ui-btn-action primary">
            <span>+ SCHEDULE SURGERY</span>
          </button>
        </div>

        <!-- Section 1: Modular Surgical Suites Operational Status -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🛡️</span> Section 1: Modular OT Sterility &amp; Positive Pressure Sentinel</h3>
              <div class="ui-section-subtitle">Class 100 laminar airflow continuous bacteriological monitoring</div>
            </div>
            <span class="ui-badge success">All 3 Theaters Certified</span>
          </div>
          <div class="ui-grid-3">
            <div class="ui-card" style="padding:18px;">
              <div style="display:flex;justify-content:space-between;">
                <h4 style="font-size:16px;font-weight:800;color:#1E0533;">OT 1 — Major Obstetric</h4>
                <span class="ui-badge amber">In Procedure</span>
              </div>
              <div style="font-size:13px;color:#64748b;margin:10px 0;">Temperature: 20.4°C • Humidity: 48% • Positive Pressure: +22 Pa</div>
              <span class="ui-badge success">HEPA Filtration: 99.997%</span>
            </div>

            <div class="ui-card" style="padding:18px;">
              <div style="display:flex;justify-content:space-between;">
                <h4 style="font-size:16px;font-weight:800;color:#1E0533;">OT 2 — Laparoscopy Modular</h4>
                <span class="ui-badge success">Sterile &amp; Ready</span>
              </div>
              <div style="font-size:13px;color:#64748b;margin:10px 0;">Temperature: 19.8°C • Humidity: 46% • Positive Pressure: +24 Pa</div>
              <span class="ui-badge success">HEPA Filtration: 99.997%</span>
            </div>

            <div class="ui-card" style="padding:18px;">
              <div style="display:flex;justify-content:space-between;">
                <h4 style="font-size:16px;font-weight:800;color:#1E0533;">OT 3 — Daycare &amp; Hysteroscopy</h4>
                <span class="ui-badge blue">Standby Available</span>
              </div>
              <div style="font-size:13px;color:#64748b;margin:10px 0;">Temperature: 21.0°C • Humidity: 50% • Positive Pressure: +20 Pa</div>
              <span class="ui-badge success">HEPA Filtration: 99.997%</span>
            </div>
          </div>
        </div>

        <!-- Section 2: Day's Surgical Roster & Emergency C-Section Schedule -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>📋</span> Section 2: Day's Master Surgical Roster</h3>
              <div class="ui-section-subtitle">Surgeon allocation, anesthetist assignment, and scrub nursing personnel</div>
            </div>
          </div>
          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;">09:30 AM — Lower Segment Cesarean Section (LSCS) [OT 1]</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">Patient: Deepa Saravanan (39 Weeks) • Lead Surgeon: Dr. Shilpi Singh • Anesthetist: Dr. Raman • Status: Baby delivered, Closing</p>
            </div>
            <span class="ui-badge amber">In Progress</span>
          </div>

          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;">02:00 PM — Laparoscopic Ovarian Cystectomy &amp; Endometriosis Clearance [OT 2]</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">Patient: Radhika M. (32 Yrs) • Lead Surgeon: Dr. Ananya Sen • Pre-op anesthesia clearance: Complete</p>
            </div>
            <span class="ui-badge blue">Scheduled</span>
          </div>

          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;">04:30 PM — Diagnostic Hysteroscopy &amp; Polypectomy [OT 3]</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">Patient: Shanthi K. • Lead Surgeon: Dr. Priya Sharma • Daycare discharge planned same evening</p>
            </div>
            <span class="ui-badge blue">Scheduled</span>
          </div>
        </div>

        <!-- Section 3: Laparoscopic Tower & Electrosurgical Device Sentinel -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🔌</span> Section 3: Advanced Electrosurgical &amp; HD Video Tower Health</h3>
              <div class="ui-section-subtitle">Ultrasonic dissection, CO2 pneumoperitoneum, and 4K optical endoscopy monitors</div>
            </div>
            <span class="ui-badge success">All Equipment Calibrated</span>
          </div>
          <div class="ui-grid-3">
            <div class="ui-card" style="padding:18px;">
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;">Ethicon Harmonic Scalpel Gen11</h4>
              <p style="font-size:12.5px;color:#64748b;margin:6px 0 10px 0;">Ultrasonic tissue coagulator. Handpiece tested and calibrated today 8:00 AM.</p>
              <span class="ui-badge success">Ready for OT 2</span>
            </div>
            <div class="ui-card" style="padding:18px;">
              <div style="font-size:15px;font-weight:800;color:#1E0533;">Olympus Visera 4K Laparoscopy</div>
              <p style="font-size:12.5px;color:#64748b;margin:6px 0 10px 0;">Dual surgical HD monitors. Zero latency fiber optic video transmission.</p>
              <span class="ui-badge success">Tested Optimal</span>
            </div>
            <div class="ui-card" style="padding:18px;">
              <div style="font-size:15px;font-weight:800;color:#1E0533;">Karl Storz High-Flow Insufflator</div>
              <p style="font-size:12.5px;color:#64748b;margin:6px 0 10px 0;">Automatic heated CO2 gas supply with smoke evacuation integration.</p>
              <span class="ui-badge success">Tanks 100% Full</span>
            </div>
          </div>
        </div>

        <!-- Section 4: Emergency Crash C-Section Protocol Checklist -->
        <div class="ui-section-card" style="background:#fff7ed;border-color:#fed7aa;">
          <div class="ui-section-title-wrap" style="border-color:#fed7aa;">
            <div class="ui-section-title-group">
              <h3 style="color:#9a3412;"><span>⚡</span> Section 4: Emergency Obstetric Crash C-Section Readiness (Decision-to-Incision &lt; 15 mins)</h3>
              <div class="ui-section-subtitle" style="color:#3B0764;">24×7 Rapid Response for fetal distress, placental abruption, or cord prolapse</div>
            </div>
            <span class="ui-badge amber">Code Pink Rapid Ready</span>
          </div>
          <div class="ui-interactive-row" style="background:#ffffff;">
            <div>
              <h4 style="font-size:15px;font-weight:700;color:#24063E;">Obstetric Blood Bank Cross-Match Standby</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">4 Units O-Negative Uncrossmatched &amp; 6 Units Fresh Frozen Plasma (FFP) thawed in Blood Bank</p>
            </div>
            <span class="ui-badge success">Standby Verified</span>
          </div>
        </div>

        <!-- Section 5: Surgical Audit & Zero-Infection Compliance Tracker -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>📊</span> Section 5: Surgical Outcomes &amp; Infection Control Audit</h3>
              <div class="ui-section-subtitle">Salem Center Surgical Site Infection (SSI) Rate: 0.00% across last 1,450 cases</div>
            </div>
            <span class="ui-badge success">NABH Benchmarked</span>
          </div>
          <div class="ui-grid-4">
            <div class="ui-card" style="padding:16px;text-align:center;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">TOTAL SURGERIES (2026)</span>
              <div style="font-size:28px;font-weight:900;color:#1E0533;margin:6px 0;">418 Cases</div>
              <span style="font-size:12px;color:#967BB6;">100% Survival Rate</span>
            </div>
            <div class="ui-card" style="padding:16px;text-align:center;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">LAPAROSCOPY SUCCESS</span>
              <div style="font-size:28px;font-weight:900;color:#967BB6;margin:6px 0;">99.8 %</div>
              <span style="font-size:12px;color:#64748b;">Zero open conversions</span>
            </div>
            <div class="ui-card" style="padding:16px;text-align:center;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">AVG OT TURNAROUND</span>
              <div style="font-size:28px;font-weight:900;color:#1E0533;margin:6px 0;">18 Mins</div>
              <span style="font-size:12px;color:#967BB6;">Rapid sterile cycle</span>
            </div>
            <div class="ui-card" style="padding:16px;text-align:center;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">SURGICAL SITE INFECTION</span>
              <div style="font-size:28px;font-weight:900;color:#967BB6;margin:6px 0;">0.00 %</div>
              <span style="font-size:12px;color:#967BB6;">NABH Standard Met</span>
            </div>
          </div>
        </div>
    '''
    return build_html("OT & Surgery Roster", "Modular Surgical Theaters & Laparoscopy Roster", "admin-surgery.html", True, content)


# ==============================================================================
# 4. ADMIN: admin-admissions.html (Bed Occupancy & Maternity Wards)
# ==============================================================================
def create_admin_admissions():
    content = '''
        <div class="dash-welcome-row">
          <div>
            <h1 class="dash-welcome-title">Bed Occupancy &amp; Maternity Ward Census 🏥</h1>
            <p class="dash-welcome-sub">Luxury LDRP birthing suites, post-operative wards, and patient admission workflow.</p>
          </div>
          <button onclick="showToast('Opening Direct Ward Admission Form...')" class="ui-btn-action primary">
            <span>+ ADMIT NEW PATIENT</span>
          </button>
        </div>

        <!-- Section 1: Real-Time Bed Occupancy Census -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🛌</span> Section 1: Real-Time Hospital Bed Census (Total 48 Beds)</h3>
              <div class="ui-section-subtitle">Real-time status of birthing suites, recovery wards, and infant cribs</div>
            </div>
            <span class="ui-badge success">10 Beds Available</span>
          </div>
          <div class="ui-grid-4">
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">TOTAL ADMISSIONS</span>
              <div style="font-size:32px;font-weight:900;color:#1E0533;margin:6px 0;">38 Beds</div>
              <span style="font-size:12px;color:#967BB6;">79% Capacity Utilization</span>
            </div>
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">LDRP SUITES OCCUPIED</span>
              <div style="font-size:32px;font-weight:900;color:#3B0764;margin:6px 0;">7 / 8</div>
              <span style="font-size:12px;color:#3B0764;">1 Ready for Sanitization</span>
            </div>
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">DISCHARGES SCHEDULED</span>
              <div style="font-size:32px;font-weight:900;color:#967BB6;margin:6px 0;">4 Today</div>
              <span style="font-size:12px;color:#967BB6;">All pediatric clearances done</span>
            </div>
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">AVG HOSPITAL STAY</span>
              <div style="font-size:32px;font-weight:900;color:#1E0533;margin:6px 0;">3.2 Days</div>
              <span style="font-size:12px;color:#967BB6;">Fast maternal recovery</span>
            </div>
          </div>
        </div>

        <!-- Section 2: Ward Breakdown & LDRP Suites Allocation -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🛋️</span> Section 2: Luxury LDRP Birthing Suites Status Board</h3>
              <div class="ui-section-subtitle">Single-room labor, delivery, recovery, and postpartum suites</div>
            </div>
          </div>
          <div class="ui-grid-4">
            <div class="ui-card" style="padding:16px;border-left:4px solid #3B0764;">
              <div style="display:flex;justify-content:space-between;">
                <strong>SUITE 101</strong>
                <span class="ui-badge amber">Active Labor</span>
              </div>
              <p style="font-size:13px;color:#334155;margin:8px 0 4px 0;">Anitha R. (39w 2d)</p>
              <div style="font-size:12px;color:#64748b;">Dr. Shilpi Singh • Nurse Mary</div>
            </div>

            <div class="ui-card" style="padding:16px;border-left:4px solid #967BB6;">
              <div style="display:flex;justify-content:space-between;">
                <strong>SUITE 102</strong>
                <span class="ui-badge success">Postpartum Day 1</span>
              </div>
              <p style="font-size:13px;color:#334155;margin:8px 0 4px 0;">Sunitha M. (Baby Girl 3.1kg)</p>
              <div style="font-size:12px;color:#64748b;">Normal Delivery • Lactation ok</div>
            </div>

            <div class="ui-card" style="padding:16px;border-left:4px solid #967BB6;">
              <div style="display:flex;justify-content:space-between;">
                <strong>SUITE 103</strong>
                <span class="ui-badge success">Postpartum Day 2</span>
              </div>
              <p style="font-size:13px;color:#334155;margin:8px 0 4px 0;">Meenakshi K. (Baby Boy)</p>
              <div style="font-size:12px;color:#64748b;">Discharge planned tomorrow</div>
            </div>

            <div class="ui-card" style="padding:16px;border-left:4px solid #967BB6;background:#FAF9F5;">
              <div style="display:flex;justify-content:space-between;">
                <strong>SUITE 104</strong>
                <span class="ui-badge blue">Vacant / Ready</span>
              </div>
              <p style="font-size:13px;color:#334155;margin:8px 0 4px 0;">Sterilized &amp; Sanitized</p>
              <button onclick="showToast('Assigned Suite 104 to incoming admission.')" class="ui-btn-action primary" style="width:100%;justify-content:center;margin-top:6px;padding:4px 10px;font-size:12px;">Assign Suite</button>
            </div>
          </div>
        </div>

        <!-- Section 3: Patient Admission & Triage Workflow -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>📥</span> Section 3: Patient Admission &amp; Obstetric Triage Workflow</h3>
              <div class="ui-section-subtitle">Instant biometric verification, bed tagging, and digital wristband generation</div>
            </div>
          </div>
          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:700;color:#24063E;">Quick Digital IPD Registration</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">Scan patient QR card or search MRN to instantly assign bed and trigger nurse call bell.</p>
            </div>
            <button onclick="showToast('Opening Rapid IPD Registration Console...')" class="ui-btn-action outline">Register Admission</button>
          </div>
        </div>

        <!-- Section 4: Discharge Planning & Neonatal Clearance Pipeline -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🎓</span> Section 4: Discharge Clearance &amp; Pediatric Sign-Off Pipeline</h3>
              <div class="ui-section-subtitle">3-Stage clearance: Obstetrician + Neonatal Pediatrician + Final TPA billing</div>
            </div>
          </div>
          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;">Bed 204 — Priya K. (Post LSCS Day 3)</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">Dr. Shilpi suture check: Passed • Pediatrician neonatal clearance: Passed • TPA settlement: Done</p>
            </div>
            <button onclick="showToast('Discharge summary generated & sent to patient WhatsApp.')" class="ui-btn-action primary">Generate Discharge</button>
          </div>
        </div>

        <!-- Section 5: Ward Nursing Shift & Patient Telemetry -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>👩‍⚕️</span> Section 5: Ward Nursing Shift &amp; Patient-to-Nurse Staffing Ratio</h3>
              <div class="ui-section-subtitle">NABH standard 1:2 in LDRP suites and 1:1 in active labor</div>
            </div>
            <span class="ui-badge success">Staffing Compliant</span>
          </div>
          <div class="ui-grid-3">
            <div class="ui-card" style="padding:18px;">
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;">Morning Shift (7am–3pm)</h4>
              <p style="font-size:13px;color:#64748b;margin:6px 0;">14 Registered Nurses on duty • Lead Incharge: Sr. Rebecca</p>
              <span class="ui-badge success">Active Shift</span>
            </div>
            <div class="ui-card" style="padding:18px;">
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;">Evening Shift (3pm–11pm)</h4>
              <p style="font-size:13px;color:#64748b;margin:6px 0;">12 Registered Nurses rostered • Lead Incharge: Sr. Lakshmi</p>
              <span class="ui-badge blue">Standby Handover</span>
            </div>
            <div class="ui-card" style="padding:18px;">
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;">Night Shift (11pm–7am)</h4>
              <p style="font-size:13px;color:#64748b;margin:6px 0;">10 Registered Nurses + 2 Midwives on labor triage</p>
              <span class="ui-badge outline">Scheduled</span>
            </div>
          </div>
        </div>
    '''
    return build_html("Bed Occupancy & Wards", "Hospital Ward Census & Inpatient Management", "admin-admissions.html", True, content)


# ==============================================================================
# 5. ADMIN: admin-nicu.html (Level-3 NICU Telemetry)
# ==============================================================================
def create_admin_nicu():
    content = '''
        <div class="dash-welcome-row">
          <div>
            <h1 class="dash-welcome-title">Level-3 NICU Telemetry &amp; Neonatal Care 🍼</h1>
            <p class="dash-welcome-sub">Tertiary neonatal intensive care, Draeger incubators, CPAP ventilation, and micro-preemie monitoring.</p>
          </div>
          <button onclick="showToast('NICU Central Telemetry stream refreshed.')" class="ui-btn-action primary">
            <span>⚡ REFRESH NICU SENSORS</span>
          </button>
        </div>

        <!-- Section 1: NICU Incubator Census & Acuity Scoreboard -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>👶</span> Section 1: Level-3 NICU Incubator Census (12 Total Cribs)</h3>
              <div class="ui-section-subtitle">Salem Center tertiary neonatal critical care facility</div>
            </div>
            <span class="ui-badge success">8 Occupied • 4 Available</span>
          </div>
          <div class="ui-grid-4">
            <div class="ui-card" style="padding:18px;border-left:4px solid #967BB6;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">ACTIVE NEONATES</span>
              <div style="font-size:32px;font-weight:900;color:#1E0533;margin:6px 0;">8 Babies</div>
              <span style="font-size:12px;color:#967BB6;">Gestational age: 28w to 36w</span>
            </div>
            <div class="ui-card" style="padding:18px;border-left:4px solid #3B0764;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">CPAP / VENTILATED</span>
              <div style="font-size:32px;font-weight:900;color:#3B0764;margin:6px 0;">2 Babies</div>
              <span style="font-size:12px;color:#64748b;">Bubble CPAP respiratory support</span>
            </div>
            <div class="ui-card" style="padding:18px;border-left:4px solid #967BB6;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">PHOTOTHERAPY UNITS</span>
              <div style="font-size:32px;font-weight:900;color:#967BB6;margin:6px 0;">3 Babies</div>
              <span style="font-size:12px;color:#3B0764;">Neonatal hyperbilirubinemia</span>
            </div>
            <div class="ui-card" style="padding:18px;border-left:4px solid #967BB6;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">ROOMING-IN READY</span>
              <div style="font-size:32px;font-weight:900;color:#967BB6;margin:6px 0;">3 Babies</div>
              <span style="font-size:12px;color:#967BB6;">Kangaroo care &amp; breast feeding</span>
            </div>
          </div>
        </div>

        <!-- Section 2: Central Neonatal Telemetry Monitor -->
        <div class="ui-section-card" style="background:#1E0533;color:#ffffff;border:none;">
          <div class="ui-section-title-wrap" style="border-color:#24063E;">
            <div class="ui-section-title-group">
              <h3 style="color:#ffffff;"><span>💓</span> Section 2: Central Multipara Neonatal Telemetry Wall</h3>
              <div class="ui-section-subtitle" style="color:#94a3b8;">Real-time continuous pulse oximetry, heart rate, and Draeger incubator thermoregulation</div>
            </div>
            <span class="ui-badge success"><span class="ui-pulse-dot"></span> All Traces Stable</span>
          </div>
          <div class="ui-grid-4">
            <div style="background:#24063E;padding:16px;border-radius:12px;border:1px solid #334155;">
              <div style="display:flex;justify-content:space-between;color:#94a3b8;font-size:11px;">
                <span>CRIB 1 (PRE-TERM 30W)</span>
                <span class="ui-badge success">Stable</span>
              </div>
              <div style="font-size:24px;font-weight:900;color:#38bdf8;margin:8px 0;">HR: 138 bpm</div>
              <div style="font-size:12px;color:#a7f3d0;">SpO2: 96% • Temp: 36.8°C</div>
            </div>

            <div style="background:#24063E;padding:16px;border-radius:12px;border:1px solid #334155;">
              <div style="display:flex;justify-content:space-between;color:#94a3b8;font-size:11px;">
                <span>CRIB 2 (CPAP SUPPORT)</span>
                <span class="ui-badge success">Stable</span>
              </div>
              <div style="font-size:24px;font-weight:900;color:#38bdf8;margin:8px 0;">HR: 142 bpm</div>
              <div style="font-size:12px;color:#a7f3d0;">SpO2: 95% • PEEP: 5 cmH2O</div>
            </div>

            <div style="background:#24063E;padding:16px;border-radius:12px;border:1px solid #334155;">
              <div style="display:flex;justify-content:space-between;color:#94a3b8;font-size:11px;">
                <span>CRIB 3 (PHOTOTHERAPY)</span>
                <span class="ui-badge success">Stable</span>
              </div>
              <div style="font-size:24px;font-weight:900;color:#facc15;margin:8px 0;">HR: 134 bpm</div>
              <div style="font-size:12px;color:#a7f3d0;">Bilirubin: 11.2 mg/dL (Dropping)</div>
            </div>

            <div style="background:#24063E;padding:16px;border-radius:12px;border:1px solid #334155;">
              <div style="display:flex;justify-content:space-between;color:#94a3b8;font-size:11px;">
                <span>CRIB 4 (GROWTH FEEDER)</span>
                <span class="ui-badge success">Stable</span>
              </div>
              <div style="font-size:24px;font-weight:900;color:#38bdf8;margin:8px 0;">HR: 130 bpm</div>
              <div style="font-size:12px;color:#a7f3d0;">Weight: 1.84 kg (+45g today)</div>
            </div>
          </div>
        </div>

        <!-- Section 3: Kangaroo Mother Care & Expressed Milk Log -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🤱</span> Section 3: Kangaroo Mother Care (KMC) &amp; Human Milk Bank</h3>
              <div class="ui-section-subtitle">Promoting maternal bonding and zero artificial formula policy</div>
            </div>
            <span class="ui-badge plum">100% Mother's Milk</span>
          </div>
          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:700;color:#24063E;">Daily KMC Skin-to-Skin Session Tracker</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">6 Mothers completed morning 2-hour KMC sessions • Neonatal body temperatures stabilized naturally.</p>
            </div>
            <span class="ui-badge success">Completed</span>
          </div>
        </div>

        <!-- Section 4: Neonatal Resuscitation & Emergency Code Pink Protocol -->
        <div class="ui-section-card" style="background:#fff7ed;border-color:#fed7aa;">
          <div class="ui-section-title-wrap" style="border-color:#fed7aa;">
            <div class="ui-section-title-group">
              <h3 style="color:#9a3412;"><span>🚨</span> Section 4: Neonatal Resuscitation &amp; Emergency Code Pink System</h3>
              <div class="ui-section-subtitle" style="color:#3B0764;">Immediate overhead alarm and T-piece resuscitator deployment</div>
            </div>
            <span class="ui-badge amber">Code Pink Sentinel Active</span>
          </div>
          <div class="ui-interactive-row" style="background:#ffffff;">
            <div>
              <h4 style="font-size:15px;font-weight:700;color:#24063E;">Neopuff T-Piece Resuscitation Warmers</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">All 3 warmers tested at 8:00 AM • Blended oxygen/air mixers calibrated to 21%-30% FiO2</p>
            </div>
            <span class="ui-badge success">Ready 24×7</span>
          </div>
        </div>

        <!-- Section 5: Weight Gain Milestones & Pediatric Discharge Criteria -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>📈</span> Section 5: Weight Gain Milestones &amp; Pediatric Discharge Gate</h3>
              <div class="ui-section-subtitle">Discharge benchmark: Consistent 20g/day weight gain and independent sucking feed</div>
            </div>
          </div>
          <div class="ui-grid-3">
            <div class="ui-card" style="padding:18px;">
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;">Baby of Lakshmi (32w)</h4>
              <p style="font-size:13px;color:#64748b;margin:6px 0;">Current: 1.95 kg (Birth: 1.4 kg) • Sucking feeds established</p>
              <span class="ui-badge success">Discharge Tomorrow</span>
            </div>
            <div class="ui-card" style="padding:18px;">
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;">Baby of Revathi (31w)</h4>
              <p style="font-size:13px;color:#64748b;margin:6px 0;">Current: 1.80 kg (Birth: 1.35 kg) • Tolerating 30ml feeds</p>
              <span class="ui-badge blue">Discharge in 3 Days</span>
            </div>
            <div class="ui-card" style="padding:18px;">
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;">Baby of Deepa (34w)</h4>
              <p style="font-size:13px;color:#64748b;margin:6px 0;">Current: 2.10 kg (Birth: 1.9 kg) • Bilirubin clear</p>
              <span class="ui-badge success">Rooming In with Mother</span>
            </div>
          </div>
        </div>
    '''
    return build_html("Level-3 NICU Telemetry", "Neonatal Intensive Care Unit Monitoring", "admin-nicu.html", True, content)


# ==============================================================================
# 6. ADMIN: admin-lab.html (Diagnostic Laboratory)
# ==============================================================================
def create_admin_lab():
    content = '''
        <div class="dash-welcome-row">
          <div>
            <h1 class="dash-welcome-title">Diagnostic Pathology &amp; Fetal Genetics Lab 🧪</h1>
            <p class="dash-welcome-sub">NABL accredited antenatal pathology, automated biochemical analyzers, and blood bank cross-matching.</p>
          </div>
          <button onclick="showToast('Dispatching Emergency Blood Cross-Match Order...')" class="ui-btn-action primary">
            <span>+ ORDER BLOOD CROSS-MATCH</span>
          </button>
        </div>

        <!-- Section 1: Laboratory Specimen Tracking Pipeline -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🔬</span> Section 1: Specimen Barcode &amp; Processing Pipeline</h3>
              <div class="ui-section-subtitle">Real-time sample tracking from phlebotomy chair to validated digital report</div>
            </div>
            <span class="ui-badge success">Avg Turnaround: 42 Mins</span>
          </div>
          <div class="ui-grid-4">
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">SAMPLES COLLECTED TODAY</span>
              <div style="font-size:28px;font-weight:900;color:#1E0533;margin:6px 0;">128 Samples</div>
              <span style="font-size:12px;color:#967BB6;">100% Barcoded &amp; Tracked</span>
            </div>
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">IN ACTIVE ANALYZER</span>
              <div style="font-size:28px;font-weight:900;color:#967BB6;margin:6px 0;">18 Samples</div>
              <span style="font-size:12px;color:#967BB6;">Beckman Coulter DxH 500</span>
            </div>
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">REPORTS VALIDATED</span>
              <div style="font-size:28px;font-weight:900;color:#967BB6;margin:6px 0;">96 Reports</div>
              <span style="font-size:12px;color:#967BB6;">Signed by Pathologist</span>
            </div>
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">CRITICAL PANIC VALUES</span>
              <div style="font-size:28px;font-weight:900;color:#967BB6;margin:6px 0;">0 Unnotified</div>
              <span style="font-size:12px;color:#967BB6;">All alerts dispatched</span>
            </div>
          </div>
        </div>

        <!-- Section 2: Fetal Genetic & Antenatal Biochemistry Roster -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🧬</span> Section 2: Antenatal Genetic &amp; Aneuploidy Testing</h3>
              <div class="ui-section-subtitle">Prenatal cell-free DNA, Dual Marker, and TORCH antibody panels</div>
            </div>
          </div>
          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;">NIPT Cell-Free DNA Batch #CF-2026-92</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">12 Maternal blood samples • Next-generation sequencing for Trisomies 21, 18, 13 • Status: Sequencing 84%</p>
            </div>
            <span class="ui-badge blue">In Analysis</span>
          </div>

          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;">First Trimester Dual Marker PAPP-A + Free Beta hCG</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">8 Samples processed on Roche Cobas e411 • FMF MoM Risk calculation complete</p>
            </div>
            <span class="ui-badge success">Reports Released</span>
          </div>
        </div>

        <!-- Section 3: Blood Bank & Obstetric Emergency Cross-Match -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🩸</span> Section 3: Hospital Blood Storage &amp; Obstetric Cross-Match</h3>
              <div class="ui-section-subtitle">Zero-delay emergency blood units reserved specifically for maternity hemorrhage</div>
            </div>
            <span class="ui-badge success">Blood Bank Reserves Full</span>
          </div>
          <div class="ui-grid-4">
            <div class="ui-card" style="padding:16px;text-align:center;">
              <span style="font-size:11px;font-weight:700;color:#3B0764;">O-NEGATIVE (UNIVERSAL)</span>
              <div style="font-size:26px;font-weight:900;color:#3B0764;margin:6px 0;">6 Units</div>
              <span style="font-size:12px;color:#64748b;">Emergency PRBC ready</span>
            </div>
            <div class="ui-card" style="padding:16px;text-align:center;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">B-POSITIVE (MOST COMMON)</span>
              <div style="font-size:26px;font-weight:900;color:#1E0533;margin:6px 0;">14 Units</div>
              <span style="font-size:12px;color:#967BB6;">Stocked</span>
            </div>
            <div class="ui-card" style="padding:16px;text-align:center;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">FRESH FROZEN PLASMA</span>
              <div style="font-size:26px;font-weight:900;color:#1E0533;margin:6px 0;">18 Units</div>
              <span style="font-size:12px;color:#967BB6;">Thawed standby: 4 units</span>
            </div>
            <div class="ui-card" style="padding:16px;text-align:center;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">PLATELET CONCENTRATES</span>
              <div style="font-size:26px;font-weight:900;color:#1E0533;margin:6px 0;">8 Units</div>
              <span style="font-size:12px;color:#967BB6;">Rotator active</span>
            </div>
          </div>
        </div>

        <!-- Section 4: Equipment Calibration & NABL Quality Control Sentinel -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🛡️</span> Section 4: NABL Daily Calibration &amp; Internal Quality Control (IQC)</h3>
              <div class="ui-section-subtitle">Westgard multirule analysis automatically validating analytical runs</div>
            </div>
            <span class="ui-badge success">All 5 QC Rules Passed</span>
          </div>
          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:700;color:#24063E;">Beckman Coulter DxH 500 (Complete Blood Count)</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">3-Level controls run at 7:30 AM • CV &lt; 1.2% for Hemoglobin and Platelets • Levey-Jennings chart valid</p>
            </div>
            <span class="ui-badge success">Calibrated</span>
          </div>
        </div>

        <!-- Section 5: Critical Panic Value Emergency Alert Dispatcher -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🚨</span> Section 5: Panic Value Protocol (Automatic Doctor SMS &amp; Phone Alert)</h3>
              <div class="ui-section-subtitle">Thresholds: Hb &lt; 7.0 g/dL, Platelets &lt; 50,000 /µL, Neonatal Bilirubin &gt; 18 mg/dL</div>
            </div>
            <span class="ui-badge success">Sentinel Monitoring Active</span>
          </div>
          <div style="background:#FAF9F5;padding:18px;border-radius:14px;border:1px solid #DDD6FE;">
            <p style="font-size:13.5px;color:#334155;line-height:1.6;">
              Automated telecom dispatcher connects directly to the attending consultant doctor's mobile phone within 90 seconds if a life-threatening abnormal value is detected.
            </p>
          </div>
        </div>
    '''
    return build_html("Diagnostic Laboratory", "Pathology, Blood Bank & Genetics Lab", "admin-lab.html", True, content)


# ==============================================================================
# 7. ADMIN: admin-billing.html (Revenue & TPA Cashless Claims)
# ==============================================================================
def create_admin_billing():
    content = '''
        <div class="dash-welcome-row">
          <div>
            <h1 class="dash-welcome-title">Revenue, Packages &amp; TPA Cashless Claims 💳</h1>
            <p class="dash-welcome-sub">Hospital financial cockpit, Star Health &amp; MediBuddy cashless claims, and maternity package settlement.</p>
          </div>
          <button onclick="showToast('Exporting Daily Financial Audit Ledger to PDF...')" class="ui-btn-action primary">
            <span>📥 EXPORT FINANCIAL AUDIT</span>
          </button>
        </div>

        <!-- Section 1: Hospital Daily Financial Telemetry -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>📊</span> Section 1: Hospital Financial Collections &amp; Stream Breakdown</h3>
              <div class="ui-section-subtitle">Consolidated daily revenue across Salem Main Hospital and Outpatient Center</div>
            </div>
            <span class="ui-badge success">Target Achieved</span>
          </div>
          <div class="ui-grid-4">
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">TODAY'S TOTAL BILLING</span>
              <div style="font-size:28px;font-weight:900;color:#967BB6;margin:6px 0;">₹ 3,42,800</div>
              <span style="font-size:12px;color:#967BB6;">+14.2% Growth Day-on-Day</span>
            </div>
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">INPATIENT MATERNITY</span>
              <div style="font-size:28px;font-weight:900;color:#1E0533;margin:6px 0;">₹ 1,95,000</div>
              <span style="font-size:12px;color:#64748b;">3 LDRP Packages Settled</span>
            </div>
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">OUTPATIENT &amp; ULTRASOUND</span>
              <div style="font-size:28px;font-weight:900;color:#1E0533;margin:6px 0;">₹ 69,400</div>
              <span style="font-size:12px;color:#64748b;">4D Scans &amp; Consultations</span>
            </div>
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">PHARMACY DISPATCH</span>
              <div style="font-size:28px;font-weight:900;color:#1E0533;margin:6px 0;">₹ 78,400</div>
              <span style="font-size:12px;color:#64748b;">114 Prescriptions Filled</span>
            </div>
          </div>
        </div>

        <!-- Section 2: TPA Cashless Pre-Authorization Tracker -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🛡️</span> Section 2: TPA Cashless Insurance Desk &amp; Pre-Auth Approvals</h3>
              <div class="ui-section-subtitle">Real-time settlement with Star Health, MediBuddy, HDFC Ergo, ICICI Lombard</div>
            </div>
            <button onclick="showToast('Querying TPA Insurance Portal API...')" class="ui-btn-action outline">Check Pending Approvals</button>
          </div>
          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;">Lingalamanasa123 — Star Health Women Care (MRN #WHC-88412)</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">Package: LDRP Luxury Birthing Suite • Claimed: ₹65,000 • Pre-Auth Approved: ₹50,000 • Status: Settled</p>
            </div>
            <span class="ui-badge success">Approved (₹50,000)</span>
          </div>

          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;">Pooja Venkat — MediBuddy / New India Assurance (MRN #WHC-89102)</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">Procedure: Laparoscopic Ovarian Cystectomy • Claimed: ₹55,000 • Query answered with operative report</p>
            </div>
            <span class="ui-badge amber">Under Query Review</span>
          </div>

          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;">Kavitha Raman — HDFC Ergo Health (MRN #WHC-90214)</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">Package: Normal Delivery with Epidural Analgesia • Claimed: ₹45,000 • Pre-auth letter generated</p>
            </div>
            <span class="ui-badge success">Approved (₹45,000)</span>
          </div>
        </div>

        <!-- Section 3: Inpatient Final Discharge Bill Clearance Console -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🧾</span> Section 3: Inpatient Final Discharge Bill Clearance Console</h3>
              <div class="ui-section-subtitle">Final bill auditing prior to maternal and newborn discharge</div>
            </div>
          </div>
          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:700;color:#24063E;">Room 204 — Priya K. (C-Section 4-Day Stay)</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">Total Bill: ₹75,000 • Insurance Paid: ₹60,000 • Patient Copay Paid: ₹15,000 • Balance: Nil</p>
            </div>
            <button onclick="showToast('Final No-Dues Clearance Slip generated for Room 204.')" class="ui-btn-action primary">Generate Gate Pass</button>
          </div>
        </div>

        <!-- Section 4: Corporate & Government Empanelment Claims -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🏢</span> Section 4: Corporate Maternity Empanelment &amp; Government Schemes</h3>
              <div class="ui-section-subtitle">Direct empanelment partnerships with IT tech parks and state maternal health benefits</div>
            </div>
          </div>
          <div class="ui-grid-3">
            <div class="ui-card" style="padding:18px;">
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;">TCS / Infosys Healthcare Tie-Up</h4>
              <p style="font-size:12.5px;color:#64748b;margin:6px 0;">100% Cashless maternity cover up to ₹1,00,000 with private luxury room upgrade.</p>
              <span class="ui-badge success">Empaneled Partner</span>
            </div>

            <div class="ui-card" style="padding:18px;">
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;">Tamil Nadu CMCHIS Maternal Cover</h4>
              <p style="font-size:12.5px;color:#64748b;margin:6px 0;">Institutional delivery benefit scheme with zero cost neonatal intensive care.</p>
              <span class="ui-badge blue">Government Approved</span>
            </div>

            <div class="ui-card" style="padding:18px;">
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;">HDFC Bank Employee Care</h4>
              <p style="font-size:12.5px;color:#64748b;margin:6px 0;">Priority OPD chamber slots and subsidized 4D anomaly scans.</p>
              <span class="ui-badge success">Active Scheme</span>
            </div>
          </div>
        </div>

        <!-- Section 5: Pharmacy & Consumables Revenue Stream -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>💊</span> Section 5: Pharmacy POS &amp; Surgical Consumables Audit</h3>
              <div class="ui-section-subtitle">Daily stock reconciliation and emergency obstetric medicine reserves</div>
            </div>
            <span class="ui-badge success">Audit Reconciled</span>
          </div>
          <div class="ui-grid-4">
            <div class="ui-card" style="padding:16px;text-align:center;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">PHARMACY TRANSACTIONS</span>
              <div style="font-size:26px;font-weight:900;color:#1E0533;margin:6px 0;">114 Bills</div>
              <span style="font-size:12px;color:#967BB6;">₹78,400 Total</span>
            </div>
            <div class="ui-card" style="padding:16px;text-align:center;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">OXYTOCIN &amp; ERGOMETRINE</span>
              <div style="font-size:26px;font-weight:900;color:#967BB6;margin:6px 0;">100% Stocked</div>
              <span style="font-size:12px;color:#64748b;">Cold-chain 2°C-8°C verified</span>
            </div>
            <div class="ui-card" style="padding:16px;text-align:center;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">EPIDURAL KITS</span>
              <div style="font-size:26px;font-weight:900;color:#1E0533;margin:6px 0;">42 Kits</div>
              <span style="font-size:12px;color:#967BB6;">Sterile batch valid</span>
            </div>
            <div class="ui-card" style="padding:16px;text-align:center;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">SURGICAL GAUZE &amp; SUTURES</span>
              <div style="font-size:26px;font-weight:900;color:#1E0533;margin:6px 0;">Full Supply</div>
              <span style="font-size:12px;color:#967BB6;">Vicryl &amp; Monocryl ready</span>
            </div>
          </div>
        </div>
    '''
    return build_html("Revenue & TPA Claims", "Hospital Financial Operations & Cashless TPA Claims", "admin-billing.html", True, content)

print("build_admin_pages.py defined.")
