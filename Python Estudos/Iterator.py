# Iterator é um padrão de projeto que permite a iteração sobre uma coleção de objetos sem expor sua representação subjacente.

carros=['Gol', 'Uno', 'Palio', 'Celta']

iterador_carros=iter(carros)


# print(next(iterador_carros))  # Gol
# print(next(iterador_carros))  # Uno
# print(next(iterador_carros))  # Palio
# print(next(iterador_carros))  # Celta
# print(next(iterador_carros))  # StopIteration
# A última chamada a next() gera uma exceção StopIteration, indicando que não há mais elementos para iterar.

while iterador_carros: # Loop so para quando atravesar todos os elementos
    try:
        carro=next(iterador_carros)
        print(carro)
    except StopIteration:
        break
