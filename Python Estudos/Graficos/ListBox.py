from tkinter import *


def imprimirEsportes():
    ve=lib_esporte.get(ACTIVE)
    print(f"Esporte {ve}")

def inserirlista():
    lib_esporte.insert(END,vnovo.get())
    vnovo.delete(0,END) # limpa do primeiro caracter ate o fim


app = Tk()
app.title("Curso Python")
app.geometry("500x400")

listaEsportes = ["Futebol","Volei","Basquete"]

lib_esporte = Listbox(app) # Caixa de lista
for esportes in listaEsportes:
    lib_esporte.insert(END,esportes) # insere cada elemnto no final da lista
lib_esporte.pack()


btn_esporte=Button(app,text="Esporte Selecionado", command=imprimirEsportes)
btn_esporte.pack()

vnovo=Entry(app)
vnovo.pack()

btn_insere=Button(app,text="Inserir na Lista", command=inserirlista)
btn_insere.pack()

app.mainloop()