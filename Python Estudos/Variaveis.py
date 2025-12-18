#Varialvel em Python
#A variaveis em Python não precisam de declaração explícita de tipo
nome = "Rafael"
idade = 21
altura = 1.75
e_maior = idade > 18
peso = 70.5
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("É maior de idade?", e_maior)
print("Peso:", peso)

#Atribuição múltipla
num1=num2=res=10 

#Variavel Global
global_var = "Eu sou uma variável global"
def minha_funcao():
    print(global_var)
    global global_var1 #Escopo global
    global_var1 = "Eu também sou uma variável global"
    
minha_funcao()
print(global_var1)

#Tipo de dados dinâmico
var = 10
print("Tipo de var:", type(var))
var = "Agora sou uma string"
print("Tipo de var:", type(var))
var = 3.14
print("Tipo de var:", type(var))
var = True
print("Tipo de var:", type(var))

x=complex(2,3)
print("Tipo de x:", type(x))
print("Valor de x:", x.imag, "+", x.real)

i=["carro","moto","aviao"] #Lista / Array
print("Valor de i pos 0:", i[0])
print("Tipo de i:", type(i))

a=("carro","moto","aviao") #Tupla
#Tupla nao pode ser alterada
print("Tipo de a:", type(a))

d={"carro":"BMW","moto":"Honda","aviao":"Embraer"} #Dicionário
#Dicionário chave:valor
print("Valor de d moto:", d["moto"])
print("Tipo de d:", type(d))

e={7,5,7,4,8,6,4} #Conjunto
#Conjunto não permite valores duplicados
print("Tipo de e:", type(e))
print("Valor de e:", e)

b=({7,5,7,4,8,6,4}) #Frozenset
#Frozenset não permite alterações
print("Tipo de b:", type(b))
print("Valor de b:", b)

#Matrizes

carro=[
    ["BMW","Audi","Mercedes"],
    ["Honda","Yamaha","Suzuki"],
    ["Embraer","Airbus","Boeing"]
]
print("Tipo de carro:", type(carro))
print("Valor de carro[0][1]:", carro[0][1])
#Primeiro colchete seleciona a linha, o segundo colchete seleciona a coluna

#Dicionário aninhado
pessoa={
    "nome":"Rafael",
    "idade":21,
    "endereco":{
        "rua":"Rua A",
        "cidade":"Sao Paulo",
        "cep":"01234-567"
    }
}
print("Tipo de pessoa:", type(pessoa))
print("Valor do endereco da pessoa:", pessoa["endereco"]["cidade"])
#Primeiro colchete seleciona a chave do dicionário, o segundo colchete seleciona a chave do dicionário aninhado


