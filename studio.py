import tkinter as tk
from tkinter import simpledialog, messagebox
import subprocess
import os
from datetime import datetime

root = tk.Tk()
root.title("CodeCanvas Studio – Generative Galaxy")
root.geometry("480x400")
root.config(bg="#0b0b1a")

# --- Başlık ---
title = tk.Label(
    root,
    text="🚀 CodeCanvas Studio",
    font=("Segoe UI", 20, "bold"),
    fg="white",
    bg="#0b0b1a",
)
title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Generative Galaxy Control Panel",
    font=("Segoe UI", 11),
    fg="#aaa",
    bg="#0b0b1a",
)
subtitle.pack()


# --- Stil fonksiyonu ---
def styled_button(master, text, command):
    return tk.Button(
        master,
        text=text,
        font=("Segoe UI", 12, "bold"),
        bg="#1c1c2e",
        fg="white",
        activebackground="#26263d",
        activeforeground="#00ffff",
        bd=0,
        relief="flat",
        padx=20,
        pady=10,
        cursor="hand2",
        command=command,
    )


# --- Script çalıştırıcı ---
def run_script(script_name, success_msg, env=None):
    try:
        subprocess.run(["python", script_name], check=True, env=env)
        messagebox.showinfo("Başarılı 🎨", success_msg)
    except subprocess.CalledProcessError:
        messagebox.showerror("Hata 💥", f"{script_name} çalıştırılırken hata oluştu.")
    except FileNotFoundError:
        messagebox.showerror("Eksik Dosya", f"{script_name} bulunamadı.")


# --- Tekli galaksi üretimi ---
def generate_single():
    env = os.environ.copy()
    env["GALLERY_MODE"] = "1"  # outputs/gallery içine kaydeder
    run_script("galaxy_generator.py", "Yeni galaksi üretildi! ✨", env)


# --- Galeri üretimi ---
def generate_gallery():
    run_script("gallery_mode.py", "Galeri oluşturuldu! 🚀")


# --- Kolaj oluşturma ---
def generate_collage():
    gallery_path = "outputs/gallery"
    if not os.path.exists(gallery_path):
        messagebox.showwarning("Uyarı", "Önce galeri oluşturmalısın!")
        return

    images = [f for f in os.listdir(gallery_path) if f.endswith(".png")]
    if not images:
        messagebox.showinfo("Bilgi", "Galeride hiç görsel yok!")
        return

    count = simpledialog.askinteger(
        "Kolaj Sayısı", f"Kaç galaksiyi kolajlamak istiyorsun? (1–{len(images)})", minvalue=1, maxvalue=len(images)
    )
    if not count:
        return

    # Geçici olarak sadece son 'count' kadarını kopyalayalım
    temp_dir = os.path.join(gallery_path, "_temp_collage")
    os.makedirs(temp_dir, exist_ok=True)

    images_sorted = sorted(images, key=lambda x: os.path.getmtime(os.path.join(gallery_path, x)))
    selected = images_sorted[-count:]

    for f in os.listdir(temp_dir):
        os.remove(os.path.join(temp_dir, f))
    for img in selected:
        src = os.path.join(gallery_path, img)
        dst = os.path.join(temp_dir, img)
        with open(src, "rb") as s, open(dst, "wb") as d:
            d.write(s.read())

    # Geçici klasörü galeri dizini olarak kullan
    env = os.environ.copy()
    env["GALLERY_DIR"] = temp_dir
    run_script("gallery_collage.py", f"{count} galaksi ile kolaj oluşturuldu! 🖼️", env)


# --- Butonlar ---
btn_single = styled_button(root, "🪐  Yeni Galaksi Üret", generate_single)
btn_gallery = styled_button(root, "🌠  Galeri (5) Üret", generate_gallery)
btn_collage = styled_button(root, "🖼️  Kolaj Oluştur", generate_collage)

btn_single.pack(pady=15)
btn_gallery.pack(pady=5)
btn_collage.pack(pady=5)

# --- Footer ---
footer = tk.Label(
    root,
    text=f"© CodeCanvas – Sefa’s Generative Art Studio – {datetime.now().year}",
    font=("Segoe UI", 9),
    fg="#666",
    bg="#0b0b1a",
)
footer.pack(side="bottom", pady=15)

root.mainloop()
