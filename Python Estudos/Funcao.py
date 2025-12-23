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

# Função lambda
soma_lambda = lambda x, y: x + y # Função anônima para soma
# A função lambda é usada para criar funções pequenas e simples em uma única linha.
print("A soma usando funcao lambda de 15 e 30 eh:", soma_lambda(15, 30))
soma_lambda2 = lambda x, y, z: x + y + z
print("A soma usando funcao lambda de 5, 10 e 15 eh:", soma_lambda2(5, 10, 15))
print("A soma usando funcao lambda de 1, 2, 3, 4 e 5 eh:", (lambda a, b, c, d, e: a + b + c + d + e)(1, 2, 3, 4, 5))

lambda_funcao = lambda x,func: x + func(x)# o "x" do func recebe o valor 10 tambem
print("O resultado da funcao lambda com funcao passada como parametro eh:", lambda_funcao(10, lambda y: y * 2))
# "x" recebe o valor 10 e "func" recebe a função lambda que multiplica "y" por 2.
# o "y" dentro da função lambda é substituído por "x" (que é 10), resultando em 10 * 2 = 20.
# Então, a expressão completa se torna 10 + 20, resultando em 30.