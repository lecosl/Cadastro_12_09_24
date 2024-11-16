import os

os.system('cls || clear')


def media(n1, n2):

    sum = n1 + n2
    med = sum / 2
    return med

def verificar(aprova):

    if aprova >= 7:
        print('O aluno está aprovado')
    else:
        print('O aluno está reprovado')


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

aprovacao = media(n1, n2)

print(f'A media é: {aprovacao}')

verificar(aprovacao)