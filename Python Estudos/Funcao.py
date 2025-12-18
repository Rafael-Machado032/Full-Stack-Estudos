#Função em Python
def saudacao(nome):
    print("Olah,", nome + "! Seja bem-vindo(a)!")
saudacao("Rafael")


num1 = 5
num2 = 10

def soma(): # Função sem parâmetros (Com entrada de dados estaticos)
    resultado = num1 + num2
    print("A soma de", num1, "e", num2, "eh:", resultado)

soma()

def multiplica(a, b): # Função com parâmetros (Entrada de dados)
    return a * b

print("A multiplicacao de 10 e 25 eh:", multiplica(10, 25))

def divisao(*n): # Função com parámetros variáveis
    return n[0] / n[1]

print("A divisao de 100 por 4 eh:", divisao(100, 4))

def subtracao(a=0, b=0): # Função com parâmetros padrão
    return a - b
print("A subtracao de 20 por 5 eh:", subtracao(20, 5))
print("A subtracao com valores padroes eh:", subtracao())
