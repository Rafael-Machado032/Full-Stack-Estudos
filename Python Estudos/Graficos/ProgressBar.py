from tkinter import *
from tkinter import ttk

def valBarra(m):
    cont=0
    etapas=m/100
    while cont<etapas:
        cont+=1
        i=0
        while i<1000000: # Ele conta ate 10000000 e passa para a proxima
            i+=1 # isso foi feito para ver a progresão da barra
        varBarra.set(cont)
        app.update() # Redezenha a tela


app = Tk()
app.title("Curso Python")
app.geometry("500x400")

varBarra=DoubleVar()
varBarra.set(0)

pb = ttk.Progressbar(app,variable=varBarra,maximum=100) # Cria uma Barra de progresso
pb.place(x=0,y=0,width=500 ,height=30)

btn=Button(app,text="Definir Barra",command=lambda:valBarra(1000000))
btn.pack(pady=35)



app.mainloop()