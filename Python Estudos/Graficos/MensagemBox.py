import os
from tkinter import *
from tkinter import messagebox

def mostrarMsg(tipomsg,msg):
    if(tipomsg=="1"):
        messagebox.showinfo(title="Curso de Python",message=msg) # Aparece "i" Informação
    elif(tipomsg=="2"):
        messagebox.showwarning(title="Curso de Python",message=msg) # Aparece "!" Atenção
    else:
        messagebox.showerror(title="Curso de Python",message=msg) # Aparece "X" Erro

def resetarTB():
    res=messagebox.askyesno("Resetar","Confirma reset do textbox?")
    # askyesno / askquestion    -> SIM e NÃO (True e False)
    # askokcancel               -> OK e CANCELAR (True e False)
    # askretrycancel            -> REPETIR E CANCELAR (True e False)
    # askyesnocancel            -> SIM, NÃO E CANCELAR (True, False e None)
    if(res==True):
        tb_num.delete(0,END)
        tb_num.insert(0,"1")


vmsg="Rafael Machado"

app = Tk()
app.title("Curso Python")
app.geometry("500x400")

vnum_cstexto=StringVar()

Label(app,text="Tipo de cx(1,2 ou 3)").pack()
tb_num=Entry(app,textvariable=vnum_cstexto)
vnum_cstexto.set("1")
tb_num.pack()

btn_msg=Button(app,text="Mostrar mensagem",command=lambda:mostrarMsg(vnum_cstexto.get(),vmsg)) # Na lambda podemos iserir parametro
btn_msg.pack()

btn_reset=Button(app,text="Resetar TextBox",command=resetarTB)
btn_reset.pack()


app.mainloop()