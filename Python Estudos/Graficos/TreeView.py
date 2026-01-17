from tkinter import *
from tkinter import ttk

app=Tk()
app.title("Curso de Python")
app.geometry("500x300")


listaNomes = [["0","Graziele","1234"],["1","Rafael","4321"],["2","Marlene","9999"]]

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

tv.pack()

for(i,n,s) in listaNomes:
    tv.insert("","end",values=(i,n,s))
    # insert()  Insere valores na grade
    # ""        Vazio é item pricipal sem subitem
    # "end"     O valor vai sempre no final
    # values    Valor a ser inseridos









app.mainloop()