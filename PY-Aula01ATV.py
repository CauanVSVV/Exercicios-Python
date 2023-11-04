"""
[PY-A01]Faça um programa em Python que, utilizando estruturas de repetição, 
calcule a média de idade dos alunos de uma turma. O programa deve pedir ao usuário 
a quantidade de alunos na turma e, em seguida, solicitar a idade de cada um. O programa 
deve utilizar um laço FOR para receber as idades dos alunos e um laço WHILE para realizar 
a soma das idades. Ao final, o programa deve exibir a média de idade da turma.
"""
quantidade_alunos = int(input("Qual a quantidade de alunos na turma? =>  "))

soma_idades = 0

for i in range(quantidade_alunos):
    idade = int(input(f"Digite a idade do aluno {i + 1}: "))
    while idade <= 0:
        print("Idade inválida. Digite novamente.")
        idade = int(input(f"Digite a idade do aluno {i + 1}: "))
    soma_idades += idade

media_idade = soma_idades / quantidade_alunos

print(f"A média de idade da turma é: {media_idade:.2f}")