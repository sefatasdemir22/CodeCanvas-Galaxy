import os
from datetime import datetime
from math import ceil, sqrt
from PIL import Image, ImageDraw, ImageFont

# --- Galeri dizini ---
gallery_dir = os.environ.get("GALLERY_DIR", "outputs/gallery")
output_file = "outputs/gallery_collage.png"

# --- Görselleri yükle ---
images = []
for filename in sorted(os.listdir(gallery_dir)):
    if filename.lower().endswith(".png"):
        images.append((filename, Image.open(os.path.join(gallery_dir, filename))))

if not images:
    raise RuntimeError(f"⚠️ '{gallery_dir}' klasöründe PNG dosyası bulunamadı.")

# --- Grid hesaplama ---
n = len(images)
cols = ceil(sqrt(n))
rows = ceil(n / cols)
thumb_size = 480
label_h = 30  # her görselin altına yazı için alan

collage_w = cols * thumb_size
collage_h = rows * (thumb_size + label_h) + 150  # başlık + footer

# --- Siyah uzay arka planı ---
collage = Image.new("RGB", (collage_w, collage_h), (5, 5, 15))

# --- Font ayarları ---
try:
    font_title = ImageFont.truetype("arial.ttf", 28)
    font_sub = ImageFont.truetype("arial.ttf", 22)
    font_label = ImageFont.truetype("arial.ttf", 16)
except:
    font_title = ImageFont.load_default()
    font_sub = ImageFont.load_default()
    font_label = ImageFont.load_default()

# --- Görselleri yerleştir ---
draw = ImageDraw.Draw(collage)
for idx, (filename, img) in enumerate(images):
    name = os.path.splitext(filename)[0].replace("_", " ")
    img = img.resize((thumb_size, thumb_size))
    x = (idx % cols) * thumb_size
    y = (idx // cols) * (thumb_size + label_h) + 80
    img_rgba = img.convert("RGBA")
    collage.paste(img_rgba, (x, y), img_rgba)


    # İsim etiketi (Pillow sürümüne göre uyumlu)
    if hasattr(draw, "textbbox"):
        bbox = draw.textbbox((0, 0), name, font=font_label)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    else:
        w, h = draw.textsize(name, font=font_label)

    draw.text(
        (x + (thumb_size - w) / 2, y + thumb_size + 5),
        name,
        fill=(200, 200, 255),
        font=font_label,
    )

# --- Başlık ---
title = "CodeCanvas: Generative Galaxy 🌌"
subtitle = f"v3.4.1 – {n} Cosmic Works"

draw.text((20, 20), title, fill=(255, 255, 255), font=font_title)
draw.text((20, 52), subtitle, fill=(180, 180, 200), font=font_sub)

# --- Footer ---
footer_text = f"© CodeCanvas – Sefa’s Generative Art Studio – {datetime.now().year}"
if hasattr(draw, "textbbox"):
    bbox = draw.textbbox((0, 0), footer_text, font=font_sub)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
else:
    w, h = draw.textsize(footer_text, font=font_sub)

draw.text(
    ((collage_w - w) // 2, collage_h - h - 25),
    footer_text,
    fill=(180, 180, 200),
    font=font_sub,
)

# --- Kaydet ---
collage.save(output_file, "PNG")
print(f"🌌 {n} galaksi siyah zeminli kolaj olarak kaydedildi: {output_file}")
