# Instalar "pip install reportlab"
# Esse é uma biblioteca para criação de PDFs em Python

from tkinter import *
from reportlab.pdfgen import canvas # Ferramentas para gerar PDFs
from reportlab.lib.pagesizes import A4 # Tamanhos de página (A4, A3, LETTER, etc.)
from reportlab.lib.units import cm, mm # Unidades de medida (centímetros, milímetros)
import os

caminho_pdf = os.path.join(os.path.dirname(__file__), "exemplo.pdf")
caminho_imgem = os.path.join(os.path.dirname(__file__), "..", "Graficos", "img", "python.png")

def criar_pdf():
    c = canvas.Canvas(caminho_pdf, pagesize=A4)
    # O canvas.Canvas cria um novo PDF obs: canvas somente cria pdf e não outros tipos de arquivos
    # Definindo o tamanho da página como A4
    largura, altura = A4
    # largura, altura pega as dimensões da página A4
    # largura = 595.27, altura = 841.89 (em pontos)
    # Centímetros: largura = 21 cm, altura = 29.7 cm
    # Milímetros: largura = 210 mm, altura = 297 mm
    c.setFont("Helvetica", 12)
    # Definindo a fonte e o tamanho do texto
    
    c.drawString(100, altura - 1*cm, "O texto fica em cima da página.")
    c.drawImage(caminho_imgem, 100, altura - 10*cm, width=50*mm, height=50*mm)
    c.circle(300, altura - 150*mm, 50)  # Desenha um círculo
    # Em geral usa os recursos do canvas para desenhar formas, imagens e textos no PDF
    c.drawString(100, altura - 148*mm, "O texto fica no meio da página.")
    c.drawString(100, altura - 290*mm, "O texto fica em baixo da página.")
    # Adicionando texto ao PDF na posição (100, altura - 100)
    c.save()
    # Salvando o PDF
    os.startfile(caminho_pdf)  # Abre o PDF após a criação (Windows)

app = Tk()
app.title("PDF Viewer")
app.geometry("800x600")

btn_criar_pdf = Button(app, text="Criar PDF", command=criar_pdf)
btn_criar_pdf.pack(pady=20)


app.mainloop()