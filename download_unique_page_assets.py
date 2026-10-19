import urllib.request
import io
import os
from PIL import Image

os.makedirs('assets/img', exist_ok=True)

new_images = {
    'about-hero.webp': 'https://cdn.sanity.io/images/0qpyiixn/production/d69004fc198f9fc8674190f0ab126ab8c2a3c5ae-1376x768.jpg?rect=176,0,1024,768&w=1200&h=800&fit=crop&auto=format',
    'about-surgery.webp': 'https://cdn.sanity.io/images/0qpyiixn/production/309da53d7eae4828e10d9ebea445960861615fc5-1376x768.jpg?rect=176,0,1024,768&w=1200&h=800&fit=crop&auto=format',
    'service-hero.webp': 'https://cdn.sanity.io/images/0qpyiixn/production/b1eb6ba8b31a6798fa24160af0ad6e5f8bc01342-1376x768.jpg?rect=176,0,1024,768&w=1200&h=800&fit=crop&auto=format',
    'service-pcos-real.webp': 'https://cdn.sanity.io/images/0qpyiixn/production/d2ed2eb034e94f2b1d2758b57e9bd1add1bc2ab2-1024x1024.jpg?rect=0,128,1024,768&w=1000&h=750&fit=crop&auto=format',
    'service-ultrasound-real.webp': 'https://cdn.sanity.io/images/0qpyiixn/production/11a8d8ea2a52ab8d14075aad28a3f95aec5ed9d9-1024x1024.jpg?rect=0,128,1024,768&w=1000&h=750&fit=crop&auto=format',
    'service-cancer-real.webp': 'https://cdn.sanity.io/images/0qpyiixn/production/8e00a913f27e9f756cd271ab2c8eead4a8483ad5-1024x1024.jpg?rect=0,128,1024,768&w=1000&h=750&fit=crop&auto=format',
    'contact-hero.webp': 'https://cdn.sanity.io/images/0qpyiixn/production/fae1fd53bff948fe4b6941fec710e9b526493f51-1024x1024.jpg?rect=0,128,1024,768&w=1200&h=800&fit=crop&auto=format',
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for fname, url in new_images.items():
    dest_path = os.path.join('assets', 'img', fname)
    print(f"Downloading {fname}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
        img = Image.open(io.BytesIO(data)).convert('RGB')
        if img.width > 1200:
            new_h = int(img.height * (1200 / img.width))
            img = img.resize((1200, new_h), Image.Resampling.LANCZOS)
        for q in [82, 76, 70, 62]:
            buf = io.BytesIO()
            img.save(buf, format='WEBP', quality=q)
            if buf.tell() < 95000:
                with open(dest_path, 'wb') as f:
                    f.write(buf.getvalue())
                print(f"Saved {fname}: {buf.tell()/1024:.1f} KB (quality={q})")
                break
        else:
            with open(dest_path, 'wb') as f:
                f.write(buf.getvalue())
            print(f"Saved {fname}: {buf.tell()/1024:.1f} KB")
    except Exception as e:
        print(f"Error {fname}: {e}")
