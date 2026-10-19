import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

os.makedirs('assets/img', exist_ok=True)

def create_gradient(width, height, color1, color2, direction='vertical'):
    base = Image.new('RGB', (width, height), color1)
    top = Image.new('RGB', (width, height), color2)
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        for x in range(width):
            if direction == 'vertical':
                val = int(255 * (y / height))
            elif direction == 'horizontal':
                val = int(255 * (x / width))
            elif direction == 'diagonal':
                val = int(255 * ((x + y) / (width + height)))
            else: # radial
                cx, cy = width / 2, height / 2
                dist = math.sqrt((x - cx)**2 + (y - cy)**2)
                max_dist = math.sqrt(cx**2 + cy**2)
                val = min(255, int(255 * (dist / max_dist)))
            mask_data.append(val)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

def draw_stackly_mark(draw, x, y, scale=1.0, color=(245, 158, 11)):
    # Draw the characteristic curved golden 'S' ribbon of Stackly
    s = scale
    pts1 = [
        (x + 20*s, y + 5*s),
        (x + 40*s, y + 5*s),
        (x + 45*s, y + 15*s),
        (x + 30*s, y + 25*s),
        (x + 10*s, y + 35*s),
        (x + 5*s, y + 45*s),
        (x + 15*s, y + 55*s),
        (x + 35*s, y + 55*s),
    ]
    # Draw smooth pill segments
    draw.rounded_rectangle([x + 12*s, y + 4*s, x + 38*s, y + 18*s], radius=int(6*s), fill=color)
    draw.rounded_rectangle([x + 6*s, y + 18*s, x + 24*s, y + 34*s], radius=int(6*s), fill=color)
    draw.rounded_rectangle([x + 18*s, y + 30*s, x + 36*s, y + 44*s], radius=int(6*s), fill=color)
    draw.rounded_rectangle([x + 4*s, y + 42*s, x + 30*s, y + 56*s], radius=int(6*s), fill=color)

def generate_logo():
    # Keep the authentic official Stackly brand assets
    icon_path = 'assets/img/stackly-icon.webp'
    if os.path.exists(icon_path):
        icon = Image.open(icon_path).convert('RGBA')
        # Generate favicon/logo if needed
        save_webp(icon, 'assets/img/logo.webp', quality=90)
    print("Stackly official logo assets preserved.")

def save_webp(img, filepath, quality=80):
    img.save(filepath, 'WEBP', quality=quality)
    size_kb = os.path.getsize(filepath) / 1024
    if size_kb > 95:
        # Re-save with lower quality to guarantee under 100kb
        img.save(filepath, 'WEBP', quality=65)
        size_kb = os.path.getsize(filepath) / 1024
    print(f"Saved {filepath} ({size_kb:.1f} KB)")

def generate_medical_card_image(title, subtitle, tag, color1, color2, icon_type, filepath, width=720, height=480):
    img = create_gradient(width, height, color1, color2, direction='diagonal')
    draw = ImageDraw.Draw(img)
    
    # Modern subtle abstract geometric overlays (medical circles, pulse grids, cross motifs)
    cx, cy = width - 180, height // 2
    for r in range(40, 260, 35):
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(255, 255, 255, 30), width=2)
        
    # Subtle medical grid pattern
    for x in range(0, width, 40):
        draw.line([(x, 0), (x, height)], fill=(255, 255, 255, 10), width=1)
    for y in range(0, height, 40):
        draw.line([(0, y), (width, y)], fill=(255, 255, 255, 10), width=1)

    # Medical cross / heart beat motif
    mx, my = cx, cy
    draw.line([(mx - 80, my), (mx - 30, my), (mx - 15, my - 45), (mx + 10, my + 55), (mx + 30, my - 25), (mx + 50, my), (mx + 90, my)], fill=(245, 158, 11), width=4)
    
    # Glassmorphism badge on left
    draw.rounded_rectangle([40, 40, width - 40, height - 40], radius=16, outline=(255, 255, 255, 60), width=1)
    
    # Tag pill
    draw.rounded_rectangle([70, 70, 70 + len(tag)*10 + 30, 105], radius=18, fill=(245, 158, 11))
    
    try:
        font_tag = ImageFont.truetype("arialbd.ttf", 13)
        font_title = ImageFont.truetype("arialbd.ttf", 30)
        font_sub = ImageFont.truetype("arial.ttf", 16)
        font_badge = ImageFont.truetype("arialbd.ttf", 14)
    except:
        font_tag = ImageFont.load_default()
        font_title = font_tag
        font_sub = font_tag
        font_badge = font_tag

    draw.text((85, 78), tag.upper(), fill=(17, 24, 39), font=font_tag)
    
    # Wrap title if long
    words = title.split()
    line1 = " ".join(words[:4])
    line2 = " ".join(words[4:]) if len(words) > 4 else ""
    
    draw.text((70, 130), line1, fill=(255, 255, 255), font=font_title)
    if line2:
        draw.text((70, 175), line2, fill=(255, 255, 255), font=font_title)
        
    draw.text((70, 235), subtitle, fill=(229, 231, 235), font=font_sub)
    
    # Bottom accreditation pill
    draw.rounded_rectangle([70, height - 110, 310, height - 70], radius=10, fill=(0, 0, 0, 120))
    draw.text((85, height - 98), "★ NABH & ISO 9001 ACCREDITED", fill=(253, 224, 71), font=font_badge)
    
    # Save webp
    save_webp(img, filepath, quality=80)

def generate_doctor_portrait(name, degree, specialty, exp, filepath):
    width, height = 480, 560
    # Clean warm medical gradient background
    img = create_gradient(width, height, (249, 250, 251), (224, 231, 255), direction='vertical')
    draw = ImageDraw.Draw(img)
    
    # Draw soft halo glow
    draw.ellipse([width//2 - 180, 50, width//2 + 180, 410], fill=(238, 242, 255))
    draw.ellipse([width//2 - 140, 90, width//2 + 140, 370], fill=(219, 234, 254))
    
    # Doctor stylized clinical portrait silhouette
    # Head & shoulders
    cx = width // 2
    # Stethoscope & doctor coat
    draw.rounded_rectangle([cx - 110, 270, cx + 110, 500], radius=40, fill=(255, 255, 255), outline=(209, 213, 219), width=2)
    # Head
    draw.ellipse([cx - 65, 120, cx + 65, 250], fill=(245, 208, 178))
    # Hair
    draw.chord([cx - 70, 110, cx + 70, 210], 180, 360, fill=(55, 48, 43))
    # Doctor scrubs / tie
    draw.polygon([(cx - 30, 270), (cx + 30, 270), (cx, 340)], fill=(13, 148, 136))
    # Stethoscope loop
    draw.arc([cx - 50, 290, cx + 50, 390], 0, 180, fill=(75, 85, 99), width=4)
    draw.ellipse([cx - 8, 385, cx + 8, 401], fill=(156, 163, 175))
    
    # Bottom badge
    draw.rounded_rectangle([30, height - 120, width - 30, height - 20], radius=16, fill=(17, 24, 39))
    
    try:
        font_name = ImageFont.truetype("arialbd.ttf", 20)
        font_sub = ImageFont.truetype("arial.ttf", 13)
        font_gold = ImageFont.truetype("arialbd.ttf", 12)
    except:
        font_name = ImageFont.load_default()
        font_sub = font_name
        font_gold = font_name
        
    draw.text((45, height - 108), name, fill=(255, 255, 255), font=font_name)
    draw.text((45, height - 82), f"{degree} • {specialty}", fill=(209, 213, 219), font=font_sub)
    draw.text((45, height - 58), f"Experience: {exp} | 5★ Trusted Care", fill=(245, 158, 11), font=font_gold)
    
    save_webp(img, filepath, quality=80)

def generate_telemetry_banner(filepath, title_text):
    # Preview banner matching screenshot 3 and 4
    width, height = 720, 260
    img = create_gradient(width, height, (15, 23, 42), (17, 24, 39), direction='diagonal')
    draw = ImageDraw.Draw(img)
    
    # Draw telemetry charts and grid lines
    for x in range(20, width, 40):
        draw.line([(x, 20), (x, height - 20)], fill=(30, 41, 59), width=1)
    for y in range(20, height, 30):
        draw.line([(20, y), (width - 20, y)], fill=(30, 41, 59), width=1)
        
    # Top stats widgets
    widgets = [
        ("ACTIVE PATIENTS", "1,420", "+12.4%"),
        ("NORMAL DELIVERIES", "98.4%", "Safe Motherhood"),
        ("NICU READINESS", "100%", "Level-3 Ready"),
        ("EMERGENCY RESPONSE", "2.1 min", "Immediate")
    ]
    wx = 40
    for w_title, w_val, w_sub in widgets:
        draw.rounded_rectangle([wx, 25, wx + 145, 85], radius=8, fill=(30, 41, 59), outline=(51, 65, 85), width=1)
        draw.text((wx + 10, 32), w_title[:15], fill=(148, 163, 184))
        draw.text((wx + 10, 48), w_val, fill=(245, 158, 11))
        draw.text((wx + 10, 68), w_sub, fill=(52, 211, 153))
        wx += 160
        
    # Area chart curve
    points = [
        (40, 200), (90, 180), (150, 190), (220, 140), (290, 155), 
        (360, 110), (430, 130), (510, 95), (590, 115), (680, 85)
    ]
    for i in range(len(points)-1):
        draw.line([points[i], points[i+1]], fill=(245, 158, 11), width=3)
        draw.ellipse([points[i][0]-3, points[i][1]-3, points[i][0]+3, points[i][1]+3], fill=(255, 255, 255))
    draw.ellipse([points[-1][0]-4, points[-1][1]-4, points[-1][0]+4, points[-1][1]+4], fill=(245, 158, 11))
    
    # Bottom badge
    draw.rounded_rectangle([40, height - 45, width - 40, height - 15], radius=6, fill=(0, 0, 0, 160))
    try:
        font_b = ImageFont.truetype("arialbd.ttf", 12)
    except:
        font_b = ImageFont.load_default()
    draw.text((55, height - 38), f"⚡ {title_text}", fill=(255, 255, 255), font=font_b)
    
    save_webp(img, filepath, quality=80)

# Generate all required graphics
print("Generating Stackly Logos...")
generate_logo()

print("Generating Hero and Section Banners...")
generate_medical_card_image(
    "World-Class Maternity & Painless Delivery", 
    "Comprehensive Obstetric Care with 24x7 High-Risk Surgical Readiness", 
    "Obstetrics & Gynecology", 
    (30, 41, 59), (15, 23, 42), "cross", "assets/img/gen_hero-1.webp", 1200, 680
)

generate_medical_card_image(
    "Advanced Laparoscopic & Robotic Surgery", 
    "Keyhole Gynae Surgeries with Same-Day Discharge & Minimal Discomfort", 
    "Minimally Invasive OT", 
    (19, 78, 74), (15, 23, 42), "cross", "assets/img/gen_hero-2.webp", 1200, 680
)

generate_medical_card_image(
    "High-Risk Pregnancy & Fetal Anomaly Scans", 
    "Precision 3D/4D Color Doppler Imaging with Maternal-Fetal Specialists", 
    "Fetal Medicine Suite", 
    (55, 48, 163), (15, 23, 42), "cross", "assets/img/gen_hero-3.webp", 1200, 680
)

generate_medical_card_image(
    "Stackly Women's Health Center", 
    "Trusted Gynecology, Maternity & Fertility Care 24/7", 
    "Welcome to Stackly", 
    (24, 24, 27), (63, 63, 70), "cross", "assets/img/gen_hero_mobile.webp", 640, 640
)

print("Generating Specialty Service Images...")
services = [
    ("Painless Normal Delivery", "Epidural analgesia & gentle birth suites", "Obstetrics", (244, 63, 94), (136, 19, 55), "service-maternity.webp"),
    ("Advanced Laparoscopy", "Keyhole removal of cysts, fibroids & endo", "Surgical Care", (13, 148, 136), (15, 23, 42), "service-laparoscopy.webp"),
    ("IVF & Reproductive Clinic", "Advanced fertility evaluation, IUI & IVF", "Fertility Suite", (124, 58, 237), (76, 29, 149), "service-fertility.webp"),
    ("4D Fetal Ultrasound", "State-of-the-art anomaly scans & genetic screening", "Diagnostics", (2, 132, 199), (12, 74, 110), "service-ultrasound.webp"),
    ("PCOS & Hormonal Care", "Holistic management of cycle, weight & fertility", "Endocrinology", (217, 119, 6), (120, 53, 15), "service-pcos.webp"),
    ("Preventive Cancer Screening", "Pap smears, HPV vaccines & mammography", "Well-Woman", (16, 185, 129), (6, 78, 59), "service-cancer-screening.webp"),
    ("Level-3 Neonatal ICU (NICU)", "24x7 expert neonatology & premature baby care", "Pediatric NICU", (225, 29, 72), (76, 5, 25), "service-nicu.webp"),
    ("Menopause & Pelvic Floor", "HRT consultation, prolapse care & strengthening", "Wellness", (109, 40, 217), (49, 46, 129), "service-menopause.webp"),
    ("Laminar Airflow Modular OT", "Ultra-sterile surgical suites with HD laparoscopy towers", "Facility OT", (30, 41, 59), (15, 23, 42), "facility-ot.webp"),
    ("Luxury LDRP Suites", "Single-room labor, delivery, recovery and postpartum stay", "Comfort Care", (88, 28, 135), (24, 24, 27), "facility-suite.webp"),
]

for title, sub, tag, c1, c2, fname in services:
    generate_medical_card_image(title, sub, tag, c1, c2, "icon", f"assets/img/{fname}", 640, 420)

print("Generating Doctor Profiles...")
doctors = [
    ("Dr. Shilpi Singh", "MS (OBG), MBBS", "Senior Obstetrician & Gynecologist", "18+ Yrs", "assets/img/shilpi-singh.webp"),
    ("Dr. Ananya Sen", "DNB, FMAS", "Fertility & Laparoscopic Surgeon", "14+ Yrs", "assets/img/dr-ananya.webp"),
    ("Dr. Meera Nair", "MD (OBG), FMF", "Maternal-Fetal Medicine Specialist", "12+ Yrs", "assets/img/dr-meera.webp"),
    ("Dr. Priya Sharma", "MBBS, DGO", "Adolescent & Preventive Health Specialist", "10+ Yrs", "assets/img/dr-priya.webp")
]

for name, deg, spec, exp, path in doctors:
    generate_doctor_portrait(name, deg, spec, exp, path)

print("Generating Blog & Telemetry Images...")
generate_medical_card_image("Painless Delivery Demystified", "Everything you need to know about epidural analgesia", "Maternity Guide", (244, 63, 94), (76, 5, 25), "blog", "assets/img/blog-1.webp", 600, 380)
generate_medical_card_image("Reversing PCOS Naturally", "Medical lifestyle & hormonal rebalancing insights", "Endocrine Health", (217, 119, 6), (69, 26, 3), "blog", "assets/img/blog-2.webp", 600, 380)
generate_medical_card_image("Cervical Cancer Screening", "Why Pap smears & HPV vaccines save lives", "Preventive Care", (16, 185, 129), (4, 47, 46), "blog", "assets/img/blog-3.webp", 600, 380)
generate_medical_card_image("Laparoscopic Surgery Recovery", "Key benefits of keyhole surgery for fibroids", "Surgical Insights", (13, 148, 136), (15, 23, 42), "blog", "assets/img/blog-4.webp", 600, 380)

generate_telemetry_banner("assets/img/telemetry-preview.webp", "Live Patient Health Telemetry & Care Cloud")
generate_telemetry_banner("assets/img/admin-preview.webp", "Hospital Analytics, Bed Occupancy & OT Telemetry Engine")

print("All WebP assets generated successfully!")
