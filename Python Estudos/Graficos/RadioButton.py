import os
from tkinter import *

def imprimirEsporte():
    ve=vesportes.get()
    if(ve=="f"):
        print("Esporte Futebol")
    elif(ve=="v"):
        print("Esporte Volei")
    else:
        print("Esporte Basquete")

app = Tk()
app.title("Curso Python")
app.geometry("500x400")

vesportes=StringVar()
vcor=StringVar()

bl_esportes = Label(app,text="Esportes")
bl_esportes.pack()

rb_futebol=Radiobutton(app,text="Futebol",value="f",variable=vesportes)
rb_futebol.pack()

rb_volei=Radiobutton(app,text="Volei",value="v",variable=vesportes,tristatevalue="nu")
rb_volei.pack()

rb_basquete=Radiobutton(app,text="Basquete",value="b",variable=vcor,tristatevalue="nu")
rb_basquete.pack()

rb_verde=Radiobutton(app,text="Verde",value="#0f0",variable=vcor)
rb_verde.pack()

rb_vermelho=Radiobutton(app,text="Vermelho",value="#f00",variable=vcor,tristatevalue="nu")
rb_vermelho.pack()

btn_esporte=Button(app,text="Esporte Selecionado",command=imprimirEsporte)
btn_esporte.pack()


app.mainloop()