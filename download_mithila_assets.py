import re
import urllib.parse
import urllib.request
import os
import io
from PIL import Image

content_path = r'C:\Users\manu1\.gemini\antigravity-ide\brain\7384924f-a2c2-40b6-acec-c75ef3d792d7\.system_generated\steps\7\content.md'
with open(content_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Find all url=%2F... patterns and src="..."
matches = re.findall(r'url=([^&"\'\s]+)', text)
decoded = set()
for m in matches:
    dec = urllib.parse.unquote(m)
    if dec.startswith('/assets') or dec.endswith('.webp') or dec.endswith('.png') or dec.endswith('.jpg'):
        decoded.add(dec)

# Also check directly in text for /assets/img/...
direct = re.findall(r'(/assets/img/[a-zA-Z0-9_\-\.]+\.(?:webp|png|jpg|jpeg))', text)
for d in direct:
    decoded.add(d)

print(f"Total unique assets found: {len(decoded)}")
for d in sorted(decoded):
    print(" -", d)

base_url = "https://www.mithilawomenshospital.in"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

os.makedirs('assets/img', exist_ok=True)

for path in sorted(decoded):
    filename = os.path.basename(path)
    # Ensure webp extension
    name, ext = os.path.splitext(filename)
    target_filename = f"{name}.webp"
    target_path = os.path.join('assets/img', target_filename)
    
    full_url = base_url + path
    try:
        req = urllib.request.Request(full_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            
            # Open with PIL
            img = Image.open(io.BytesIO(data))
            
            # Convert to RGB if RGBA and saving webp or keep RGBA
            # Resize if very huge so it fits under 100kb
            max_dim = 1600
            if img.width > max_dim or img.height > max_dim:
                img.thumbnail((max_dim, max_dim), Image.Resampling.LANCZOS)
                
            # Save as WebP under 100kb
            quality = 82
            img.save(target_path, 'WEBP', quality=quality)
            
            size_kb = os.path.getsize(target_path) / 1024
            while size_kb > 95 and quality > 30:
                quality -= 10
                img.save(target_path, 'WEBP', quality=quality)
                size_kb = os.path.getsize(target_path) / 1024
                
            print(f"Downloaded & optimized {target_filename}: {size_kb:.1f} KB (quality={quality})")
    except Exception as e:
        print(f"Failed to fetch {full_url}: {e}")
