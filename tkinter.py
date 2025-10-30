import tkinter as tk
import random

GENISLIK = 500
YUKSEKLIK = 400
HEDEF_BOYUT = 50

puan = 0

def yeni_hedef():
    canvas.delete("hedef")
    x = random.randint(0, GENISLIK - HEDEF_BOYUT)
    y = random.randint(0, YUKSEKLIK - HEDEF_BOYUT)
    canvas.create_oval(x, y, x + HEDEF_BOYUT, y + HEDEF_BOYUT, fill="red", tags="hedef")
    canvas.tag_bind("hedef", "<Button-1>", tiklandi)

def tiklandi(event):
    global puan
    puan += 1
    puan_label.config(text=f"Puan: {puan}")
    yeni_hedef()

# Ana pencere
pencere = tk.Tk()
pencere.title("🎯 Hedefe Tıklama Oyunu")

puan_label = tk.Label(pencere, text="Puan: 0", font=("Helvetica", 16))
puan_label.pack()

canvas = tk.Canvas(pencere, width=GENISLIK, height=YUKSEKLIK, bg="white")
canvas.pack()

yeni_hedef()

pencere.mainloop()
