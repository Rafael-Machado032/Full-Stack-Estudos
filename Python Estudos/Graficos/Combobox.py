from tkinter import *
from tkinter import ttk

def imprimirEsportes():
    ve=cb_esportes.get()
    print(f"Esporte {ve}")

app = Tk()
app.title("Curso Python")
app.geometry("500x400")

listaEsportes = ["Futebol","Volei","Basquete"]

lb_esporte = Label(app,text="Esportes")
lb_esporte.pack()

cb_esportes=ttk.Combobox(app,values=listaEsportes)
cb_esportes.set("Futebol") # set ja seleciona o futebol
cb_esportes.pack()

btn_esporte=Button(app,text="Esporte Selecionado", command=imprimirEsportes)
btn_esporte.pack()


app.mainloop()