import random # Importa o módulo random para gerar números aleatórios
import os # Importa o módulo os para interagir com o sistema operacional

erros = 0 # Inicializa a variável de erros
sorteado = random.randint(1, 10) # Gera um número aleatório entre 1 e 10
jogador = int(input("Digite um número entre 1 e 10: ")) # Solicita ao jogador que digite um número
os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela do console

while jogador != sorteado: # Enquanto o jogador não acertar o número sorteado
    erros += 1 # Incrementa o contador de erros
    print("Número errado! Tente novamente.") # Informa que o número está errado
    jogador = int(input("Digite um número entre 1 e 10: ")) # Solicita ao jogador que digite outro número
    os.system('cls' if os.name == 'nt' else 'clear') # Verifica o sistema operacional e limpa a tela do console
print(f"Parabéns! Você acertou o número {sorteado} com {erros} tentativas erradas.") # Informa que o jogador acertou e o número de erros




