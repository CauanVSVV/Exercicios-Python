#[PY-A04]Escreva uma função em Python que recebe dois números como argumentos e retorna o maior entre eles.

#a) Implemente a função com o nome "maior_numero" e utilizando condicionais.

def maior_numero (num1: float, num2: float):
    if num1 > num2:
        return num1
    return num2

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

maior_num = maior_numero(num1, num2)

print(f"O maior número é: {maior_num}")

#b) Implemente a mesma função, porém utilizando a função "max".

def maior_numero (num1: float, num2: float):
    return max(num1, num2)

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

maior_num = maior_numero(num1, num2)

print(f"O maior número é: {maior_num}")