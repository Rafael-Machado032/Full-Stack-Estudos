#Manipulação de lista

c=["HRV","Golf","Civic"]

print("Lista c:", c)
c.append("Fusca") #append adiciona um item no final da lista
print("Lista c após adicionar Fusca:", c)

c.remove("Golf") #remove remove o item especificado da lista
print("Lista c após remover Golf:", c)

c.insert(1,"Corolla") #insert adiciona um item na posição especificada
print("Lista c após inserir Corolla na posição 1:", c)

c.pop() #pop remove o último item da lista
print("Lista c após remover o último item:", c)

c.sort() #sort ordena a lista em ordem alfabética
print("Lista c ordenada:", c)

c.reverse() #reverse inverte a ordem da lista
print("Lista c invertida:", c)

c.clear() #clear remove todos os itens da lista
print("Lista c após clear:", c)

print("Tamanho da lista c:", len(c)) #len retorna o tamanho da lista

#Input
nome = input("Digite seu nome: ") #input recebe uma entrada do usuário
print("Olá,", nome)
idade = int(input("Digite sua idade: ")) #converte a entrada para inteiro
print("Você tem", idade, "anos.")


