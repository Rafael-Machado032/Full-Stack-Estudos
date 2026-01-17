from tkinter import *

def imprimirValor():
    ve=sc_escala.get()
    print(f"Valor da barra é {ve}")


app = Tk()
app.title("Curso Python")
app.geometry("500x400")


lb_valor=Label(app,text="Valor")
lb_valor.pack()

sc_escala=Scale(app,from_=0,to=100,orient=HORIZONTAL) # Barra deslizante  de 0 a 100
sc_escala.set(50) #comeca no 50
sc_escala.pack()

btn_valor=Button(app,text="Valor Escala", command=imprimirValor)
btn_valor.pack()

app.mainloop()