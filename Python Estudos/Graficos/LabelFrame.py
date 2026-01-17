from tkinter import *


app = Tk()
app.title("Curso Python")
app.geometry("500x400")


lbf_esportes=LabelFrame(app,text="Esportes",borderwidth=1,relief="solid")
lbf_esportes.place(x=20,y=25,width=100,height=100)

lb_esportes1=Label(lbf_esportes,text="Futebol")
lb_esportes1.pack()

lb_esportes2=Label(lbf_esportes,text="Volei")
lb_esportes2.pack()

lb_esportes3=Label(lbf_esportes,text="Basquete")
lb_esportes3.pack()



app.mainloop()