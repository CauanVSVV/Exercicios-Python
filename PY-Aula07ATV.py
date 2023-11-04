"""
[PY-A07]Você foi contratado para desenvolver um programa que calcule a média 
de notas dos alunos de uma turma. Para isso, você deverá criar uma lista com 
as notas de cada aluno e, em seguida, implementar uma função que calcule a média 
aritmética das notas. Além disso, você deverá utilizar um loop while para pedir 
ao usuário que insira as notas dos alunos até que ele decida parar. Por fim, 
você deverá utilizar um loop for para imprimir a média de cada aluno.

a) Escreva o código para a função que calcule a média aritmética das notas.

b) Escreva o código para o loop while que pede ao usuário que insira as notas dos alunos.

c) Escreva o código para o loop for que imprime a média de cada aluno.
"""

def media_aritmetica(notas):
    return sum(notas) / len(notas)

continuar = True

notas_turma = []

numero_alunos = int(input("Digite o número de alunos na turma: "))

for i in range(numero_alunos):
    print(f"\nNotas do aluno {i+1}:")
    print("Para parar digite um número abaixo de 0")
    notas_aluno = []

    j = 1

    while (continuar):
        nota = float(input(f"Nota {j}: "))
        if nota < 0:
            break
        else:
            notas_aluno.append(nota)
        j += 1
    notas_turma.append(notas_aluno)

print("\n")

for i, notas_aluno in enumerate(notas_turma):
    media_aluno = media_aritmetica(notas_aluno)
    print(f"Média do aluno {i+1}: {media_aluno:.2f} \nNotas do aluno {i+1}: {notas_aluno}\n")