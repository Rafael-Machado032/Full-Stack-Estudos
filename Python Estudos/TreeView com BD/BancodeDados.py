import sqlite3
from sqlite3 import Error
import os


limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do terminal
#Cria a conexão com o banco de dados

def ConexaoBancoDados():
    """Estabelece uma conexão com o banco de dados SQLite especificado pelo caminho."""
    conexao = None
    caminho_banco = os.path.join(os.path.dirname(__file__),'Cotatos.db')
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
            );
        """)
        # CREATE TABLE IF NOT EXISTS cria a tabela apenas se ela não existir
        conexao.commit() # Salva as alterações no banco de dados
        print("Tabela 'contatos' criada com sucesso.")
    except Error as e:
        print(f"Erro ao criar a tabela: {e}")

#Insere dados na tabela
def InserirDados(conexao, nome, telefone):
    """Insere um novo contato na tabela 'contatos'."""
    try:
        cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
        cursor.execute("""
            INSERT INTO contatos (s_nome_contatos, n_telefone_contatos)
            VALUES (?, ?, ?);
        """, (nome, telefone))
        conexao.commit() # Salva as alterações no banco de dados
        print("Dados inseridos com sucesso na tabela 'contatos'.")
    except Error as e:
        print(f"Erro ao inserir dados: {e}")

#Editar dados na tabela
def EditarDados(conexao, id_contato, nome, telefone):
    """Edita um contato existente na tabela 'contatos' com base no ID fornecido."""
    try:
        cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
        cursor.execute("""
            UPDATE contatos
            SET s_nome_contatos = ?, n_telefone_contatos = ?, s_email_contatos = ?
            WHERE i_contato_contatos = ?;
        """, (nome, telefone, id_contato))
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




#CriarTabela(ConexaoBancoDados())

#Exemplo de inserção de dados
#InserirDados(ConexaoBancoDados(), "João Silva", 123456789, "joao.silva@email.com")

