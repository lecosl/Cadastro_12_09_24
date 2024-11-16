import os

os.system("cls || clear")


def adicionar(nota):
    for i in range(1, 5):
        add = float(input(f'Digite {i}º Nota: '))
        nota.append(add)

def organizar(nota):
    for j, k in enumerate(nota, start=1): 
        print(f'{j}ª nota é {k}')

def media(nota):
    media = sum(nota) / len(nota)
    return media

def aprovacao(nota):
    x = media(nota)
    if x >= 7:
        print("Aluno esta aprovado! ")
    else:
        print('Aluno esta reprovado! ')

notas = []

adicionar(notas)

os.system("cls || clear")

organizar(notas)

media(notas)

print(f"A media é: {media(notas)}")

aprovacao(notas)