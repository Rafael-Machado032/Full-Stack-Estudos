class Carro:
    velmax = 0  # Atributo de classe
    ligado = False  # Atributo de instância
    cor = ""  # Atributo de instância
    def __init__(self, cor, velmax):# Construtor da classe
        #__init__ é um método especial chamado automaticamente quando um objeto é criado
        self.cor = cor # self é uma referência ao objeto atual e obrigatório no método construtor
        #self é igual ao this em outras linguagens de programação
        self.velmax = velmax
    def ligar(self): # Método para ligar o carro
        self.ligado = True
    def desligar(self): # Método para desligar o carro
        self.ligado = False
    def status(self): # Método para mostrar o status do carro
        if self.ligado:
            estado = "ligado"
        else:
            estado = "desligado"
        return f"O carro esta {estado}, de cor {self.cor} e velocidade maxima de {self.velmax} km/h."
    # O "f" antes da string indica que é uma f-string, permitindo a inclusão de expressões dentro das chaves {}
# Criando instâncias da classe Carro
carro1 = Carro("vermelho", 180)
carro2 = Carro("azul", 220)
# Usando os métodos da classe
carro1.ligar()
print(carro1.status())  # Saída: O carro está ligado, de cor vermelho e velocidade máxima de 180 km/h.
carro2.desligar()
print(carro2.status())  # Saída: O carro está desligado, de cor azul e velocidade máxima de 220 km/h.

#Herança de classes
class CarroEletrico(Carro): # A classe CarroEletrico herda da classe Carro
    def __init__(self, cor, velmax, carga_bateria):
        super().__init__(cor, velmax) # Chama o construtor da classe pai
        #O Super() é usado para acessar métodos e atributos da classe pai
        self.carga_bateria = carga_bateria # Atributo específico da classe CarroEletrico
    def status(self): # Sobrescreve o método status da classe pai
        estado = "ligado" if self.ligado else "desligado"
        return f"O carro eletrico esta {estado}, de cor {self.cor}, velocidade maxima de {self.velmax} km/h e carga da bateria em {self.carga_bateria}%."
# Criando uma instância da classe CarroEletrico
carro_eletrico = CarroEletrico("verde", 150, 85)
carro_eletrico.ligar()
print(carro_eletrico.status())  # Saída: O carro elétrico está ligado, de cor verde, velocidade máxima de 150 km/h e carga da bateria em 85%.





