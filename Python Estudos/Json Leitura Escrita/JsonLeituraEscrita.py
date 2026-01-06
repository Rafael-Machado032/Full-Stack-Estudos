import json # Importando a biblioteca JSON
import os

carros_json = '{"carros1": [ {"modelo": "Gol", "marca": "Volkswagen", "ano": 2015}, {"modelo": "Civic", "marca": "Honda", "ano": 2018}, {"modelo": "Corolla", "marca": "Toyota", "ano": 2020} ] }'

carros = json.loads(carros_json) # Convertendo JSON para dicionário

for carro in carros['carros1']:
    print(f"Modelo: {carro['modelo']}, Marca: {carro['marca']}, Ano: {carro['ano']}")

print("-------------------------------------------------------------------")
carros_novos = '{"modelo":"Honda Fit","marca":"Honda","ano":2022}'

carro_novo = json.loads(carros_novos)

for x in carro_novo:
    print(f"{x}: {carro_novo[x]}")

print("-------------------------------------------------------------------")
carroDicionario = {
    "modelo": "Ford Ka",
    "marca": "Ford",
    "ano": 2019
}
#dicionário -> objeto json

carro_jsonD = json.dumps(carroDicionario) # Convertendo dicionário para JSON
print(carro_jsonD)

print("-------------------------------------------------------------------")
carro_jsonD = json.dumps(carroDicionario, indent=4,separators=(": "," = "),sort_keys=True) 
#indent -> define a identação do json (número de espaços)
#separators -> define os separadores entre chave/valor e itens
#sort_keys -> ordena as chaves em ordem alfabética
print(carro_jsonD)

print("-------------------------------------------------------------------")
carros_lista = [
    {"modelo": "Fiesta", "marca": "Ford", "ano": 2016},
    {"modelo": "Onix", "marca": "Chevrolet", "ano": 2017},
    {"modelo": "Sandero", "marca": "Renault", "ano": 2018}
]
#list -> array json

carro_jsonL = json.dumps(carros_lista) # Convertendo lista para JSON

carros_tupla = ("Palio", "Fiat", 2015)
#tupla -> array json

carro_jsonT = json.dumps(carros_tupla) # Convertendo tupla para JSON

#Ex:

#{
#   "Nome": "Lionel Messi",
#   "Clube": "Paris Saint-Germain",
#   "Posição": "Atacante",
#   "Gols": 30,
#   "Times": ["Barcelona", "Paris Saint-Germain", "Argentina"],
#   "Uniforme":[
#       {"Camisa":10,"Shorts":8,"Meias":10},
#       {"Camisa":30,"Shorts":25,"Meias":30},
#       {"Camisa":10,"Shorts":8,"Meias":10}
#   ]
#}

Jogadores_json = '{"Nome": "Lionel Messi", "Clube": "Paris Saint-Germain", "Posição": "Atacante", "Gols": 30, "Times": ["Barcelona", "Paris Saint-Germain", "Argentina"], "Uniforme":[{"Camisa":10,"Shorts":8,"Meias":10},{"Camisa":30,"Shorts":25,"Meias":30},{"Camisa":10,"Shorts":8,"Meias":10}]}'

JogadoresJ = json.loads(Jogadores_json) # Convertendo JSON para dicionário

# Imprimindo chaves

for chave in JogadoresJ:
    print(chave) # Imprime as chaves do dicionário

print("-------------------------------------------------------------------")
# Imprimindo valores
for valor in JogadoresJ.values():
    print(valor) # Imprime os valores do dicionário

print("-------------------------------------------------------------------")
# Imprimindo itens (chave e valor)
for item in JogadoresJ.items():
    print(item) # Imprime os itens do dicionário (tuplas de chave e valor)

print("-------------------------------------------------------------------")
# Valor específico
print(JogadoresJ["Clube"]) # Imprime o valor associado à chave "Clube
# Valores na lista associada à chave "Times"


for time in JogadoresJ["Times"]:
    print(time) # Imprime cada time na lista associada à chave "Times"


for uniforme in JogadoresJ["Uniforme"]:
    #print(uniforme) # Imprime cada dicionário na lista associada à chave "Uniforme"
    print(f"Camisa: {uniforme['Camisa']}, Shorts: {uniforme['Shorts']}, Meias: {uniforme['Meias']}")

print("-------------------------------------------------------------------")
# Leitura de arquivo JSON

# with open(r"c:\Users\rafin\OneDrive\Documentos\GitHub\Full Stack Estudos\Python Estudos\Json Leitura Escrita\ExemploJson.json", "r", encoding='utf-8') as aj:
#     jogadorAj = json.load(aj) # Lendo o conteúdo do arquivo JSON e convertendo para dicionário
    
#     for chave, valor in jogadorAj.items():
#         print(f"{chave}: {valor}")


caminho_arquivo = os.path.join(os.path.dirname(__file__), 'ExemploJson.json')
with open(caminho_arquivo, "r", encoding='utf-8') as aj:
    jogadorAj = json.load(aj) # Lendo o conteúdo do arquivo JSON e convertendo para dicionário
    print("\nLendo arquivo JSON: \n")
    for chave, valor in jogadorAj.items():
        print(f"{chave}: {valor}")

print("-------------------------------------------------------------------")
