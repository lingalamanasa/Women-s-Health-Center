import urllib.request
import io
import os
from PIL import Image

os.makedirs('assets/img', exist_ok=True)

# Map of target file to Sanity CDN image URL
blog_images = {
    'blog-1.webp': 'https://cdn.sanity.io/images/0qpyiixn/production/0d113034624421e65dbeb192fd47e65bc322a4bd-1376x768.jpg?rect=112,0,1152,768&w=1200&h=800&fit=crop&auto=format',
    'blog-2.webp': 'https://cdn.sanity.io/images/0qpyiixn/production/11cdd96716a58a35333b98b5f7d3bb23281e1042-1376x768.jpg?rect=112,0,1152,768&w=1200&h=800&fit=crop&auto=format',
    'blog-3.webp': 'https://cdn.sanity.io/images/0qpyiixn/production/2b1e62527f95d9d049cb1a6fa3b71cbc128cc40a-1376x768.jpg?rect=112,0,1152,768&w=1200&h=800&fit=crop&auto=format',
    'blog-4.webp': 'https://cdn.sanity.io/images/0qpyiixn/production/1d92ba6ed19c3a04b853b60973025c933d6e882b-1376x768.jpg?rect=112,0,1152,768&w=1200&h=800&fit=crop&auto=format',
    'blog-5.webp': 'https://cdn.sanity.io/images/0qpyiixn/production/6170fd8dd43ca97fad7ff825a45ad582d80513d4-1376x768.jpg?rect=112,0,1152,768&w=1200&h=800&fit=crop&auto=format',
    'blog-6.webp': 'https://cdn.sanity.io/images/0qpyiixn/production/874e6d47e6ff0e145987d1af1e68ea83abe7abdf-1376x768.jpg?rect=112,0,1152,768&w=1200&h=800&fit=crop&auto=format',
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for fname, url in blog_images.items():
    dest_path = os.path.join('assets', 'img', fname)
    print(f"Downloading {fname} from {url}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
        
        # Open with PIL and compress to WebP under 100KB
        img = Image.open(io.BytesIO(data)).convert('RGB')
        # Resize to max 1200 width maintaining aspect ratio
        if img.width > 1200:
            new_h = int(img.height * (1200 / img.width))
            img = img.resize((1200, new_h), Image.Resampling.LANCZOS)
        
        # Save as WebP with quality to stay under 95KB
        for q in [82, 78, 72, 65, 58]:
            buf = io.BytesIO()
            img.save(buf, format='WEBP', quality=q)
            size = buf.tell()
            if size < 95000:
                with open(dest_path, 'wb') as f:
                    f.write(buf.getvalue())
                print(f"Saved {fname}: {size/1024:.1f} KB (quality={q})")
                break
        else:
            with open(dest_path, 'wb') as f:
                f.write(buf.getvalue())
            print(f"Saved {fname}: {buf.tell()/1024:.1f} KB")

    except Exception as e:
        print(f"Error downloading {fname}: {e}")
