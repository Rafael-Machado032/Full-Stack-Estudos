from tkinter import *
from tkinter import ttk



app = Tk()
app.title("Curso Python")
app.geometry("500x400")


nb = ttk.Notebook(app) # Cria uma janela
nb.place(x=0,y=0,width=500 ,height=300)

tb1 = Frame(nb) # Cria um container vazio
nb.add(tb1,text="Inicio") # Cria a aba do container

tb2 = Frame(nb)
nb.add(tb2,text="Serviços")

lb1=Label(tb1,text="Curso de Python")
lb1.pack()

lb2=Label(tb2,text="Container 2")
lb2.pack()


app.mainloop()