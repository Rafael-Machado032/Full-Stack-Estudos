from tkinter import *


def imprimirValores():
    v1=int(sb_valores1.get())
    v2=int(sb_valores2.get())
    print(f"A soma dos valores e {v1 + v2}")


app = Tk()
app.title("Curso Python")
app.geometry("500x400")

listaEsportes = ["Futebol","Volei","Basquete"]

sb_valores1 = Spinbox(app,from_=0,to=10) # Caixa Numerico com seta de 0 a 10
sb_valores1.pack()

sb_valores2 = Spinbox(app,values=(1,2,3,4,5)) # Caixa Numerico com seta
sb_valores2.pack()


btn_valores=Button(app,text="Somar valores", command=imprimirValores)
btn_valores.pack()



app.mainloop()