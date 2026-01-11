from tkinter import *
import os

# tkinter é uma biblioteca padrão do Python para criar interfaces gráficas
app = Tk() # Cria a janela principal da aplicação

app.title("Gráfico Simples") # Define o título da janela
app.geometry("700x600") # Define o tamanho da janela (largura x altura)
app.configure(bg="blue") # Define a cor de fundo da janela

txt1 = Label(app, text="Gráfico Simples", bg="yellow", fg="black", font=("Arial", 16))
txt1.place(x=120, y=20, width=200, height=50)
# place é um método que posiciona o widget em coordenadas específicas dentro da janela
# ex: x=120, y=20 define a posição do widget na janela x=120 pixels da esquerda e y=20 pixels do topo
# width e height definem a largura e altura do widget
# ex: width=200, height=50 define a largura de 200 pixels e altura de 50 pixels
txt2 = Label(app, text="Exemplo de gráfico usando Tkinter", bg="blue", fg="white", font=("Arial", 12))
txt2.pack( side=TOP, fill=X, expand=True)
# pack é um método que organiza os widgets em blocos antes de colocá-los na janela
# padx e pedy adicionam espaço fora do widget padx = horizontal pady = vertical
# ipadx e ipady adicionam espaço interno do conteúdo do widget ipadx = horizontal ipady = vrtical
# side define em qual lado da janela o widget será colocado "top,left,rigth,bottom"
# fill define como o widget deve preencher o espaço disponível x = horizontal, y = vertical, both = ambos
# expand define se o widget deve expandir para preencher o espaço extra disponível na janela "True" ou "False"
# anchor define a âncora do widget dentro do espaço disponível
# exite N (norte), S (sul), E (leste), W (oeste) e combinações como NE (nordeste), SW (sudoeste)
# A diferenca de usar place e pack é que place permite um controle mais preciso da posiçao dos widgets, enquanto pack organiza os widgets de forma mais automática e simples
txt3 = Label(app, text="Tkinter é fácil de usar!", bg="green", fg="white", font=("Arial", 12))
txt3.pack(pady=10, anchor=CENTER)

vnome = Entry(app, bg="white", fg="black", font=("Arial", 12))
# Entry é um widget que permite a entrada de texto pelo usuário
vnome.pack(side=TOP, pady=10, padx=20)

vmsg = Text(app, bg="white", fg="black", font=("Arial", 12))
# Text é um widget que permite a entrada de texto multilinha pelo usuário
vmsg.place(x=150, y=300, width=400, height=200)

def impDados():
    nome = vnome.get() # Obtém o texto inserido no widget Entry
    mensagem = vmsg.get("1.0", END) # Obtém o texto inserido no widget Text, do início (1.0) até o fim (END)
    print("Nome:", nome)
    print("Mensagem:", mensagem)
    caminho_gravar = os.path.join(os.path.dirname(__file__),'salvar_msg.txt')
    #os.path.dirname(__file__) pega o diretório do arquivo atual
    #os.path.join combina o diretório com o nome do arquivo de texto
    with open(caminho_gravar, 'a') as arquivo:
        # Abre o arquivo em modo de anexação ('a'), criando-o se não existir
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"Mensagem: {mensagem}\n")
        arquivo.write("-" * 40 + "\n") # Adiciona uma linha separadora
    print(f"Dados salvos em {caminho_gravar}")

botao = Button(app, text="Enviar", bg="orange", fg="black", font=("Arial", 12), command=impDados)
# Button é um widget que cria um botão clicável
# A fução so pode ser chamado antes do botão ser criado
botao.pack(pady=10, padx=100)
# Configura o botão para chamar a função impDados quando clicado

app.mainloop() #Mantém a janela aberta até que o usuário a feche

