import os
import random
from colorama import Fore, Back, Style

jogarNovamente = "s"
jogadas = 0
quemJoga = 2
maxJogadas = 9
vit = "n"
velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def tela():
    global velha
    global jogadas
    os.system("cls" if os.name == "nt" else "clear")
    print("    0   1   2")
    print("0: " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1: " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2: " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("   -----------")
    print("Jogadas: " + Fore.GREEN + str(jogadas) + Style.RESET_ALL)

def jogadorJoga():
    global jogadas
    global quemJoga
    global vit
    global maxJogadores
    if quemJoga == 2 and jogadas < maxJogadas:
        
        
        try:
            l = int(input("Linha: "))
            c = int(input("Coluna: "))
            while velha[l][c] != " ":
                l = int(input("Linha: "))
                c = int(input("Coluna: "))

            velha[l][c] = "X"
            quemJoga = 1
            jogadas += 1

        except:
            print("Jogada inválida!")

def cpuJoga():
    global jogadas
    global quemJoga
    global vit
    global maxJogadores
    if quemJoga == 1 and jogadas < maxJogadas:
        l = random.randint(0, 2)
        c = random.randint(0, 2)

        while velha[l][c] != " ":
            l = random.randint(0, 2)
            c = random.randint(0, 2)

        velha[l][c] = "O"
        quemJoga = 2
        jogadas += 1

def verificarVitoria():
    

while True:
    tela()
    jogadorJoga()
    cpuJoga()


