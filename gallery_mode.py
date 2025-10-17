import os
import subprocess

# Galeri çıktısı için mod belirle
os.environ["GALLERY_MODE"] = "1"

# Kaç galaksi üretileceğini belirle
num_galaxies = 5
print(f"🚀 {num_galaxies} yeni galaksi oluşturuluyor...\n")

for i in range(num_galaxies):
    print(f"✨ {i+1}. galaksi oluşturuluyor...")
    env = os.environ.copy()
    env["GALLERY_MODE"] = "1"
    subprocess.run(["python", "galaxy_generator.py"], env=env)

print("\n🌌 Galeri tamamlandı! Görseller outputs/gallery klasöründe.")
