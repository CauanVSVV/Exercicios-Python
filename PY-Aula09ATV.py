"""
[PY-A09]Desenvolva uma calculadora simples utilizando a biblioteca Tkinter em Python.

A calculadora deve permitir a realização das operações básicas (adição, 
subtração, multiplicação e divisão) e ser capaz de lidar com entradas de números inteiros e decimais.

Além disso, a interface da calculadora deve ser intuitiva e fácil de usar para o usuário.
"""

from tkinter import *

cor1 = "#000000" #preto
cor2 = "#ffffff" #branco
cor3 = "#f77a05" #laranja

window = Tk()
window.title("Calculadora")
window.geometry("235x309")
window.config(bg=cor1)

frame_tela = Frame(window, width=235, height=50, bg=cor1)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(window, width=235, height=268, bg=cor1)
frame_corpo.grid(row=1, column=0)

todos_valores = ''

def entrada_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)

def calcular():
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))

def limpar_tela():

    global todos_valores

    todos_valores = ""
    valor_texto.set("")

valor_texto = StringVar()

app_label =Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18 '), bg=cor1, fg=cor2)
app_label.place(x=0, y=0)

botao_1 =Button(frame_corpo, command=lambda:limpar_tela() , text="C", width=17, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_1.place(x=0, y=0)
botao_2 =Button(frame_corpo, command=lambda: entrada_valores('/'), text="/", width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_2.place(x=177, y=0)

botao_3 =Button(frame_corpo, command=lambda: entrada_valores('7'), text="7", width=5, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_3.place(x=0, y=52)
botao_4 =Button(frame_corpo, command=lambda: entrada_valores('8'), text="8", width=5, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_4.place(x=59, y=52)
botao_5 =Button(frame_corpo, command=lambda: entrada_valores('9'), text="9", width=5, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_5.place(x=118, y=52)
botao_6 =Button(frame_corpo, command=lambda: entrada_valores('*'), text="*", width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_6.place(x=177, y=52)

botao_7 =Button(frame_corpo, command=lambda: entrada_valores('4'), text="4", width=5, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_7.place(x=0, y=104)
botao_8 =Button(frame_corpo, command=lambda: entrada_valores('5'), text="5", width=5, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_8.place(x=59, y=104)
botao_9 =Button(frame_corpo, command=lambda: entrada_valores('6'), text="6", width=5, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_9.place(x=118, y=104)
botao_10 =Button(frame_corpo, command=lambda: entrada_valores('-'), text="-", width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_10.place(x=177, y=104)

botao_11 =Button(frame_corpo, command=lambda: entrada_valores('1'), text="1", width=5, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_11.place(x=0, y=156)
botao_12 =Button(frame_corpo, command=lambda: entrada_valores('2'), text="2", width=5, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_12.place(x=59, y=156)
botao_13 =Button(frame_corpo, command=lambda: entrada_valores('3'), text="3", width=5, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_13.place(x=118, y=156)
botao_14 =Button(frame_corpo, command=lambda: entrada_valores('+'), text="+", width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_14.place(x=177, y=156)

botao_15 =Button(frame_corpo, command=lambda: entrada_valores('0'), text="0", width=11, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_15.place(x=0, y=208)
botao_16 =Button(frame_corpo, command=lambda: entrada_valores('.'), text=".", width=5, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_16.place(x=118, y=208)
botao_17 =Button(frame_corpo, command=lambda: calcular(), text="=", width=5, height=2, bg=cor3, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_17.place(x=177, y=208)

window.mainloop()