import numpy as np
import matplotlib.pyplot as plt
import colorsys, random, os

# --- Galaksi ismi ---
prefixes = ["Quantum","Dream","Silent","Eternal","Crimson","Void","Luminous","Fractal"]
suffixes = ["Nebula","Storm","Orbit","Whisper","Pulse","Core","Drift","Spiral"]
name = random.choice(prefixes) + " " + random.choice(suffixes)

# --- Renk modları ---
color_modes = {
    "Aurora": [(0.4,1.0,0.8),(0.3,0.8,1.0),(0.7,0.5,1.0)],
    "Solar":  [(1.0,0.6,0.1),(1.0,0.8,0.4),(1.0,0.2,0.0)],
    "Void":   [(0.7,0.7,1.0),(0.3,0.3,0.6),(0.1,0.1,0.3)],
    "Candy":  [(1.0,0.6,0.9),(0.7,0.3,1.0),(0.9,0.4,0.6)],
}
mode_name = random.choice(list(color_modes.keys()))
base_colors = color_modes[mode_name]

def random_color_from_mode():
    r,g,b = random.choice(base_colors)
    h,s,v = colorsys.rgb_to_hsv(r,g,b)
    h = (h + random.uniform(-0.05,0.05)) % 1.0
    s = min(1.0, max(0.0, s + random.uniform(-0.1,0.1)))
    v = min(1.0, max(0.0, v + random.uniform(-0.1,0.1)))
    return colorsys.hsv_to_rgb(h,s,v)

colors = [random_color_from_mode() for _ in range(5)]
shape  = random.choice(["spiral","ring","burst"])

# --- Noktaları üret ---
n_points = 10000
theta = np.linspace(0, 8*np.pi, n_points)

if shape == "spiral":
    r = np.linspace(0.1,1,n_points)**2.5
    x = r*np.cos(theta) + np.random.normal(0,0.03,n_points)
    y = r*np.sin(theta) + np.random.normal(0,0.03,n_points)
elif shape == "ring":
    r = np.ones(n_points)*0.7 + np.random.normal(0,0.05,n_points)
    x = r*np.cos(theta) + np.random.normal(0,0.02,n_points)
    y = r*np.sin(theta) + np.random.normal(0,0.02,n_points)
else:  # burst
    x = np.random.normal(0,0.5,n_points)
    y = np.random.normal(0,0.5,n_points)
    r = np.sqrt(x**2 + y**2)
    m = r < 1
    x, y = x[m], y[m]

# --- Görselleştir ---
plt.style.use("dark_background")
fig, ax = plt.subplots(figsize=(8,8))
ax.set_axis_off()
fig.patch.set_alpha(0.0)
ax.set_facecolor((0,0,0,0))

for i in range(5):
    ax.scatter(
        x + np.random.normal(0,0.05,len(x)),
        y + np.random.normal(0,0.05,len(x)),
        s=np.random.randint(1,4),
        color=colors[i],
        alpha=0.28
    )

ax.set_title(f"{name} [{mode_name} - {shape}]", color="white", fontsize=14, pad=20)

# --- Kayıt klasörü ---
# Varsayılan olarak outputs/gallery'ye kaydeder
gallery_mode_env = os.environ.get("GALLERY_MODE", "0")
if gallery_mode_env == "1":
    output_dir = os.path.join("outputs", "gallery")
else:
    # Varsayılan olarak da artık gallery'yi kullanıyoruz
    output_dir = os.path.join("outputs", "gallery")

os.makedirs(output_dir, exist_ok=True)

filename = f"{name.replace(' ','_')}_{shape}_{mode_name}.png"
filepath = os.path.join(output_dir, filename)

# --- Kaydet ---
plt.savefig(filepath, dpi=300, bbox_inches="tight", transparent=True)
plt.close()

print(f"✨ Yeni galaksi kaydedildi: {filepath}")
