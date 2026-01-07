import re # Importa o módulo de expressões regulares
#RegEx - Regular Expression

texto = "Curso de Python 2024. Aprenda Python 3.11 e 3.12!"



pesquisa = input("Digite o termo de busca: ")
res = re.findall(pesquisa, texto)
# Encontra todas as ocorrências do termo de busca no texto
print(res)
if res:
    print(f"Encontrado {len(res)} ocorrência(s) de '{pesquisa}'")
else:
    print(f"Nenhuma ocorrência de '{pesquisa}' encontrada.")

print("------------------------------------------------")

pesquisa2 = input("Digite o termo de busca para search: ")
res2 = re.search(pesquisa2, texto)
# Procura a primeira ocorrência do termo de busca no texto

if res2 != None:
    posicaoInicio = res2.start() # Posição inicial da correspondência
    posicaoFim = res2.end() # Posição final da correspondência
    tamanho = posicaoFim - posicaoInicio # Tamanho da correspondência
    print(f"'{pesquisa2}' encontrado na posição {posicaoInicio} até {posicaoFim} com tamanho {tamanho}")

print("------------------------------------------------")

pesquisa3 = input("Digite o termo de busca para split: ")

res3 = re.split(pesquisa3, texto)
# Divide o texto em uma lista usando o termo de busca como delimitador
# Exemplo se uso a letra "a" como delimitador fica
# ['Curso de Python 2024. ', 'prend', ' Python 3.11 e 3.12!']
print(res3)

res3 = re.split(r"\s+", texto)
# pesquisa3 = r"\s+"  # Expressão regular para espaços em branco
print(res3)

print("------------------------------------------------")

pesquisa4 = input("Digite o termo de busca para sub: ")
substituto = input("Digite o termo substituto: ")
res4 = re.sub(pesquisa4, substituto, texto)
# Substitui todas as ocorrências do termo de busca pelo termo substituto no texto
print(res4)
