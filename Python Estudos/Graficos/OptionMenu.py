import os
from tkinter import *

def imprimirEsporte():
    ve=vesportes.get()
    if(ve=="Futebol"):
        print("Esporte Futebol")
    elif(ve=="Volei"):
        print("Esporte Volei")
    else:
        print("Esporte Basquete")

app = Tk()
app.title("Curso Python")
app.geometry("500x400")

listaEsportes=["Futebol","Volei","Basquete"]

vesportes=StringVar()
vesportes.set(listaEsportes[0]) # Valor padrão

bl_esportes = Label(app,text="Esportes")
bl_esportes.pack()

op_esportes=OptionMenu(app,vesportes,*listaEsportes)
op_esportes.pack()

btn_esporte=Button(app,text="Esporte Selecionado",command=imprimirEsporte)
btn_esporte.pack()

app.mainloop()