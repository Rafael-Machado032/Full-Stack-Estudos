import os

caminho_arquivo = os.path.join(os.path.dirname(__file__), 'Exemplo.txt')
#os.path.dirname(__file__) pega o diretório do arquivo atual
#os.path.join junta o diretório com o nome do arquivo

arquivo = open(caminho_arquivo, "a")  # Abre (ou cria) um arquivo para escrita
# r - read - Leitura
# w - write - Escrita (apaga o conteúdo anterior)
# a - append - Adiciona conteúdo ao final do arquivo
# x - create - Cria um arquivo, mas gera um erro se o arquivo já existir
# b - binary - Modo binário (para arquivos não-texto)
# t - text - Modo texto (padrão)

txt = input("Digite algo para escrever no arquivo: ")
arquivo.write(txt + "\n")  # Escreve o texto digitado no arquivo

arquivo.close()  # Fecha o arquivo

arquivo = open(caminho_arquivo, "r")  # Abre o arquivo para leitura
conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo

print("Conteúdo do arquivo:")
print(conteudo)  # Exibe o conteúdo lido
print(arquivo.readlines())  # Lê o arquivo linha por linha e retorna uma lista
arquivo.close()  # Fecha o arquivo

deletar = input("Deseja deletar o arquivo? (s/n): ")
if deletar.lower() == 's':
    os.remove(caminho_arquivo)  # Remove o arquivo criado