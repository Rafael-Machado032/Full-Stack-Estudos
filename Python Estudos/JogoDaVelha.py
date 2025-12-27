import os # importa o módulo os para interações com o sistema operacional
import time # importa o módulo time para manipulação de tempo
import platform # importa o módulo platform para identificar o sistema operacional
import pickle # importa o módulo pickle para serialização de objetos
from datetime import datetime # importa a classe datetime do módulo datetime para manipulação de datas e horas
from collections import defaultdict # importa defaultdict do módulo collections para criar dicionários com valores padrão
from colorama import Fore, Style, init # importa colorama para colorir a saída no terminal
init(autoreset=True) # inicializa colorama com autoreset para resetar as cores após cada impressão

class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [' ' for _ in range(9)]
        self.jogador_atual = 'X'
        self.historico_jogos = defaultdict(list)
        self.carregar_historico()

    def exibir_tabuleiro(self):
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print(f"{Fore.CYAN} Jogo da Velha {Style.RESET_ALL}")
        for i in range(3):
            print(f" {self.tabuleiro[3*i]} | {self.tabuleiro[3*i+1]} | {self.tabuleiro[3*i+2]} ")
            if i < 2:
                print("---|---|---")

    def fazer_jogada(self, posicao):
        if self.tabuleiro[posicao] == ' ':
            self.tabuleiro[posicao] = self.jogador_atual
            return True
        return False

    def verificar_vencedor(self):
        combinacoes_vencedoras = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in combinacoes_vencedoras:
            if self.tabuleiro[combo[0]] == self.tabuleiro[combo[1]] == self.tabuleiro[combo[2]] != ' ':
                return self.tabuleiro[combo[0]]
        if ' ' not in self.tabuleiro:
            return 'Empate'
        return None

    def alternar_jogador(self):
        self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'

    def salvar_historico(self, vencedor):
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.historico_jogos[data_hora].append({
            'vencedor': vencedor,
            'tabuleiro': self.tabuleiro.copy()
        })
        with open('historico_jogos.pkl', 'wb') as f:
            pickle.dump(self.historico_jogos
, f)
    def carregar_historico(self):
        if os.path.exists('historico_jogos.pkl'):
            with open('historico_jogos.pkl', 'rb') as f:
                self.historico_jogos = pickle.load(f)
    def exibir_historico(self):
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print(f"{Fore.MAGENTA} Histórico de Jogos {Style.RESET_ALL}")
        for data_hora, jogos in self.historico_jogos.items():
            for jogo in jogos:
                print(f"Data/Hora: {data_hora} | Vencedor: {jogo['vencedor']}")
                tabuleiro = jogo['tabuleiro']
                for i in range(3):
                    print(f" {tabuleiro[3*i]} | {tabuleiro[3*i+1]} | {tabuleiro[3*i+2]} ")
                    if i < 2:
                        print("---|---|---")
                print("\n")
        input("Pressione Enter para voltar ao menu principal...")
    def jogar(self):
        while True:
            self.exibir_tabuleiro()
            try:
                posicao = int(input(f"Jogador {self.jogador_atual}, escolha uma posição (1-9) ou 0 para sair: ")) - 1
                if posicao == -1:
                    print("Saindo do jogo...")
                    break
                if posicao < 0 or posicao > 8:
                    raise ValueError
                if not self.fazer_jogada(posicao):
                    print("Posição já ocupada! Tente novamente.")
                    time.sleep(1)
                    continue
            except ValueError:
                print("Entrada inválida! Tente novamente.")
                time.sleep(1)
                continue
            vencedor = self.verificar_vencedor()
            if vencedor:
                self.exibir_tabuleiro()
                if vencedor == 'Empate':
                    print(f"{Fore.YELLOW}O jogo terminou em empate!{Style.RESET_ALL}")
                else:
                    print(f"{Fore.GREEN}Jogador {vencedor} venceu!{Style.RESET_ALL}")
                self.salvar_historico(vencedor)
                input("Pressione Enter para continuar...")
                self.tabuleiro = [' ' for _ in range(9)]
                self.jogador_atual = 'X'
            else:
                self.alternar_jogador()

def main():
    jogo = JogoDaVelha()
    while True:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print(f"{Fore.CYAN} Bem-vindo ao Jogo da Velha! {Style.RESET_ALL}")
        print("1. Jogar")
        print("2. Ver Histórico de Jogos")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            jogo.jogar()
        elif escolha == '2':
            jogo.exibir_historico()
        elif escolha == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")
            time.sleep(1)
if __name__ == "__main__":
    main()
