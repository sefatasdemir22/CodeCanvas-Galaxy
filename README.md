# 🌌 CodeCanvas: Generative Galaxy

**CodeCanvas: Generative Galaxy** — Python ile yazılmış bir generative art projesidir.
Her çalıştırmada rastgele bir galaksi, yıldız patlaması veya aurora benzeri soyut desen üretir.
Her tablo benzersizdir ve “koddan sanat” felsefesini yansıtır 🎨

---

## 🚀 Özellikler

* Rastgele galaksi isimleri (örnek: *Silent Orbit*, *Crimson Core*)
* Farklı galaksi tipleri: spiral, ring, burst
* Renk modları: Aurora, Solar, Void, Candy
* Tamamen siyah “uzay” arka plan
* Şeffaf PNG çıktılar (kolajlarda kusursuz karışım)
* Otomatik galeri üretimi (`gallery_mode.py`)
* Kolaj birleştirici (`gallery_collage.py`)
* GUI destekli kontrol paneli (`studio.py`)

---

## 🧩 Klasör Yapısı

```
CodeCanvas-Galaxy
│
├── galaxy_generator.py      # Tek galaksi üretimi
├── gallery_mode.py          # 5 galaksi birden üretir
├── gallery_collage.py       # Tüm galaksileri tek kolajda birleştirir
├── studio.py                # GUI (CodeCanvas Studio)
├── outputs/
│   └── gallery/             # Tüm galaksi çıktıları
├── requirements.txt         # Bağımlılıklar
└── README.md
```

---

## 🪄 Kullanım

### 1️⃣ Gereksinimler

```bash
pip install -r requirements.txt
```

### 2️⃣ Tekli galaksi üretimi

```bash
python galaxy_generator.py
```

### 3️⃣ 5 galaksi birden (galeri modu)

```bash
python gallery_mode.py
```

### 4️⃣ Kolaj oluşturma

```bash
python gallery_collage.py
```

→ `outputs/gallery_collage.png` dosyasında uzay temalı kolaj oluşturulur.

### 5️⃣ GUI versiyonu (önerilen)

```bash
python studio.py
```

→ Karanlık arayüzde “Yeni Galaksi Üret”, “Galeri (5) Üret” ve “Kolaj Oluştur” butonlarıyla
tam bir **generative art stüdyosu** deneyimi yaşanır.

---

## ✨ Örnek Çıktılar

* Dream Pulse — Solar Ring
* Fractal Pulse — Candy Spiral
* Luminous Drift — Solar Ring
* Quantum Core — Void Burst

<p align="center">
  <img src="outputs/gallery_collage.png" width="500">
</p>

---

## 💡 Geliştirme Fikirleri (v5+)

* Arka plan yıldız tozu / nebula efekti
* Renk temalarına manuel seçim
* Galaksi tipini kullanıcı seçimi
* Galeriye sesli/animasyonlu versiyonlar
* SVG / Video export
* Online galeri veya NFT entegrasyonu

---

## 📜 Lisans

Bu proje [MIT License](LICENSE) kapsamında paylaşılmıştır.
Kodun açık, eğitici ve özgürce yeniden kullanılabilir olmasını destekler.

```
MIT License

Copyright (c) 2025 Sefa Taşdemir

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

> ✨ *Part of CodeCanvas: Sefa’s Generative Art Studio*
