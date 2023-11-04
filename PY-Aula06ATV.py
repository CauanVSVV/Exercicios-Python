#a) Explique o que o código faz. 

import random

lista = [1, 2, 3, 4, 5]

x = random.choice(lista)

# No código acima, é importado o módulo random e logo depois é criado uma lista com os valores [1, 2, 3, 4, 5]. 
# Em seguida a função choice() do módulo random é usada para pegar um valor aleatório contido na lista, depois de selecionar o elemento ele é atribuido a variável x.


# b) Escreva um trecho de código que use a função random 
# para gerar um número inteiro aleatório entre 10 e 20 (inclusive).

import random

numero_inteiro = random.randint(10, 20)

print(f"Número inteiro aleatório entre 10 e 20: {numero_inteiro}")


# c) Escreva um trecho de código que use a função random 
# para gerar uma lista com 5 elementos inteiros aleatórios entre 1 e 100 (inclusive). 


import random

lista_numeros_inteiros = []

for i in range(5):

    numero_inteiro = random.randint(1, 100)

    lista_numeros_inteiros.append(numero_inteiro)

print(f"Lista com 5 números inteiros gerados aleatoriamente: {lista_numeros_inteiros}")