import os
from tkinter import *

# O tkinter padrão suporta PNG, GIF e PPM/PGM
# Para aceitar outros formatos instalar "pip install pillow"
# e usa o modulo "from PIL import Image, ImageTk"

caminho_img = os.path.join(os.path.dirname(__file__),"img","python.png")

app = Tk()
app.title("Curso Python")
app.geometry("500x400")


imgLogo=PhotoImage(file=caminho_img)
l_Logo=Label(app,image=imgLogo)
l_Logo.pack()


app.mainloop()