from tkinter import *

def impSenha():
    print(f"Senha digitada "+ p_senha.get())

app = Tk()
app.title("Curso Python")
app.geometry("500x400")

vsenha=StringVar()

p_senha=Entry(app,textvariable=vsenha,show="*") #show Insere o valor para esconder o caracter
p_senha.pack()

btn_mostrarSenha=Button(app,text="Imprime Senha",command=impSenha)
btn_mostrarSenha.pack()


app.mainloop()