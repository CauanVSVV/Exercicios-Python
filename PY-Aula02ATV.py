"""
[PY-A02]Escreva um programa em Python que receba duas listas 
como entrada do usuário e retorne uma tupla contendo os elementos 
em comum entre as duas listas e a soma desses elementos.
"""

elementos_iguais = []

print("Digite os números que deseja adicionar na primeira lista.")
lista1 = input("Obs: Os números presição estar sepados por espaço (Ex: 1 2 3 4) => ").split()

print("")

print("Digite os números que deseja adicionar na segunda lista.")
lista2 = input("Obs: Os números presição estar sepados por espaço (Ex: 1 2 3 4) => ").split()

lista1 = [int(num) for num in lista1]
lista2 = [int(num) for num in lista2]

for elemento in lista1:
    if elemento in lista2:
        elementos_iguais.append(elemento)

soma_elementos_iguais = sum(elementos_iguais)

result = tuple([elementos_iguais, soma_elementos_iguais])

print("")
print(f"Os elementos em comun das duas listas e a soma entre eles = > {result}")