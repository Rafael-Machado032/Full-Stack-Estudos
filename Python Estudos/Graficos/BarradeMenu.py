import os
from tkinter import *


caminho = os.path.join(os.path.dirname(__file__),"NovoContato.py")

def semComando():
    print()

def novoContato():
    exec(open(caminho).read(), globals())
    




app = Tk()
app.title("Barra de Menu")
app.geometry("500x400")
app.configure(bg = "#dde")

barramenu = Menu(app)

menuContatos = Menu(barramenu, tearoff=0)
menuContatos.add_command(label = "Novo", command = novoContato)
menuContatos.add_command(label = "Pesquisar", command = semComando)
menuContatos.add_command(label = "Deletar", command = semComando)
menuContatos.add_separator()
menuContatos.add_command(label = "Fechar", command=app.quit)
barramenu.add_cascade(label="Contatos", menu=menuContatos)

menuManutencao = Menu(barramenu, tearoff=0)
menuManutencao.add_command(label = "Banco de Dados", command = semComando)
barramenu.add_cascade(label="Manutenção", menu=menuManutencao)

menuSobre = Menu(barramenu, tearoff=0)
menuSobre.add_command(label = "Curso de Python", command = semComando)
barramenu.add_cascade(label = "Sobre", menu=menuSobre)


app.config(menu=barramenu)

app.mainloop()