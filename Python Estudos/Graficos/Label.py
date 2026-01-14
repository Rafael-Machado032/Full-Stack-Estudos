from tkinter import *

app = Tk()
app.title("Curso Python")
app.geometry("500x400")

lb_curso=Label(app,text="Curso de Python",bg="blue",foreground="yellow",font=("Ariel",25))
lb_curso.pack(fill=X,expand=TRUE)

app.mainloop()