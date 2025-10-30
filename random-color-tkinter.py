import tkinter as tk
import random

# Rastgele renk seç
def rastgele_renk():
    renkler = ["red", "green", "blue", "yellow", "purple", "orange", "pink"]
    return random.choice(renkler)

# Butona tıklanınca çalışacak fonksiyon
def butona_tikla():
    global puan
    puan += 1
    puan_label.config(text=f"Puan: {puan}")
    pencere.config(bg=rastgele_renk())

# Ana pencere
pencere = tk.Tk()
pencere.title("🎯 Renkli Buton Oyunu")
pencere.geometry("400x300")

puan = 0

# Puan etiketi
puan_label = tk.Label(pencere, text="Puan: 0", font=("Helvetica", 20))
puan_label.pack(pady=20)

# Tıklanabilir buton
oyun_butonu = tk.Button(pencere, text="Tıkla!", font=("Helvetica", 18), command=butona_tikla)
oyun_butonu.pack(pady=20)

# Başlat
pencere.mainloop()
