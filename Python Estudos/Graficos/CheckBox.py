import os
from tkinter import *

def futebolClicado():
    print("Futebol")

def voleiClicado():
    print("Volei")

def basqueteClicado():
    print("Basquete")



app = Tk()
app.title("Curso Python")
app.geometry("500x400")

vfutebol=StringVar()
vvolei=StringVar()
vbasquete=StringVar()

vfutebol.set("n")
vvolei.set("n")
vbasquete.set("n")


fr_quadro1=Frame(app,borderwidth=1,relief="solid")
fr_quadro1.place(x=10,y=10,width=200,height=100)

cb_futebol=Checkbutton(fr_quadro1,text="Futebol",variable=vfutebol,onvalue="s",offvalue="n",command=futebolClicado)
cb_futebol.pack(side=LEFT)

cb_volei=Checkbutton(fr_quadro1,text="Volei",variable=vvolei,onvalue="s",offvalue="n",command=voleiClicado)
cb_volei.pack(side=LEFT)

cb_basquete=Checkbutton(fr_quadro1,text="Basquete",variable=vbasquete,onvalue="s",offvalue="n",command=basqueteClicado)
cb_basquete.pack(side=LEFT,fill=X)
app.mainloop()