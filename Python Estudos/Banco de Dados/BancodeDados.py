import sqlite3
from sqlite3 import Error
import os


limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do terminal
#Cria a conexão com o banco de dados

def ConexaoBancoDados():
    """Estabelece uma conexão com o banco de dados SQLite especificado pelo caminho."""
    conexao = None
    caminho_banco = os.path.join(os.path.dirname(__file__),'SQLPython.db')
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
                s_email_contatos TEXT UNIQUE NOT NULL
            );
        """)
        # CREATE TABLE IF NOT EXISTS cria a tabela apenas se ela não existir
        conexao.commit() # Salva as alterações no banco de dados
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

#Editar dados na tabela
def EditarDados(conexao, id_contato, nome, telefone, email):
    """Edita um contato existente na tabela 'contatos' com base no ID fornecido."""
    try:
        cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
        cursor.execute("""
            UPDATE contatos
            SET s_nome_contatos = ?, n_telefone_contatos = ?, s_email_contatos = ?
            WHERE i_contato_contatos = ?;
        """, (nome, telefone, email, id_contato))
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

while True:
    limpar()
    conexao = ConexaoBancoDados()
    CriarTabela(conexao)
    print("Escolha uma opção:")
    print("1 - Inserir novo contato")
    print("2 - Editar contato")
    print("3 - Deletar contato")
    print("4 - Consultar contato")
    print("5 - Sair")
    opcao = input("Digite o número da opção desejada: ")
    if opcao == '1':
        limpar()
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        InserirDados(conexao, nome, telefone, email)
    elif opcao == '2':
        limpar()
        id_contato = input("Digite o ID do contato a ser editado: ")
        contato = PesquisarContato(conexao, id_contato)
        nome = input("Digite o novo nome do contato: " + f" (atual: {contato[1]}) ") or contato[1]
        telefone = input("Digite o novo telefone do contato: " + f" (atual: {contato[2]}) ") or contato[2]
        email = input("Digite o novo email do contato: " + f" (atual: {contato[3]}) ") or contato[3]
        EditarDados(conexao, id_contato, nome, telefone, email)
    elif opcao == '3':
        limpar()
        id_contato = input("Digite o ID do contato a ser deletado: ")
        DeletarDados(conexao, id_contato)
        
    elif opcao == '4':
        limpar()
        contatos = ConsultarDados(conexao)
        print("Contatos cadastrados:")
        for contato in contatos:
            print(contato)
        input("Pressione Enter para continuar...")
    elif opcao == '5':
        limpar()
        break
    limpar()
conexao.close()