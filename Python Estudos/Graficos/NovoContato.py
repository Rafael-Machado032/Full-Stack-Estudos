import sqlite3
from sqlite3 import Error
import os
from tkinter import *


limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do terminal
#Cria a conexão com o banco de dados

def ConexaoBancoDados():
    """Estabelece uma conexão com o banco de dados SQLite especificado pelo caminho."""
    conexao = None
    caminho_banco = os.path.join(os.path.dirname(__file__),'graficos.db')
    #os.path.dirname(__file__) pega o diretório do arquivo atual
    #os.path.join combina o diretório com o nome do banco de dados
    try:
        conexao = sqlite3.connect(caminho_banco) # Conecta ao banco de dados SQLite
        print("Conexão bem-sucedida ao banco de dados SQLite")
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    return conexao

#Cria uma tabela no banco de dados

def CriarTabela(conexao):
    """Cria uma tabela chamada 'contatos' no banco de dados."""
    try:
        cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contatos (
                i_contato_contatos INTEGER PRIMARY KEY AUTOINCREMENT,
                s_nome_contatos TEXT NOT NULL,
                n_telefone_contatos INTEGER,
                s_email_contatos TEXT UNIQUE NOT NULL,
                s_observacao_contatos TEXT
            );
        """)
        # CREATE TABLE IF NOT EXISTS cria a tabela apenas se ela não existir
        conexao.commit() # Salva as alterações no banco de dados
        print("Tabela 'contatos' criada com sucesso.")
    except Error as e:
        print(f"Erro ao criar a tabela: {e}")

#Insere dados na tabela
def InserirDados(conexao, nome, telefone, email, observacao=None):
    """Insere um novo contato na tabela 'contatos'."""
    try:
        cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
        cursor.execute("""
            INSERT INTO contatos (s_nome_contatos, n_telefone_contatos, s_email_contatos, s_observacao_contatos)
            VALUES (?, ?, ?, ?);
        """, (nome, telefone, email, observacao))
        conexao.commit() # Salva as alterações no banco de dados
        nome_entry.delete(0,END)
        telefone_entry.delete(0,END)
        email_entry.delete(0,END)
        observacao_text.delete("1.0",END)
        print("Dados inseridos com sucesso na tabela 'contatos'.")
    except Error as e:
        print(f"Erro ao inserir dados: {e}")

#Editar dados na tabela
def EditarDados(conexao, id_contato, nome, telefone, email, observacao):
    """Edita um contato existente na tabela 'contatos' com base no ID fornecido."""
    try:
        cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
        cursor.execute("""
            UPDATE contatos
            SET s_nome_contatos = ?, n_telefone_contatos = ?, s_email_contatos = ?, s_observacao_contatos = ?
            WHERE i_contato_contatos = ?;
        """, (nome, telefone, email, observacao, id_contato))
        conexao.commit() # Salva as alterações no banco de dados
        print("Dados atualizados com sucesso na tabela 'contatos'.")
    except Error as e:
        print(f"Erro ao editar dados: {e}")

#Delete de dados na tabela
def DeletarDados(conexao, id_contato):
    """Deleta um contato da tabela 'contatos' com base no ID fornecido."""
    try:
        cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
        cursor.execute("""
            DELETE FROM contatos WHERE i_contato_contatos = ?;
        """, (id_contato,))
        conexao.commit() # Salva as alterações no banco de dados
        print("Dados deletados com sucesso da tabela 'contatos'.")
    except Error as e:
        print(f"Erro ao deletar dados: {e}")

#Consutar dados na tabela
def ConsultarDados(conexao):
    """Consulta e retorna todos os contatos da tabela 'contatos'."""
    try:
        cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
        cursor.execute("SELECT * FROM contatos;")
        resultados = cursor.fetchall() # Obtém todos os resultados da consulta
        return resultados
    except Error as e:
        print(f"Erro ao consultar dados: {e}")
        return []
    
#Pesquisar contato na tabela
def PesquisarContato(conexao, id):
    """Pesquisa um contato na tabela 'contatos' com base no ID fornecido."""
    try:
        cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
        cursor.execute("SELECT * FROM contatos WHERE i_contato_contatos = ?;", (id,))
        resultado = cursor.fetchone() # Obtém o primeiro resultado da consulta
        return resultado
    except Error as e:
        print(f"Erro ao pesquisar contato: {e}")
        return None
    
app = Toplevel() # Cria a janela principal da aplicação

#        "PACK" um widget no widget pai. Use as opções:

# after=widget                          -> inclua-o depois de incluir o widget pai
# anchor=NSEW (ou subset)               -> posicione o widget de acordo com a direção especificada
# before=widget                         -> inclua-o antes de incluir o widget pai
# expand=bool                           -> expanda o widget se o tamanho do pai aumentar
# fill=NONE ou X ou Y ou BOTH           -> preencha o widget se ele aumentar de tamanho
# in=master                             -> use o widget mestre para conter este widget
# in_=master                            -> veja a descrição da opção 'in'
# ipadx=valor                           -> adicione espaço interno na direção x
# ipady=valor                           -> adicione espaço interno na direção y
# padx=valor                            -> adicione espaço na direção x
# pady=valor                            -> adicione espaço na direção y
# side=TOP ou BOTTOM ou LEFT ou RIGHT   -> onde adicionar este widget.

#       "PLACE" um widget dentro do widget pai. Use as seguintes opções:

# in=master                             -> mestre em relação ao qual o widget está posicionado
# in_=master                            -> veja a descrição da opção 'in'
# x=valor                               -> posiciona a âncora deste widget na posição x do mestre
# y=valor                               -> posiciona a âncora deste widget na posição y do mestre
# relx=valor                            -> posiciona a âncora deste widget entre 0,0 e 1,0

#       Em relação à largura do mestre (1,0 é a borda direita)
# rely=valor                            -> posiciona a âncora deste widget entre 0,0 e 1,0

#       Em relação à altura do mestre (1,0 é a borda inferior)
# anchor=NSEW (ou subset)               -> posiciona a âncora de acordo com a direção fornecida
# width=valor                           -> largura deste widget em pixels
# height=valor                          -> altura deste widget em pixels
# relwidth=valor                        -> largura deste widget entre 0,0 e 1,0

#       Em relação à largura do mestre (1,0 é a mesma largura que o mestre)
# relheight=valor                       -> altura deste widget entre 0,0 e 1,0

#       Em relação à altura do mestre (1.0 é a mesma altura do mestre)
# bordermode="inside" ou "outside"      -> se deve levar em consideração a largura da borda do widget mestre

app.title("Gráfico Banco de Dados") # Define o título da janela
app.geometry("500x400") # Define o tamanho da janela (largura x altura)
app.configure(bg="blue") # Define a cor de fundo da janela

titulo = Label(app, text="Novo Contato", bg="yellow", fg="black", font=("Arial", 16))
titulo.pack(pady=20)

conexao = ConexaoBancoDados()
CriarTabela(conexao)

nome_label = Label(app, text="Nome:", bg="blue", fg="white", font=("Arial", 12))
nome_label.pack(anchor=W, padx=55)
nome_entry = Entry(app, bg="white", fg="black", font=("Arial", 12))
nome_entry.pack(padx=20, ipadx=100)

telefone_label = Label(app, text="Telefone:", bg="blue", fg="white", font=("Arial", 12))
telefone_label.pack(anchor=W, padx=55)
telefone_entry = Entry(app, bg="white", fg="black", font=("Arial", 12))
telefone_entry.pack(padx=20, ipadx=100)

email_label = Label(app, text="Email:", bg="blue", fg="white", font=("Arial", 12))
email_label.pack(anchor=W, padx=55)
email_entry = Entry(app, bg="white", fg="black", font=("Arial", 12))
email_entry.pack(padx=20, ipadx=100)

observacao_label = Label(app, text="Observação:", bg="blue", fg="white", font=("Arial", 12))
observacao_label.pack(anchor=W, padx=55)
observacao_text = Text(app, bg="white", fg="black", font=("Arial", 12), height=5, width=42)
observacao_text.pack(padx=20)

gravar_btn = Button(app, text="Gravar Contato", bg="orange", fg="black", font=("Arial", 12),
                    command=lambda: InserirDados(
                        conexao,
                        nome_entry.get(),
                        telefone_entry.get(),
                        email_entry.get(),
                        observacao_text.get("1.0", END).strip()
                    ))
gravar_btn.pack(pady=10)

app.mainloop() #Mantém a janela aberta até que o usuário a feche

