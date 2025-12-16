texto=" Curso de Python "

def limpa_espaco(texto): # Remove espaços em branco no início e no fim
    return texto.strip()
print(limpa_espaco(texto))

def maiusculo(texto): # Converte o texto para maiúsculas
    return texto.upper()
print(maiusculo(texto))

def minusculo(texto): # Converte o texto para minúsculas
    return texto.lower()
print(minusculo(texto))

def contar_caracteres(texto): # Conta o número de caracteres no texto
    return len(texto)
print(contar_caracteres(texto))

def substituir(texto): # Substitui "Python" por "PHP"
    return texto.replace("Python", "PHP")
print(substituir(texto))

def dividir_palavras(texto): # Divide o texto em array de palavras
    return texto.split()
print(dividir_palavras(texto))