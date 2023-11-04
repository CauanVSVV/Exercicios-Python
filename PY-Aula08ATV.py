"""
[PY-A08]Crie uma janela usando a biblioteca TKINTER em 
Python que tenha um título "Sistema de Cadastro". Nesta janela, 
crie um campo de entrada de texto para o usuário digitar seu nome e um 
botão "Enviar" que, ao ser clicado, exiba uma mensagem de boas-vindas 
com o nome do usuário em uma nova janela.
"""

from tkinter import *
from tkinter import messagebox

def exibir_mensagem_nome():
    messagebox.showinfo("Bem-vindo!", "Olá, " + nome_usuario.get() + "! Bem-vindo ao sistema de cadastro!")

window = Tk()

window.geometry("400x150")

txt_x = 130
txt_y = 10
nome_x = 110
nome_y = 50
botao_x = 165
botao_y = 100

window.title('Sistema de Cadastro')

Label(window,text="Preencha o campo abaixo").place(x=txt_x, y=txt_y)

Label(window, text="Nome:").place(x=nome_x, y=nome_y)
nome_usuario = Entry(window)
nome_usuario.place(x=nome_x+50, y=nome_y)

enviar_nome = Button(window, text="Enviar",bg="#3492eb",fg="#FFFFFF",width=10, command=exibir_mensagem_nome)
enviar_nome.place(x=botao_x, y=botao_y)

window.mainloop()