# build_user_pages.py
# Generates the 6 remaining User Dashboard pages with 5 UI/UX sections each
from generate_all_dashboards import build_html

# ==============================================================================
# 2. USER: user-vitals.html (Telemetry & Vitals)
# ==============================================================================
def create_user_vitals():
    content = '''
        <div class="dash-welcome-row">
          <div>
            <h1 class="dash-welcome-title">Maternal Telemetry &amp; Vitals Monitor 💓</h1>
            <p class="dash-welcome-sub">Continuous biometric tracking, fetal kick count velocity, and preeclampsia indicators.</p>
          </div>
          <button onclick="showToast('Syncing with Bluetooth Vitals Cuff... Connected!')" class="ui-btn-action primary">
            <span>⚡ SYNC BLUETOOTH DEVICES</span>
          </button>
        </div>

        <!-- Section 1: Live Maternal Biometrics Grid -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>📊</span> Section 1: Live Maternal Biometrics Grid</h3>
              <div class="ui-section-subtitle">Real-time parameters verified against pregnancy gestational norms</div>
            </div>
            <span class="ui-badge success"><span class="ui-pulse-dot"></span> Telemetry Active</span>
          </div>
          <div class="ui-grid-3">
            <div class="ui-card" style="padding:22px;border-top:4px solid #967BB6;">
              <div style="display:flex;justify-content:space-between;">
                <span style="font-size:12px;font-weight:700;color:#64748b;">ARTERIAL BLOOD PRESSURE</span>
                <span class="ui-badge success">Optimal</span>
              </div>
              <div style="font-size:32px;font-weight:900;color:#1E0533;margin:12px 0 4px 0;">118/76</div>
              <p style="font-size:12.5px;color:#64748b;">Target range: 110-125 / 70-82 mmHg • Mean Arterial: 90 mmHg</p>
            </div>

            <div class="ui-card" style="padding:22px;border-top:4px solid #967BB6;">
              <div style="display:flex;justify-content:space-between;">
                <span style="font-size:12px;font-weight:700;color:#64748b;">PULSE OXIMETRY (SpO2)</span>
                <span class="ui-badge success">99% Normal</span>
              </div>
              <div style="font-size:32px;font-weight:900;color:#1E0533;margin:12px 0 4px 0;">99 %</div>
              <p style="font-size:12.5px;color:#64748b;">Resting pulse rate: 74 bpm • Continuous photoplethysmography</p>
            </div>

            <div class="ui-card" style="padding:22px;border-top:4px solid #967BB6;">
              <div style="display:flex;justify-content:space-between;">
                <span style="font-size:12px;font-weight:700;color:#64748b;">WEIGHT GAIN VELOCITY</span>
                <span class="ui-badge amber">+6.8 kg Total</span>
              </div>
              <div style="font-size:32px;font-weight:900;color:#1E0533;margin:12px 0 4px 0;">64.2 kg</div>
              <p style="font-size:12.5px;color:#64748b;">Weekly progression: 0.38 kg/wk • Optimal BMI percentile curve</p>
            </div>
          </div>
        </div>

        <!-- Section 2: Fetal Kick Count Telemetry & Daily Movement Tracker -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>👣</span> Section 2: Fetal Kick Count Telemetry (Cardiff Count-to-Ten)</h3>
              <div class="ui-section-subtitle">Record 10 distinct baby kicks to confirm healthy fetal neurological activity</div>
            </div>
            <button onclick="recordKick()" class="ui-btn-action primary" id="kickCounterBtn">
              <span>+ RECORD KICK (Current: 10)</span>
            </button>
          </div>
          <div class="ui-interactive-row" style="background:#fffbeb;border-color:#fef3c7;">
            <div>
              <h4 style="font-size:16px;font-weight:800;color:#92400e;">Today's Kick Goal Achieved in 1 Hour 12 Minutes 🎉</h4>
              <p style="font-size:13px;color:#3B0764;margin-top:2px;">Count started at 8:00 AM • 10th movement logged at 9:12 AM. Fetal reactivity score: Excellent.</p>
            </div>
            <span class="ui-badge amber">Verified Reactivity</span>
          </div>
          <div class="ui-grid-4" style="margin-top:16px;">
            <div class="ui-card" style="padding:16px;text-align:center;">
              <div style="font-size:11px;font-weight:700;color:#64748b;">MONDAY</div>
              <div style="font-size:22px;font-weight:800;color:#967BB6;margin:4px 0;">10 Kicks</div>
              <div style="font-size:11px;color:#64748b;">in 58 mins</div>
            </div>
            <div class="ui-card" style="padding:16px;text-align:center;">
              <div style="font-size:11px;font-weight:700;color:#64748b;">TUESDAY</div>
              <div style="font-size:22px;font-weight:800;color:#967BB6;margin:4px 0;">10 Kicks</div>
              <div style="font-size:11px;color:#64748b;">in 1 hr 05 mins</div>
            </div>
            <div class="ui-card" style="padding:16px;text-align:center;">
              <div style="font-size:11px;font-weight:700;color:#64748b;">WEDNESDAY</div>
              <div style="font-size:22px;font-weight:800;color:#967BB6;margin:4px 0;">10 Kicks</div>
              <div style="font-size:11px;color:#64748b;">in 1 hr 12 mins</div>
            </div>
            <div class="ui-card" style="padding:16px;text-align:center;background:#FAF9F5;">
              <div style="font-size:11px;font-weight:700;color:#64748b;">THURSDAY</div>
              <div style="font-size:22px;font-weight:800;color:#967BB6;margin:4px 0;">In Progress</div>
              <div style="font-size:11px;color:#64748b;">Next slot 8:00 PM</div>
            </div>
          </div>
        </div>

        <!-- Section 3: Gestational Diabetes & Blood Glucose Log -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🩸</span> Section 3: Gestational Diabetes (GDM) Glucose Profiler</h3>
              <div class="ui-section-subtitle">DIPSI &amp; IADPSG guidelines benchmarked for prenatal safety</div>
            </div>
            <button onclick="showToast('Opening Glucose Logger Modal...')" class="ui-btn-action outline">+ Log Blood Sugar</button>
          </div>
          <div class="ui-grid-3">
            <div class="ui-card" style="padding:18px;">
              <span class="ui-badge success">Fasting Normal</span>
              <div style="font-size:28px;font-weight:800;color:#1E0533;margin:10px 0 2px 0;">88 mg/dL</div>
              <div style="font-size:12px;color:#64748b;">Benchmark threshold: &lt; 95 mg/dL</div>
            </div>
            <div class="ui-card" style="padding:18px;">
              <span class="ui-badge success">1-Hr Post-Prandial</span>
              <div style="font-size:28px;font-weight:800;color:#1E0533;margin:10px 0 2px 0;">122 mg/dL</div>
              <div style="font-size:12px;color:#64748b;">Benchmark threshold: &lt; 140 mg/dL</div>
            </div>
            <div class="ui-card" style="padding:18px;">
              <span class="ui-badge success">2-Hr Post-Prandial</span>
              <div style="font-size:28px;font-weight:800;color:#1E0533;margin:10px 0 2px 0;">112 mg/dL</div>
              <div style="font-size:12px;color:#64748b;">Benchmark threshold: &lt; 120 mg/dL</div>
            </div>
          </div>
        </div>

        <!-- Section 4: Preeclampsia & Blood Pressure Trend Monitor -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🛡️</span> Section 4: Preeclampsia &amp; Vascular Resistance Monitor</h3>
              <div class="ui-section-subtitle">Continuous uterine artery PI correlation and urine protein dipstick tracking</div>
            </div>
            <span class="ui-badge success">Risk Score: Low (0.02%)</span>
          </div>
          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:700;color:#24063E;">Urine Dipstick Protein Albumin Evaluation</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">Result: Negative / Nil • Last verified during Week 24 OPD consultation</p>
            </div>
            <span class="ui-badge success">Nil Protein</span>
          </div>
          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:700;color:#24063E;">Bilateral Uterine Artery Mean Pulsatility Index (PI)</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">PI value: 0.88 • High velocity low resistance diastolic flow confirmed by Dr. Meera</p>
            </div>
            <span class="ui-badge success">Normal Waveform</span>
          </div>
        </div>

        <!-- Section 5: Connected Wearables & Home Health Sync -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>📱</span> Section 5: Connected Wearables &amp; Home Telemetry Devices</h3>
              <div class="ui-section-subtitle">Paired medical peripherals automatically feeding maternal clinical data</div>
            </div>
            <button onclick="showToast('Pairing new medical telemetry device...')" class="ui-btn-action outline">+ Pair New Device</button>
          </div>
          <div class="ui-grid-3">
            <div class="ui-card" style="padding:18px;">
              <div style="display:flex;justify-content:space-between;">
                <h4 style="font-size:15px;font-weight:800;color:#1E0533;">Omron Evolv BP Cuff</h4>
                <span class="ui-badge success">Connected</span>
              </div>
              <p style="font-size:12.5px;color:#64748b;margin:8px 0 12px 0;">Wireless upper arm Bluetooth blood pressure monitor.</p>
              <button onclick="showToast('Fetching latest BP reading...')" class="ui-btn-action outline" style="width:100%;justify-content:center;">Sync Reading Now</button>
            </div>

            <div class="ui-card" style="padding:18px;">
              <div style="display:flex;justify-content:space-between;">
                <h4 style="font-size:15px;font-weight:800;color:#1E0533;">Accu-Chek Guide GDM</h4>
                <span class="ui-badge success">Connected</span>
              </div>
              <p style="font-size:12.5px;color:#64748b;margin:8px 0 12px 0;">Instant wireless blood glucose meter and fasting sync.</p>
              <button onclick="showToast('Syncing glucose readings...')" class="ui-btn-action outline" style="width:100%;justify-content:center;">Sync Readings</button>
            </div>

            <div class="ui-card" style="padding:18px;">
              <div style="display:flex;justify-content:space-between;">
                <h4 style="font-size:15px;font-weight:800;color:#1E0533;">Apple Health / Fitbit</h4>
                <span class="ui-badge success">Active</span>
              </div>
              <p style="font-size:12.5px;color:#64748b;margin:8px 0 12px 0;">Daily maternal steps, sleep duration, and resting heart rate.</p>
              <button onclick="showToast('Syncing maternal activity...')" class="ui-btn-action outline" style="width:100%;justify-content:center;">Refresh Health Kit</button>
            </div>
          </div>
        </div>
    '''
    return build_html("Telemetry & Vitals", "Maternal Vitals & Fetal Monitoring", "user-vitals.html", False, content)


# ==============================================================================
# 3. USER: user-consultations.html (Consultations & OPD)
# ==============================================================================
def create_user_consultations():
    content = '''
        <div class="dash-welcome-row">
          <div>
            <h1 class="dash-welcome-title">Consultations &amp; OPD Chambers 📅</h1>
            <p class="dash-welcome-sub">Schedule in-person hospital consultations, tele-health sessions, and track OPD token wait times.</p>
          </div>
          <button onclick="showToast('Opening Rapid Appointment Scheduler...')" class="ui-btn-action primary">
            <span>+ BOOK NEW CONSULTATION</span>
          </button>
        </div>

        <!-- Section 1: Active Appointment & Real-Time Chamber Queue Status -->
        <div class="ui-section-card" style="border:1.5px solid #967BB6;background:#fffdfa;">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🎫</span> Section 1: Active Appointment &amp; Real-Time Chamber Queue</h3>
              <div class="ui-section-subtitle">Live hospital queue telemetry at Stackly Salem Center</div>
            </div>
            <span class="ui-badge amber"><span class="ui-pulse-dot amber"></span> Live Queue Active</span>
          </div>
          <div class="ui-grid-4">
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">YOUR APPOINTMENT TOKEN</span>
              <div style="font-size:36px;font-weight:900;color:#3B0764;margin:8px 0 4px 0;">TOKEN #14</div>
              <p style="font-size:12px;color:#64748b;">OPD Chamber 1 • Dr. Shilpi Singh</p>
            </div>
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">CURRENTLY SERVING TOKEN</span>
              <div style="font-size:36px;font-weight:900;color:#967BB6;margin:8px 0 4px 0;">TOKEN #11</div>
              <p style="font-size:12px;color:#64748b;">Consultation in progress (Chamber 1)</p>
            </div>
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">ESTIMATED WAIT TIME</span>
              <div style="font-size:36px;font-weight:900;color:#1E0533;margin:8px 0 4px 0;">~18 Mins</div>
              <p style="font-size:12px;color:#64748b;">2 Patients ahead of your turn</p>
            </div>
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">CONSULTATION MODE</span>
              <div style="font-size:24px;font-weight:800;color:#1E0533;margin:12px 0 4px 0;">In-Person OPD</div>
              <button onclick="showToast('Directions & digital token sent to WhatsApp.')" class="ui-btn-action outline" style="width:100%;justify-content:center;margin-top:6px;">View Digital Token</button>
            </div>
          </div>
        </div>

        <!-- Section 2: Book New Specialist Appointment -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>👩‍⚕️</span> Section 2: Choose Specialist &amp; Book In-Person / Tele-Consult</h3>
              <div class="ui-section-subtitle">Board-certified senior clinical consultants at Women's Health Center</div>
            </div>
          </div>
          <div class="ui-grid-4">
            <div class="ui-card" style="padding:18px;text-align:center;">
              <img src="assets/img/shilpi-singh.webp" alt="Dr. Shilpi" style="width:84px;height:84px;border-radius:50%;object-fit:cover;margin:0 auto 12px auto;border:2px solid #967BB6;">
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;">Dr. Shilpi Singh</h4>
              <p style="font-size:11.5px;color:#3B0764;font-weight:700;">Director Obstetrics &amp; Surgery</p>
              <div style="font-size:12px;color:#64748b;margin:8px 0 12px 0;">OPD: Mon–Sat (10am–2pm)</div>
              <button onclick="showToast('Selected Dr. Shilpi Singh. Choose slot below.')" class="ui-btn-action primary" style="width:100%;justify-content:center;">Select Doctor</button>
            </div>

            <div class="ui-card" style="padding:18px;text-align:center;">
              <img src="assets/img/dr-ananya.webp" alt="Dr. Ananya" style="width:84px;height:84px;border-radius:50%;object-fit:cover;margin:0 auto 12px auto;border:2px solid #bbf7d0;">
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;">Dr. Ananya Sen</h4>
              <p style="font-size:11.5px;color:#166534;font-weight:700;">Reproductive &amp; Laparoscopy</p>
              <div style="font-size:12px;color:#64748b;margin:8px 0 12px 0;">OPD: Mon–Fri (2pm–6pm)</div>
              <button onclick="showToast('Selected Dr. Ananya Sen. Choose slot below.')" class="ui-btn-action outline" style="width:100%;justify-content:center;">Select Doctor</button>
            </div>

            <div class="ui-card" style="padding:18px;text-align:center;">
              <img src="assets/img/dr-meera.webp" alt="Dr. Meera" style="width:84px;height:84px;border-radius:50%;object-fit:cover;margin:0 auto 12px auto;border:2px solid #bfdbfe;">
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;">Dr. Meera Nair</h4>
              <p style="font-size:11.5px;color:#1e40af;font-weight:700;">Fetal Medicine &amp; Ultrasound</p>
              <div style="font-size:12px;color:#64748b;margin:8px 0 12px 0;">OPD: Tue, Thu, Sat (9am–1pm)</div>
              <button onclick="showToast('Selected Dr. Meera Nair. Choose slot below.')" class="ui-btn-action outline" style="width:100%;justify-content:center;">Select Doctor</button>
            </div>

            <div class="ui-card" style="padding:18px;text-align:center;">
              <img src="assets/img/dr-priya.webp" alt="Dr. Priya" style="width:84px;height:84px;border-radius:50%;object-fit:cover;margin:0 auto 12px auto;border:2px solid #fbcfe8;">
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;">Dr. Priya Sharma</h4>
              <p style="font-size:11.5px;color:#831843;font-weight:700;">Adolescent &amp; Hormonal Care</p>
              <div style="font-size:12px;color:#64748b;margin:8px 0 12px 0;">OPD: Mon, Wed, Fri (4pm–8pm)</div>
              <button onclick="showToast('Selected Dr. Priya Sharma. Choose slot below.')" class="ui-btn-action outline" style="width:100%;justify-content:center;">Select Doctor</button>
            </div>
          </div>
        </div>

        <!-- Section 3: Virtual Tele-Consultation Digital Lounge -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>💻</span> Section 3: Tele-Consultation Digital Lounge (HD Encrypted Video)</h3>
              <div class="ui-section-subtitle">Secure HIPAA &amp; Telemedicine Practice Guidelines compliant consult room</div>
            </div>
            <button onclick="showToast('Testing camera, microphone, and internet bandwidth... All Systems Optimal!')" class="ui-btn-action outline">Check Audio/Video</button>
          </div>
          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:700;color:#24063E;">Next Scheduled Tele-Visit: Antenatal Nutrition &amp; Fetal Growth</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">With Dr. Shilpi Singh • Friday at 4:30 PM (25 Min slot) • Links activates 10 mins prior</p>
            </div>
            <button onclick="showToast('Entering Secure Virtual Waiting Room...')" class="ui-btn-action primary">Join Video Lounge</button>
          </div>
        </div>

        <!-- Section 4: Past Consultation Records & Clinical Notes -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>📁</span> Section 4: Past Consultation Summaries &amp; Doctor Remarks</h3>
              <div class="ui-section-subtitle">Complete chronological record of physical checkups and clinical remarks</div>
            </div>
          </div>
          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:700;color:#24063E;">Week 20 Review: Anatomy Scan &amp; Fundal Height Evaluation</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">Consultant: Dr. Shilpi Singh • Remarks: Fetal heartbeat 144 bpm, fundal height matching dates, iron dosage adjusted.</p>
            </div>
            <button onclick="showToast('Downloading Clinical OPD Summary #RX-88412...')" class="ui-btn-action outline">Download Note PDF</button>
          </div>
          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:700;color:#24063E;">Week 16 Review: Quadruple Marker &amp; Cervical Length Assessment</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">Consultant: Dr. Meera Nair • Remarks: Cervix internal os closed (3.8 cm length), normal amniotic fluid index (AFI: 14 cm).</p>
            </div>
            <button onclick="showToast('Downloading Clinical OPD Summary #RX-81902...')" class="ui-btn-action outline">Download Note PDF</button>
          </div>
        </div>

        <!-- Section 5: Direct Doctor Messaging & Nurse Triage Hotline -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>💬</span> Section 5: Secure Direct Doctor Messaging &amp; Follow-Up Queries</h3>
              <div class="ui-section-subtitle">Ask questions directly to your care team within 7 days of your consultation</div>
            </div>
          </div>
          <div style="background:#FAF9F5;border:1px solid #DDD6FE;border-radius:14px;padding:20px;">
            <div style="margin-bottom:14px;">
              <label style="font-size:13px;font-weight:700;color:#1E0533;display:block;margin-bottom:6px;">Type your non-emergency clinical query:</label>
              <textarea placeholder="e.g., Hello Dr. Shilpi, can I take the calcium supplement with breakfast instead of lunch?" style="width:100%;height:80px;border-radius:10px;border:1.5px solid #cbd5e1;padding:12px;font-family:inherit;font-size:13.5px;"></textarea>
            </div>
            <div style="display:flex;justify-content:space-between;align-items:center;">
              <span style="font-size:12px;color:#64748b;">Average response time: Within 2 hours during OPD hours (Mon–Sat)</span>
              <button onclick="showToast('Your question has been securely transmitted to Dr. Shilpi Singh.')" class="ui-btn-action primary">Send Question to Doctor</button>
            </div>
          </div>
        </div>
    '''
    return build_html("Consultations & OPD", "OPD Token Queue & Doctor Appointments", "user-consultations.html", False, content)


# ==============================================================================
# 4. USER: user-scans.html (4D Scans & Lab Reports)
# ==============================================================================
def create_user_scans():
    content = '''
        <div class="dash-welcome-row">
          <div>
            <h1 class="dash-welcome-title">4D Ultrasound Scans &amp; Diagnostic Vault 📡</h1>
            <p class="dash-welcome-sub">High-definition 4D GE Voluson fetal imaging, anomaly scans, and accredited pathology reports.</p>
          </div>
          <button onclick="showToast('Downloading Complete Pregnancy Medical Dossier (ZIP)...')" class="ui-btn-action primary">
            <span>📦 DOWNLOAD COMPLETE DOSSIER</span>
          </button>
        </div>

        <!-- Section 1: High-Definition 4D Fetal Ultrasound Gallery -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>👶</span> Section 1: 4D HD-Live Fetal Ultrasound Gallery (GE Voluson E10)</h3>
              <div class="ui-section-subtitle">Real-time volumetric render of fetal features and active movement clips</div>
            </div>
            <span class="ui-badge amber">HD Live Rendered</span>
          </div>
          <div class="ui-grid-3">
            <div class="ui-card" style="padding:16px;">
              <div style="height:180px;border-radius:12px;overflow:hidden;background:#1E0533;margin-bottom:12px;">
                <img src="assets/img/facility-ultrasound.webp" alt="4D Scan" style="width:100%;height:100%;object-fit:cover;">
              </div>
              <span class="ui-badge amber">Week 20 • TIFFA Scan</span>
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;margin:8px 0 4px 0;">Fetal Facial Profile &amp; Upper Extremity</h4>
              <p style="font-size:12.5px;color:#64748b;">Nasal bone present, intact palate, clear fingers visualized.</p>
              <button onclick="showToast('Downloading 4K High-Res Ultrasound Image...')" class="ui-btn-action outline" style="width:100%;justify-content:center;margin-top:10px;">Download Scan Photo</button>
            </div>

            <div class="ui-card" style="padding:16px;">
              <div style="height:180px;border-radius:12px;overflow:hidden;background:#1E0533;margin-bottom:12px;">
                <img src="assets/img/service-ultrasound-real.webp" alt="Doppler Scan" style="width:100%;height:100%;object-fit:cover;">
              </div>
              <span class="ui-badge success">Week 24 • Color Doppler</span>
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;margin:8px 0 4px 0;">Umbilical Cord 3-Vessel Flow</h4>
              <p style="font-size:12.5px;color:#64748b;">2 Arteries, 1 Vein confirmed. Peak systolic velocity normal.</p>
              <button onclick="showToast('Downloading Doppler Velocity Cine Loop...')" class="ui-btn-action outline" style="width:100%;justify-content:center;margin-top:10px;">Download Doppler Clip</button>
            </div>

            <div class="ui-card" style="padding:16px;">
              <div style="height:180px;border-radius:12px;overflow:hidden;background:#1E0533;margin-bottom:12px;">
                <img src="assets/img/facility-suite.webp" alt="Echocardiography" style="width:100%;height:100%;object-fit:cover;">
              </div>
              <span class="ui-badge blue">Week 22 • Fetal Echo</span>
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;margin:8px 0 4px 0;">4-Chamber Cardiac Anatomy</h4>
              <p style="font-size:12.5px;color:#64748b;">Intact ventricular septum, concordant outflow tracts.</p>
              <button onclick="showToast('Downloading Pediatric Cardiology Report...')" class="ui-btn-action outline" style="width:100%;justify-content:center;margin-top:10px;">Download Cardiac Scan</button>
            </div>
          </div>
        </div>

        <!-- Section 2: Trimester Genetic & Biochemical Screenings -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🧬</span> Section 2: Trimester Aneuploidy &amp; Genetic Screenings</h3>
              <div class="ui-section-subtitle">Fetal Medicine Foundation (UK) accredited risk calculations</div>
            </div>
            <span class="ui-badge success">All Risks Low</span>
          </div>
          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:700;color:#24063E;">Non-Invasive Prenatal Testing (NIPT) Cell-Free Fetal DNA</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">Trisomy 21 (Down Syndrome), Trisomy 18 (Edwards), Trisomy 13 (Patau) • Risk: &lt; 1 in 10,000</p>
            </div>
            <button onclick="showToast('Downloading Certified NIPT Certificate...')" class="ui-btn-action outline">View Report PDF</button>
          </div>

          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:700;color:#24063E;">First Trimester Combined Screening (NT Scan + Free Beta hCG + PAPP-A)</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">Nuchal Translucency: 1.4 mm • MoM Values: Normal physiological distribution</p>
            </div>
            <button onclick="showToast('Downloading FMF Dual Marker Report...')" class="ui-btn-action outline">View Report PDF</button>
          </div>
        </div>

        <!-- Section 3: Maternal Hematology & Biochemistry Archive -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🧪</span> Section 3: Maternal Hematology &amp; Clinical Pathology Log</h3>
              <div class="ui-section-subtitle">NABL accredited diagnostic laboratory telemetry</div>
            </div>
          </div>
          <div class="ui-grid-4">
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">HEMOGLOBIN (Hb)</span>
              <div style="font-size:26px;font-weight:800;color:#967BB6;margin:6px 0 2px 0;">12.4 g/dL</div>
              <span style="font-size:12px;color:#64748b;">No anemia detected</span>
            </div>
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">BLOOD GROUP &amp; Rh</span>
              <div style="font-size:26px;font-weight:800;color:#1E0533;margin:6px 0 2px 0;">B Positive</div>
              <span style="font-size:12px;color:#64748b;">Rh Incompatibility: Nil</span>
            </div>
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">THYROID (TSH)</span>
              <div style="font-size:26px;font-weight:800;color:#967BB6;margin:6px 0 2px 0;">1.85 mIU/L</div>
              <span style="font-size:12px;color:#64748b;">Optimal Trimester 2 range</span>
            </div>
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">PLATELET COUNT</span>
              <div style="font-size:26px;font-weight:800;color:#967BB6;margin:6px 0 2px 0;">240,000 /µL</div>
              <span style="font-size:12px;color:#64748b;">Normal coagulation profile</span>
            </div>
          </div>
        </div>

        <!-- Section 4: Schedule Diagnostic Ultrasound or Home Blood Collection -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🗓️</span> Section 4: Schedule Upcoming Ultrasound or Home Phlebotomy</h3>
              <div class="ui-section-subtitle">Safe, sterile home sample collection or priority ultrasound suite booking</div>
            </div>
          </div>
          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:700;color:#24063E;">Recommended Next: Third Trimester Fetal Well-being &amp; Doppler Scan</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">Target timing: Week 28 to Week 30 • GE Voluson E10 Suite • Dr. Meera Nair</p>
            </div>
            <button onclick="showToast('Ultrasound scan appointment reserved for Week 28.')" class="ui-btn-action primary">Schedule Scan Slot</button>
          </div>
        </div>

        <!-- Section 5: Radiologist & Sonologist Attestation & Clinical Comments -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>✍️</span> Section 5: Radiologist Certification &amp; FMF Signature</h3>
              <div class="ui-section-subtitle">Verified by Lead Consultant Dr. Meera Nair, MD (OBG), Certified FMF UK</div>
            </div>
            <span class="ui-badge success">Cryptographically Verified</span>
          </div>
          <div style="background:#FAF9F5;padding:20px;border-radius:14px;border:1px solid #DDD6FE;">
            <p style="font-size:13.5px;color:#334155;line-height:1.7;">
              <strong>Sonologist Diagnostic Conclusion:</strong> Single live intrauterine pregnancy corresponding to 24 weeks 3 days. Symmetrical fetal growth along the 54th percentile. Normal amniotic fluid index (14.2 cm). Retroplacental clear space intact. No markers of fetal structural defect identified.
            </p>
            <div style="margin-top:14px;display:flex;align-items:center;gap:16px;">
              <div style="font-size:13px;color:#64748b;">Digital Certificate Hash: <code>0x98f4a...d87c2</code></div>
              <div style="font-size:13px;color:#15803d;font-weight:700;">✓ FMF UK ID: 194820</div>
            </div>
          </div>
        </div>
    '''
    return build_html("4D Scans & Lab Reports", "Ultrasound Vault & Pathology Telemetry", "user-scans.html", False, content)


# ==============================================================================
# 5. USER: user-maternity.html (Maternity Journey & Milestones)
# ==============================================================================
def create_user_maternity():
    content = '''
        <div class="dash-welcome-row">
          <div>
            <h1 class="dash-welcome-title">Your Maternity Journey &amp; Milestones 🤰</h1>
            <p class="dash-welcome-sub">Week-by-week fetal anatomical development, customized birthing plan, and LDRP suite preferences.</p>
          </div>
          <button onclick="showToast('Exporting Pregnancy Milestone Keepsake Journal...')" class="ui-btn-action primary">
            <span>📖 DOWNLOAD MILESTONE JOURNAL</span>
          </button>
        </div>

        <!-- Section 1: Gestational Timeline & Trimester Milestone Navigator -->
        <div class="ui-section-card" style="background:linear-gradient(135deg, #ffffff 0%, #fdf2f8 100%);">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🌟</span> Section 1: Gestational Timeline &amp; Baby Size Navigator</h3>
              <div class="ui-section-subtitle">Week 24 Day 3 • Second Trimester • 110 Days until estimated due date (EDD)</div>
            </div>
            <span class="ui-badge plum">Trimester 2 (Golden Phase)</span>
          </div>
          <div class="ui-grid-4">
            <div class="ui-card" style="padding:20px;text-align:center;">
              <div style="font-size:36px;margin-bottom:8px;">🥭</div>
              <div style="font-size:11px;font-weight:700;color:#64748b;">BABY IS THE SIZE OF A</div>
              <div style="font-size:22px;font-weight:900;color:#831843;margin:4px 0;">Papaya / Ear of Corn</div>
              <div style="font-size:12px;color:#64748b;">Length: ~30 cm • Weight: ~600g</div>
            </div>

            <div class="ui-card" style="padding:20px;text-align:center;">
              <div style="font-size:36px;margin-bottom:8px;">📅</div>
              <div style="font-size:11px;font-weight:700;color:#64748b;">ESTIMATED DUE DATE (EDD)</div>
              <div style="font-size:22px;font-weight:900;color:#1E0533;margin:4px 0;">August 2, 2026</div>
              <div style="font-size:12px;color:#64748b;">Based on Dating Scan at 8 Weeks</div>
            </div>

            <div class="ui-card" style="padding:20px;text-align:center;">
              <div style="font-size:36px;margin-bottom:8px;">🧠</div>
              <div style="font-size:11px;font-weight:700;color:#64748b;">BRAIN &amp; SENSORY MILESTONE</div>
              <div style="font-size:20px;font-weight:900;color:#967BB6;margin:4px 0;">Hearing Your Voice</div>
              <div style="font-size:12px;color:#64748b;">Auditory cochlea fully functioning</div>
            </div>

            <div class="ui-card" style="padding:20px;text-align:center;">
              <div style="font-size:36px;margin-bottom:8px;">🫁</div>
              <div style="font-size:11px;font-weight:700;color:#64748b;">LUNG DEVELOPMENT</div>
              <div style="font-size:20px;font-weight:900;color:#967BB6;margin:4px 0;">Surfactant Production</div>
              <div style="font-size:12px;color:#64748b;">Branching respiratory tree</div>
            </div>
          </div>
        </div>

        <!-- Section 2: Fetal Biometry & Growth Trajectory Percentiles -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>📈</span> Section 2: Fetal Biometry &amp; Ultrasound Growth Trajectory</h3>
              <div class="ui-section-subtitle">Hadlock equation calculations based on Dr. Meera's latest sonography</div>
            </div>
            <span class="ui-badge success">54th Percentile (Ideal)</span>
          </div>
          <div class="ui-grid-4">
            <div class="ui-card" style="padding:16px;">
              <span style="font-size:11px;color:#64748b;font-weight:700;">BIPARIETAL DIAMETER (BPD)</span>
              <div style="font-size:24px;font-weight:800;color:#1E0533;margin:6px 0;">60.2 mm</div>
              <div style="font-size:11.5px;color:#967BB6;">Matches 24w 4d</div>
            </div>
            <div class="ui-card" style="padding:16px;">
              <span style="font-size:11px;color:#64748b;font-weight:700;">HEAD CIRCUMFERENCE (HC)</span>
              <div style="font-size:24px;font-weight:800;color:#1E0533;margin:6px 0;">224 mm</div>
              <div style="font-size:11.5px;color:#967BB6;">Matches 24w 2d</div>
            </div>
            <div class="ui-card" style="padding:16px;">
              <span style="font-size:11px;color:#64748b;font-weight:700;">ABDOMINAL CIRCUMFERENCE</span>
              <div style="font-size:24px;font-weight:800;color:#1E0533;margin:6px 0;">198 mm</div>
              <div style="font-size:11.5px;color:#967BB6;">Matches 24w 3d</div>
            </div>
            <div class="ui-card" style="padding:16px;">
              <span style="font-size:11px;color:#64748b;font-weight:700;">FEMUR LENGTH (FL)</span>
              <div style="font-size:24px;font-weight:800;color:#1E0533;margin:6px 0;">43.8 mm</div>
              <div style="font-size:11.5px;color:#967BB6;">Matches 24w 3d</div>
            </div>
          </div>
        </div>

        <!-- Section 3: Maternal Symptom Tracker & Wellness Journal -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>📝</span> Section 3: Daily Symptom &amp; Physiological Wellness Log</h3>
              <div class="ui-section-subtitle">Real-time symptom severity logging evaluated by maternity nurses</div>
            </div>
            <button onclick="showToast('Symptom Logger Saved.')" class="ui-btn-action outline">+ Log Today's Symptoms</button>
          </div>
          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:700;color:#24063E;">Braxton Hicks Mild Contractions</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">Logged 1 episode post-evening walk • Painless tightening lasting 25 seconds. Normal physiological practice.</p>
            </div>
            <span class="ui-badge success">Physiological Normal</span>
          </div>

          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:700;color:#24063E;">Lower Back &amp; Pelvic Girdle Support</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">Mild fatigue in lumbar region • Relieved by maternity pregnancy pillow and pelvic tilts.</p>
            </div>
            <span class="ui-badge amber">Mild / Managed</span>
          </div>
        </div>

        <!-- Section 4: Personalized Birth Plan & LDRP Suite Customizer -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🛋️</span> Section 4: Personalized Birth Plan &amp; LDRP Suite Preferences</h3>
              <div class="ui-section-subtitle">Collaboratively planned with Dr. Shilpi Singh for respectful birthing</div>
            </div>
            <button onclick="showToast('Birth Plan Saved to Clinical Record.')" class="ui-btn-action primary">Save Preferences</button>
          </div>
          <div class="ui-grid-3">
            <div class="ui-card" style="padding:18px;">
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;margin-bottom:8px;">Birthing Philosophy</h4>
              <div style="font-size:13px;color:#334155;line-height:1.6;">
                ✓ Priority on Normal Physiological Delivery<br>
                ✓ Delayed cord clamping (2-3 mins)<br>
                ✓ Immediate skin-to-skin golden hour
              </div>
            </div>

            <div class="ui-card" style="padding:18px;">
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;margin-bottom:8px;">Pain Relief Preferences</h4>
              <div style="font-size:13px;color:#334155;line-height:1.6;">
                ✓ Ergonomic birthing ball &amp; walking<br>
                ✓ Warm shower hydrotherapy<br>
                ✓ Epidural analgesia on demand
              </div>
            </div>

            <div class="ui-card" style="padding:18px;">
              <h4 style="font-size:15px;font-weight:800;color:#1E0533;margin-bottom:8px;">LDRP Suite Comforts</h4>
              <div style="font-size:13px;color:#334155;line-height:1.6;">
                ✓ Companion birth partner present<br>
                ✓ Dimmed ambient lighting<br>
                ✓ Bluetooth soothing music playlist
              </div>
            </div>
          </div>
        </div>

        <!-- Section 5: Antenatal Fitness & Lamaze Preparation Classes -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🧘‍♀️</span> Section 5: Antenatal Fitness, Yoga &amp; Lamaze Workshops</h3>
              <div class="ui-section-subtitle">Live weekly hospital batches and virtual breathing sessions</div>
            </div>
            <span class="ui-badge success">Enrolled</span>
          </div>
          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:700;color:#24063E;">Saturday Lamaze: Labor Breathing Techniques &amp; Partner Coaching</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">Saturday 11:00 AM • Hospital Antenatal Studio • Led by Senior Midwife R. Lakshmi</p>
            </div>
            <button onclick="showToast('Seat confirmed for Saturday Lamaze Workshop!')" class="ui-btn-action outline">Confirm Attendance</button>
          </div>
        </div>
    '''
    return build_html("Maternity Journey", "Pregnancy Milestones & Birthing Plan", "user-maternity.html", False, content)


# ==============================================================================
# 6. USER: user-prescriptions.html (Digital Prescriptions & Meds)
# ==============================================================================
def create_user_prescriptions():
    content = '''
        <div class="dash-welcome-row">
          <div>
            <h1 class="dash-welcome-title">Digital Prescriptions &amp; Medication Tracker 💊</h1>
            <p class="dash-welcome-sub">Cryptographically verified electronic prescriptions, pill schedules, and 1-tap pharmacy refills.</p>
          </div>
          <button onclick="showToast('Ordering 30-Day Antenatal Refill to Registered Address...')" class="ui-btn-action primary">
            <span>🛒 1-TAP PHARMACY REFILL</span>
          </button>
        </div>

        <!-- Section 1: Active Antenatal Medication Schedule & Daily Dosage Matrix -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>⏰</span> Section 1: Active Antenatal Medication Daily Dosage Matrix</h3>
              <div class="ui-section-subtitle">Timings calibrated for maximum maternal bioavailability and zero mineral interference</div>
            </div>
            <span class="ui-badge success">Schedule Active</span>
          </div>
          <div class="ui-grid-3">
            <div class="ui-card" style="padding:20px;border-left:4px solid #967BB6;">
              <span class="ui-badge amber">MORNING (8:30 AM)</span>
              <h4 style="font-size:16px;font-weight:800;color:#1E0533;margin:10px 0 4px 0;">Ferrous Ascorbate (100mg) + Folic Acid</h4>
              <p style="font-size:13px;color:#64748b;">Take 30 mins after breakfast with lemon water or orange juice to boost iron absorption.</p>
            </div>

            <div class="ui-card" style="padding:20px;border-left:4px solid #967BB6;">
              <span class="ui-badge blue">AFTERNOON (1:30 PM)</span>
              <h4 style="font-size:16px;font-weight:800;color:#1E0533;margin:10px 0 4px 0;">Calcium Carbonate (500mg) + Vit D3</h4>
              <p style="font-size:13px;color:#64748b;">Take after lunch. Keep 4 hours distance from iron supplements to prevent absorption competition.</p>
            </div>

            <div class="ui-card" style="padding:20px;border-left:4px solid #967BB6;">
              <span class="ui-badge plum">NIGHT (9:30 PM)</span>
              <h4 style="font-size:16px;font-weight:800;color:#1E0533;margin:10px 0 4px 0;">Omega-3 DHA (200mg)</h4>
              <p style="font-size:13px;color:#64748b;">Essential fatty acids for fetal neuro-retinal development. Take post-dinner with warm milk.</p>
            </div>
          </div>
        </div>

        <!-- Section 2: Digitally Signed Doctor Prescriptions Archive -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>📜</span> Section 2: Digitally Signed Doctor Prescriptions (QR Verified)</h3>
              <div class="ui-section-subtitle">Valid across all licensed pharmacies in India under Telemedicine Practice Guidelines</div>
            </div>
          </div>
          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:700;color:#24063E;">Rx #WHC-2026-88412 — Trimester 2 Maintenance Regimen</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">Prescribed by Dr. Shilpi Singh, MS (OBG) • Reg #TMC-64820 • Issued: Oct 10, 2026</p>
            </div>
            <button onclick="showToast('Downloading Digitally Signed PDF Rx #WHC-2026-88412...')" class="ui-btn-action outline">Download PDF Rx</button>
          </div>

          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:700;color:#24063E;">Rx #WHC-2026-79104 — Gestational Prophylaxis &amp; Micronutrients</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">Prescribed by Dr. Meera Nair, MD (OBG) • Reg #TMC-58219 • Issued: Sep 12, 2026</p>
            </div>
            <button onclick="showToast('Downloading Digitally Signed PDF Rx #WHC-2026-79104...')" class="ui-btn-action outline">Download PDF Rx</button>
          </div>
        </div>

        <!-- Section 3: Medication Adherence & Compliance Score -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>📊</span> Section 3: Medication Adherence &amp; Clinical Compliance</h3>
              <div class="ui-section-subtitle">Consistent supplementation directly correlates with healthy birth weight</div>
            </div>
            <span class="ui-badge success">96% Adherence (Excellent)</span>
          </div>
          <div class="ui-grid-4">
            <div class="ui-card" style="padding:18px;text-align:center;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">ACTIVE STREAK</span>
              <div style="font-size:32px;font-weight:900;color:#967BB6;margin:6px 0;">28 Days</div>
              <span style="font-size:12px;color:#64748b;">Zero missed doses in Oct</span>
            </div>
            <div class="ui-card" style="padding:18px;text-align:center;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">IRON COMPLIANCE</span>
              <div style="font-size:32px;font-weight:900;color:#1E0533;margin:6px 0;">98 %</div>
              <span style="font-size:12px;color:#64748b;">Hb stable at 12.4 g/dL</span>
            </div>
            <div class="ui-card" style="padding:18px;text-align:center;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">CALCIUM COMPLIANCE</span>
              <div style="font-size:32px;font-weight:900;color:#1E0533;margin:6px 0;">95 %</div>
              <span style="font-size:12px;color:#64748b;">Bone density preserved</span>
            </div>
            <div class="ui-card" style="padding:18px;text-align:center;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">DHA COMPLIANCE</span>
              <div style="font-size:32px;font-weight:900;color:#1E0533;margin:6px 0;">96 %</div>
              <span style="font-size:12px;color:#64748b;">Fetal biometry supported</span>
            </div>
          </div>
        </div>

        <!-- Section 4: In-House Pharmacy 1-Click Refill & Doorstep Delivery -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🚚</span> Section 4: Hospital In-House Pharmacy Home Delivery</h3>
              <div class="ui-section-subtitle">Genuine temperature-controlled cold-chain medications delivered within Salem</div>
            </div>
            <span class="ui-badge success">Free Delivery Active</span>
          </div>
          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:700;color:#24063E;">Delivery Address: Fairlands, Salem, Tamil Nadu 636016</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">Contact: +91 70107 92745 • Expected dispatch: Same Day within 3 Hours</p>
            </div>
            <button onclick="showToast('Order confirmed. Hospital Pharmacy rider dispatched.')" class="ui-btn-action primary">Dispatch Next Pack</button>
          </div>
        </div>

        <!-- Section 5: Trimester Drug Safety & Contraindication Sentinel -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🛡️</span> Section 5: Trimester Drug Safety &amp; FDA Category Checker</h3>
              <div class="ui-section-subtitle">Real-time checking against pregnancy contraindications and lactation safety</div>
            </div>
            <span class="ui-badge success">Safe for Trimester 2</span>
          </div>
          <div style="background:#f0fdf4;border:1px solid #bbf7d0;border-radius:14px;padding:20px;">
            <div style="font-weight:800;color:#166534;font-size:15px;margin-bottom:6px;">✓ Zero Teratogenic Drugs Detected</div>
            <p style="font-size:13px;color:#15803d;line-height:1.6;">
              All prescribed compounds have been validated against the National Formulary of India (NFI) and FDA Category B standards. No NSAIDs (Ibuprofen), tetracyclines, or ACE inhibitors detected.
            </p>
          </div>
        </div>
    '''
    return build_html("Digital Prescriptions", "Prescription Vault & Medication Schedule", "user-prescriptions.html", False, content)


# ==============================================================================
# 7. USER: user-billing.html (Insurance & Billing)
# ==============================================================================
def create_user_billing():
    content = '''
        <div class="dash-welcome-row">
          <div>
            <h1 class="dash-welcome-title">Insurance, Packages &amp; Billing 💳</h1>
            <p class="dash-welcome-sub">Cashless maternity claim pre-authorizations, transparent delivery packages, and zero hidden costs.</p>
          </div>
          <button onclick="showToast('Generating Consolidated Inpatient Tax Invoice PDF...')" class="ui-btn-action primary">
            <span>📥 DOWNLOAD GST INVOICE</span>
          </button>
        </div>

        <!-- Section 1: Comprehensive Account Summary -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>💰</span> Section 1: Maternity Financial Account Summary</h3>
              <div class="ui-section-subtitle">Transparent billing with zero surprise clinical surcharges</div>
            </div>
            <span class="ui-badge success">Account in Good Standing</span>
          </div>
          <div class="ui-grid-4">
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">ESTIMATED TOTAL PACKAGE</span>
              <div style="font-size:28px;font-weight:900;color:#1E0533;margin:6px 0;">₹ 65,000</div>
              <span style="font-size:12px;color:#64748b;">LDRP Luxury Suite Delivery</span>
            </div>
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">CASHLESS TPA APPROVED</span>
              <div style="font-size:28px;font-weight:900;color:#967BB6;margin:6px 0;">₹ 50,000</div>
              <span style="font-size:12px;color:#64748b;">Star Health Pre-Auth Done</span>
            </div>
            <div class="ui-card" style="padding:18px;">
              <span style="font-size:11px;font-weight:700;color:#64748b;">ADVANCE DEPOSIT PAID</span>
              <div style="font-size:28px;font-weight:900;color:#967BB6;margin:6px 0;">₹ 15,000</div>
              <span style="font-size:12px;color:#64748b;">OPD Booking Receipt #8402</span>
            </div>
            <div class="ui-card" style="padding:18px;background:#f0fdf4;">
              <span style="font-size:11px;font-weight:700;color:#166534;">OUT-OF-POCKET BALANCE</span>
              <div style="font-size:28px;font-weight:900;color:#166534;margin:6px 0;">₹ 0</div>
              <span style="font-size:12px;color:#166534;">Fully Covered under TPA</span>
            </div>
          </div>
        </div>

        <!-- Section 2: TPA Cashless Pre-Authorization Tracker -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🛡️</span> Section 2: Cashless Maternity Insurance Pre-Authorization</h3>
              <div class="ui-section-subtitle">Real-time settlement status with hospital TPA Helpdesk</div>
            </div>
            <span class="ui-badge success">Pre-Auth Approved</span>
          </div>
          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:700;color:#24063E;">Star Health &amp; Allied Insurance — Women Care Policy</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">Policy No: <code>STAR-MAT-9921820</code> • Pre-Auth Approval Code: <code>APPR-SH-77210</code> • Approved Sum: ₹50,000</p>
            </div>
            <button onclick="showToast('Downloading TPA Pre-Authorization Letter...')" class="ui-btn-action outline">Download Letter</button>
          </div>
        </div>

        <!-- Section 3: Itemized Outpatient & Inpatient Billing Ledger -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🧾</span> Section 3: Itemized Ledger &amp; Outpatient Diagnostics</h3>
              <div class="ui-section-subtitle">Every consultation, ultrasound scan, and laboratory test transparently accounted</div>
            </div>
          </div>
          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:14.5px;font-weight:700;color:#1E0533;">Level-2 TIFFA 4D Ultrasound Scan (GE Voluson)</h4>
              <p style="font-size:12.5px;color:#64748b;">Dr. Meera Nair • Oct 10, 2026 • Receipt #RC-10492</p>
            </div>
            <div style="text-align:right;">
              <span style="font-weight:800;color:#1E0533;font-size:15px;">₹ 2,800</span><br>
              <span class="ui-badge success">Paid (UPI)</span>
            </div>
          </div>

          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:14.5px;font-weight:700;color:#1E0533;">Antenatal Comprehensive Blood Work &amp; OGTT Panel</h4>
              <p style="font-size:12.5px;color:#64748b;">NABL Certified Pathology • Sep 28, 2026 • Receipt #RC-09821</p>
            </div>
            <div style="text-align:right;">
              <span style="font-weight:800;color:#1E0533;font-size:15px;">₹ 1,450</span><br>
              <span class="ui-badge success">Paid (UPI)</span>
            </div>
          </div>

          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:14.5px;font-weight:700;color:#1E0533;">Obstetric Specialist Consultation (Dr. Shilpi Singh)</h4>
              <p style="font-size:12.5px;color:#64748b;">OPD Chamber 1 • Sep 14, 2026 • Receipt #RC-08912</p>
            </div>
            <div style="text-align:right;">
              <span style="font-weight:800;color:#1E0533;font-size:15px;">₹ 600</span><br>
              <span class="ui-badge success">Paid (UPI)</span>
            </div>
          </div>
        </div>

        <!-- Section 4: Transparent Maternity Package Cost Estimator -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>📦</span> Section 4: All-Inclusive Delivery Packages (Zero Hidden Charges)</h3>
              <div class="ui-section-subtitle">Includes room stay, pediatrician neonatal checkup, nursing, and medicines</div>
            </div>
          </div>
          <div class="ui-grid-3">
            <div class="ui-card" style="padding:20px;">
              <div style="font-size:12px;font-weight:700;color:#3B0764;">PHYSIOLOGICAL BIRTH</div>
              <h4 style="font-size:18px;font-weight:900;color:#1E0533;margin:6px 0;">Normal Delivery Package</h4>
              <div style="font-size:26px;font-weight:900;color:#3B0764;margin-bottom:12px;">₹ 45,000 <span style="font-size:13px;color:#64748b;font-weight:400;">/ 3 Days Stay</span></div>
              <p style="font-size:13px;color:#64748b;line-height:1.6;">LDRP Birthing suite, doctor fee, midwife care, newborn vaccination, 3 days luxury stay.</p>
            </div>

            <div class="ui-card" style="padding:20px;border:2px solid #967BB6;background:#fffdfa;">
              <div style="font-size:12px;font-weight:700;color:#967BB6;">MOST POPULAR CHOICE</div>
              <h4 style="font-size:18px;font-weight:900;color:#1E0533;margin:6px 0;">LDRP Luxury Birthing Suite</h4>
              <div style="font-size:26px;font-weight:900;color:#967BB6;margin-bottom:12px;">₹ 65,000 <span style="font-size:13px;color:#64748b;font-weight:400;">/ 4 Days Stay</span></div>
              <p style="font-size:13px;color:#64748b;line-height:1.6;">Private luxury suite, partner stay, birthing ball, Lamaze coach, 24/7 dedicated nurse.</p>
            </div>

            <div class="ui-card" style="padding:20px;">
              <div style="font-size:12px;font-weight:700;color:#967BB6;">SURGICAL EXCELLENCE</div>
              <h4 style="font-size:18px;font-weight:900;color:#1E0533;margin:6px 0;">Cesarean (C-Section) Package</h4>
              <div style="font-size:26px;font-weight:900;color:#967BB6;margin-bottom:12px;">₹ 75,000 <span style="font-size:13px;color:#64748b;font-weight:400;">/ 5 Days Stay</span></div>
              <p style="font-size:13px;color:#64748b;line-height:1.6;">Modular OT charges, anesthetist fee, post-op pain management, deluxe private suite.</p>
            </div>
          </div>
        </div>

        <!-- Section 5: Online Payment & Section 80D Tax Receipt -->
        <div class="ui-section-card">
          <div class="ui-section-title-wrap">
            <div class="ui-section-title-group">
              <h3><span>🔒</span> Section 5: Instant Payment Gateway &amp; Section 80D Tax Benefit</h3>
              <div class="ui-section-subtitle">256-Bit SSL encrypted payments eligible for Income Tax Section 80D deduction</div>
            </div>
            <div class="ssl-badge"><span>256–Bit SSL Encrypted</span></div>
          </div>
          <div class="ui-interactive-row">
            <div>
              <h4 style="font-size:15px;font-weight:700;color:#24063E;">Section 80D Preventive Health Checkup Tax Certificate (AY 2026-27)</h4>
              <p style="font-size:13px;color:#64748b;margin-top:2px;">Claim up to ₹5,000 tax deduction for antenatal diagnostic payments under Income Tax Act.</p>
            </div>
            <button onclick="showToast('Downloading 80D Tax Exemption Certificate PDF...')" class="ui-btn-action primary">Download 80D Certificate</button>
          </div>
        </div>
    '''
    return build_html("Insurance & Billing", "Cashless TPA Claims & Maternity Packages", "user-billing.html", False, content)

print("build_user_pages.py defined.")
