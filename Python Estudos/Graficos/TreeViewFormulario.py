from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def inserir():
    if vid.get() == "" or vnome.get() == "" or vsenha.get() == "":
        messagebox.showerror(title="ERRO", message="Digite todos os dados")
        return
    tv.insert("","end",values=(vid.get(),vnome.get(),vsenha.get()))
    vid.delete(0,END)
    vnome.delete(0,END)
    vsenha.delete(0,END)


def deletar():
    print()

def mostrar():
    print()

app=Tk()
app.title("Curso de Python")
app.geometry("500x400")


lb_id=Label(app,text="ID")
vid=Entry(app)

lb_nome=Label(app,text="NOME")
vnome=Entry(app)

lb_senha=Label(app,text="SENHA")
vsenha=Entry(app)

tv=ttk.Treeview(app,columns=("id","nome","senha"),show="headings")
# show="headings" Remove a coluna vazia que por padrão vem na grade
tv.column("id",minwidth=0,width=50)
# Cria o tamanho da grade
tv.column("nome",minwidth=0,width=250)
tv.column("senha",minwidth=0,width=100)

tv.heading("id",text="ID")
# Insere texto no cabeçalho da coluna
tv.heading("nome",text="NOME")
tv.heading("senha",text="SENHA")

btn_inserir=Button(app,text="Inserir",command=inserir)
btn_deletar=Button(app,text="Deletar",command=deletar)
btn_mostrar=Button(app,text="Mostrar",command=mostrar)

lb_id.grid(column=0,row=0,sticky=W)
vid.grid(column=0,row=1,sticky=W)

lb_nome.grid(column=1,row=0,sticky=W)
vnome.grid(column=1,row=1,sticky=W)

lb_senha.grid(column=2,row=0,sticky=W)
vsenha.grid(column=2,row=1,sticky=W)

tv.grid(column=0,row=3,columnspan=3,pady=5)

btn_inserir.grid(column=0,row=4)
btn_deletar.grid(column=1,row=4)
btn_mostrar.grid(column=2,row=4)











app.mainloop()