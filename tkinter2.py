import tkinter as tk
import random

GENISLIK = 500
YUKSEKLIK = 400
HEDEF_BASLANGIC_BOYUT = 50
SURE = 30  # saniye

puan = 0
kalan_sure = SURE
hedef_boyut = HEDEF_BASLANGIC_BOYUT

def yeni_hedef():
    global hedef_boyut
    canvas.delete("hedef")
    x = random.randint(0, GENISLIK - hedef_boyut)
    y = random.randint(0, YUKSEKLIK - hedef_boyut)
    canvas.create_oval(x, y, x + hedef_boyut, y + hedef_boyut, fill="red", tags="hedef")
    canvas.tag_bind("hedef", "<Button-1>", tiklandi)

def tiklandi(event):
    global puan, hedef_boyut
    puan += 1
    if hedef_boyut > 20:
        hedef_boyut -= 2  # her tıklamada hedef küçülür (oyunu zorlaştırır)
    puan_label.config(text=f"Puan: {puan}")
    yeni_hedef()

def zamanlayici():
    global kalan_sure
    if kalan_sure > 0:
        kalan_sure -= 1
        zaman_label.config(text=f"Kalan Süre: {kalan_sure}")
        pencere.after(1000, zamanlayici)
    else:
        canvas.delete("hedef")
        canvas.create_text(GENISLIK/2, YUKSEKLIK/2, text=f"Oyun Bitti!\nSkorun: {puan}", font=("Helvetica", 24), fill="black")

# Ana pencere
pencere = tk.Tk()
pencere.title("🎯 Geliştirilmiş Hedefe Tıklama Oyunu")

puan_label = tk.Label(pencere, text="Puan: 0", font=("Helvetica", 16))
puan_label.pack()

zaman_label = tk.Label(pencere, text=f"Kalan Süre: {SURE}", font=("Helvetica", 14))
zaman_label.pack()

canvas = tk.Canvas(pencere, width=GENISLIK, height=YUKSEKLIK, bg="white")
canvas.pack()

yeni_hedef()
zamanlayici()

pencere.mainloop()
