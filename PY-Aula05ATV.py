#[PY-A05]Escreva uma função em Python que recebe uma lista de números inteiros e retorna a média aritmética dos valores.

def media_aritmetrica (lista_numeros):
    soma_lista = sum(lista_numeros)
    return soma_lista / len(lista_numeros)

numeros_inteiros = [6,11,3,4,5]

resultado = media_aritmetrica(numeros_inteiros)

print(f"Média aritmédica da lista = > {resultado}")

#tipo 2:

def media_aritmetrica (lista_numeros):
    soma_lista = sum(lista_numeros)
    return soma_lista / len(lista_numeros)

numeros_inteiros = []

while (True):
    try:
        numero = int(input("\nDigite um número inteiro para ser adicionado na lista: "))
        numeros_inteiros.append(numero)
        print("\nNúmero adicionado na lista!")
    except ValueError:
        print("\nDigite apenas números inteiros!")
        continue

    print(f"\nLista => {numeros_inteiros}")
    resposta = input("\nDeseja continuar adicionando números na lista? [s/n]")
    if resposta.lower() == "n":
        break

media = media_aritmetrica(numeros_inteiros)

print(f"\nMédia aritmetica da lista de números inteiros: {media}")