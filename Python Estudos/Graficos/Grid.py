from tkinter import *

app=Tk()
app.title("Curso de Python")
app.geometry("500x300")


lb_curso = Label(app,text="Curso de Python ")
lb_nome = Label(app,text="Digite seu nome: ")
lb_idade = Label(app,text="Informe sua idade: ")

et_nome = Entry(app)
et_idade = Entry(app)

btn = Button(app,text="Imprimir")

lb_curso.grid(column=0,row=0,columnspan=2)
# columnspan mescla colunas
# rowspan mescla linhas
lb_nome.grid(column=0,row=1,sticky="w",padx=10)
# Norte "N" Topo
# Sul   "S" Baixo
# Leste "E" Direita
# Oeste "W" Esquerda
et_nome.grid(column=0,row=2,padx=10)

lb_idade.grid(column=1,row=1,sticky="w",padx=10)
# Stick posição da tela ponto cardial
# Norte "N" Topo
# Sul   "S" Baixo
# Leste "E" Direita
# Oeste "W" Esquerda
et_idade.grid(column=1,row=2,padx=10)




app.mainloop()