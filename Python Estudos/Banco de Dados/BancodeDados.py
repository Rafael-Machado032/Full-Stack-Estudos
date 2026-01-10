import sqlite3
from sqlite3 import Error



#Cria a conexão com o banco de dados

def ConexaoBancoDados():
    """Estabelece uma conexão com o banco de dados SQLite especificado pelo caminho."""
    conexao = None
    caminho_banco = './SQLPython.db'
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
                s_email_contatos TEXT UNIQUE NOT NULL
            );
        """)
        print("Tabela 'contatos' criada com sucesso.")
    except Error as e:
        print(f"Erro ao criar a tabela: {e}")

#Insere dados na tabela
def InserirDados(conexao, nome, telefone, email):
    """Insere um novo contato na tabela 'contatos'."""
    try:
        cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
        cursor.execute("""
            INSERT INTO contatos (s_nome_contatos, n_telefone_contatos, s_email_contatos)
            VALUES (?, ?, ?);
        """, (nome, telefone, email))
        conexao.commit() # Salva as alterações no banco de dados
        print("Dados inseridos com sucesso na tabela 'contatos'.")
    except Error as e:
        print(f"Erro ao inserir dados: {e}")

CriarTabela(ConexaoBancoDados())