#Condicional IF
e_maior = True
a=10
b=5
nome = "Rafael"
nome2 = "Ana"
Curso = "Full Stack"
Pesquisa = "full"
#Para dentro do bloco if, utilizamos espaços
if e_maior:
    print(nome, "é maior de idade.")
    print("Pode acessar o conteúdo restrito.")
else:
    print(nome, "não é maior de idade.")
    print("Acesso negado ao conteúdo restrito.")

if a>b:
    print(a, "é maior que", b)
else:
    print(a, "não é maior que", b)

if a==b:
    print(a, "é igual a", b)
elif a>b:
    print(a, "é maior que", b)
else:
    print(a, "é menor que", b)

#Condicional com string
print(nome in nome2)  # Retorna False, pois "Rafael" não está em "Ana"
print(nome2 not in nome)  # Retorna True, pois "Ana" não está em "Rafael"
print(Pesquisa.lower() in Curso.lower())  # Retorna True, ignorando maiúsculas/minúsculas

#Condicional com For

carros = ["Gol", "Uno", "Palio", "Celta"]

for carro in carros: # Percorre a lista de carros e insere cada carro na variável 'carro'
    if carro == "Palio":
        print(carro, "encontrado! Parando a busca.")
        break  # Sai do loop quando encontrar "Palio"
    print("Procurando...", carro)
else:
    print("Carro não encontrado na lista.")


#Condicional com While
contador = 0
while contador < 5:
    print("Contador é:", contador)
    contador += 1  # Incrementa o contador em 1

print("Contagem finalizada. Contador é igual a", contador)




