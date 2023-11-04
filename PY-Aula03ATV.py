"""
[PY-A03]Considere o seguinte dicionário em Python:

pessoas = {

    "João": 23,

    "Maria": 28,

    "Pedro": 35,

    "Lucas": 19

}

a) Acesse a idade da pessoa "João" e armazene em uma variável chamada idade_joao.

b) Adicione uma nova pessoa ao dicionário com nome "Ana" e idade 31.

c) Crie uma função chamada maior_idade que recebe um dicionário como argumento 
e retorna o nome da pessoa com a maior idade.
"""

def maior_idade (pessoas_dicionario):
    a_maior_idade = max(pessoas_dicionario.values())
    for nome_pessoa, idade_pessoa in pessoas_dicionario.items():
        if idade_pessoa == a_maior_idade:
            return nome_pessoa

pessoas = {
    "João": 23,
    "Maria": 28,
    "Pedro": 35,
    "Lucas": 19
}

idade_joao = pessoas["João"]

print(f"\nAs pessoas que estão no dicionario: {pessoas}")

pessoas["Ana"] = 31

print(f"\nAna foi adicionada no dicionario: {pessoas}")

nome_pessoa_maior_idade = maior_idade(pessoas)

print(f"\nNome da pessoa com a maior idade do dicionario: {nome_pessoa_maior_idade}")