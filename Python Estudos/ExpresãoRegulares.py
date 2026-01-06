import re # Importa o módulo de expressões regulares

texto = "Curso de Python 2024. Aprenda Python 3.11 e 3.12!"


while True:
    pesquisa = input("Digite o termo de busca: ")
    res = re.findall(pesquisa, texto)
    # Encontra todas as ocorrências do termo de busca no texto
    print(res)
    if res:
        print(f"Encontrado {len(res)} ocorrência(s) de '{pesquisa}'")
    else:
        print(f"Nenhuma ocorrência de '{pesquisa}' encontrada.")