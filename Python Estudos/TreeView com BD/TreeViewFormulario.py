from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import BancodeDados

def popular():
    tv.delete(*tv.get_children())
    # Deleta todos os itens do treeview antes de popular novamente
    conexao = BancodeDados.ConexaoBancoDados()
    resultados = BancodeDados.ConsultarDados(conexao)
    for row in resultados:
        tv.insert("","end",values=row)


def inserir():
    if vnome.get().strip() == "" or vtelefone.get().strip() == "":
        messagebox.showerror(title="ERRO", message="Digite todos os dados")
        return
    try:
        conexao = BancodeDados.ConexaoBancoDados()
        BancodeDados.InserirDados(conexao, vnome.get(), vtelefone.get())
        conexao.close()
        messagebox.showinfo(title="SUCESSO", message="Contato inserido com sucesso!")
        vnome.delete(0,END)
        vtelefone.delete(0,END)
        popular()
    except Exception as e:
        print(f"Erro ao inserir: {e}")
        messagebox.showerror(title="ERRO", message=f"Erro ao inserir contato!\n{str(e)}")


def deletar():
    try:
        conexao = BancodeDados.ConexaoBancoDados()
        itemSelecionado = tv.selection()[0]
        valores = tv.item(itemSelecionado,"values")
        BancodeDados.DeletarDados(conexao, valores[0])
        messagebox.showinfo(title="SUCESSO",message="Contato deletado com sucesso!")
    except:
        messagebox.showerror(title="ERRO",message="Selecione o item a ser deletado!")

def pesquisar():
    try:
        conexao = BancodeDados.ConexaoBancoDados()
        resultado = BancodeDados.PesquisarContato(conexao, vnomePesquisar.get())
        tv.delete(*tv.get_children())
        if resultado:
            tv.insert("","end",values=resultado)
        else:
            messagebox.showinfo(title="NÃO ENCONTRADO",message="Contato não encontrado!")
    except:
        messagebox.showerror(title="ERRO",message="Erro ao pesquisar contato!")

app=Tk()
app.title("Curso de Python")
app.geometry("500x450")

quadroGrid = LabelFrame(app,text="Contatos")
quadroGrid.pack(fill="both",expand="yes",padx=10,pady=10)

tv=ttk.Treeview(quadroGrid,columns=("id","nome","telefone"),show="headings")
tv.pack()
tv.column("id",minwidth=0,width=50)
tv.column("nome",minwidth=0,width=250)
tv.column("telefone",minwidth=0,width=100)
tv.heading("id",text="ID")
tv.heading("nome",text="NOME")
tv.heading("telefone",text="TELEFONE")
popular()

quadroInserir = LabelFrame(app,text="Inserir novos contatos")
quadroInserir.pack(fill="both",expand="yes",padx=10,pady=10)

lb_nome=Label(quadroInserir,text="NOME:")
lb_nome.pack(side=LEFT)
vnome=Entry(quadroInserir)
vnome.pack(side=LEFT,padx=10)
lb_telefone=Label(quadroInserir,text="TELEFONE:")
lb_telefone.pack(side=LEFT)
vtelefone=Entry(quadroInserir)
vtelefone.pack(side=LEFT,padx=10)
btn_inserir=Button(quadroInserir,text="Inserir",command=inserir)
btn_inserir.pack(side=LEFT,padx=10)

quadroPesquisar = LabelFrame(app,text="Pesquisar contatos")
quadroPesquisar.pack(fill="both",expand="yes",padx=10,pady=10)

lb_nome=Label(quadroPesquisar,text="NOME:")
lb_nome.pack(side=LEFT)
vnomePesquisar=Entry(quadroPesquisar)
vnomePesquisar.pack(side=LEFT,padx=10)

btn_pesquisar=Button(quadroPesquisar,text="Pesquisar",command=pesquisar)
btn_pesquisar.pack(side=LEFT,padx=10)
btn_mostrar=Button(quadroPesquisar,text="Mostrar Tudo",command=popular)
btn_mostrar.pack(side=LEFT,padx=10)


app.mainloop()