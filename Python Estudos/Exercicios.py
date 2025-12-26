import os # os é uma biblioteca para interagir com o sistema operacional
carros = []

class Carro:
    nome=""
    potencia=0
    velMax=0
    ligado=False

    def __init__(self,nome, potencia):
        self.nome=nome
        self.potencia=potencia
        self.velMax=potencia*2
        self.ligado=False
    def ligar(self):
        if self.ligado:
            print(f"O carro {self.nome} já está ligado.")
        else:
            self.ligado=True
            print(f"O carro {self.nome} foi ligado com sucesso.")
    def desligar(self):
        if not self.ligado:
            print(f"O carro {self.nome} já está desligado.")
        else:
            self.ligado=False
            print(f"O carro {self.nome} foi desligado com sucesso.")
    def mostrarDados(self):
        print(f"Nome:................ {self.nome}") #"f" indica que é uma f-string
        print(f"Potência:............ {self.potencia} cv")
        print(f"Velocidade Máxima:... {self.velMax} km/h")
        print(f"Estado:.............. {'Ligado' if self.ligado else 'Desligado'}")
        print("-"*30)

def Menu():
    os.system("cls" if os.name == "nt" else "clear")
    print("===== Gerenciador de Carros =====")
    print("1. Adicionar Carro")
    print("2. Excluir Todos Carros")
    print("3. Excluir Carro")
    print("4. Listar Carros")
    print("5. Informações do Carro")
    print("6. Ligar Carro")
    print("7. Desligar Carro")
    print("8. Sair")
    print("Quantidade de carros cadastrados:", len(carros))
    print("==================================")
    opcao = input("Escolha uma opção: ") # Pausa e lê a opção escolhida pelo usuário
    return opcao
    
def adicionarCarro():
    os.system("cls" if os.name == "nt" else "clear")
    print("===== Adicionar Carro =====")
    nome = input("Nome do carro: ")
    potencia = int(input("Potência do carro (cv): "))
    novo_carro = Carro(nome, potencia)
    carros.append(novo_carro)
    print(f"Carro {nome} adicionado com sucesso!")
    input("Pressione Enter para continuar...") # Pausa para o usuário ler a mensagem

def excluirTodosCarros():
    os.system("cls" if os.name == "nt" else "clear")
    print("===== Excluir Carros =====")
    carros.clear()
    print("Todos os carros foram excluídos.")
    input("Pressione Enter para continuar...") # Pausa para o usuário ler a mensagem

def excluirCarro():
    os.system("cls" if os.name == "nt" else "clear")
    print("===== Excluir Carro =====")
    nome = input("Nome do carro: ")
    for carro in carros:
        if carro.nome == nome:
            carros.remove(carro)
            print(f"Carro {nome} excluído com sucesso.")
            break
    else:
        print(f"Carro {nome} não encontrado.")
    input("Pressione Enter para continuar...") # Pausa para o usuário ler a mensagem

def listarCarros():
    os.system("cls" if os.name == "nt" else "clear")
    print("===== Lista de Carros =====")
    if not carros:
        print("Nenhum carro cadastrado.")
    else:
        for carro in carros:
            carro.mostrarDados()
    input("Pressione Enter para continuar...") # Pausa para o usuário ler a mensagem

def informacoesCarro():
    os.system("cls" if os.name == "nt" else "clear")
    print("===== Informações do Carro =====")
    nome = input("Nome do carro: ")
    for carro in carros:
        if carro.nome == nome:
            carro.mostrarDados()
            break
    else:
        print(f"Carro {nome} não encontrado.")
    input("Pressione Enter para continuar...") # Pausa para o usuário ler a mensagem

def ligarCarro():
    os.system("cls" if os.name == "nt" else "clear")
    print("===== Ligar Carro =====")
    nome = input("Nome do carro: ")
    for carro in carros:
        if carro.nome == nome:
            carro.ligar()
            break
    else:
        print(f"Carro {nome} não encontrado.")
    input("Pressione Enter para continuar...") # Pausa para o usuário ler a mensagem

def desligarCarro():
    os.system("cls" if os.name == "nt" else "clear")
    print("===== Desligar Carro =====")
    nome = input("Nome do carro: ")
    for carro in carros:
        if carro.nome == nome:
            carro.desligar()
            break
    else:
        print(f"Carro {nome} não encontrado.")
    input("Pressione Enter para continuar...") # Pausa para o usuário ler a mensagem

while True:
    opcao = Menu() # Chama a função Menu e armazena a opção escolhida
    if opcao == "1":
        adicionarCarro()
    elif opcao == "2":
        excluirTodosCarros()
    elif opcao == "3":
        excluirCarro()
    elif opcao == "4":
        listarCarros()
    elif opcao == "5":
        informacoesCarro()
    elif opcao == "6":
        ligarCarro()
    elif opcao == "7":
        desligarCarro()
    elif opcao == "8":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
        input("Pressione Enter para continuar...")




