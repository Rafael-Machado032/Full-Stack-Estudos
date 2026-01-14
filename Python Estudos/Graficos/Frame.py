import os
from tkinter import *
from tkinter import messagebox


app = Tk()
app.title("Curso Python")
app.geometry("500x400")

fr_quadro1=Frame(app,borderwidth=1,relief="solid")# Frame foma uma moldura quadrado
# relief =
#   flat    -> (Padrão) sem marcação
#   raised  -> 3D Elevada
#   sunken  -> 3D Funda
#   solid   -> Linha sem efeito de profundidade
#
# 
fr_quadro1.place(x=50,y=50,width=100,height=100)

Label(fr_quadro1,text="Dentro do frame").pack()
# O Frame vira pai do elemento
app.mainloop()