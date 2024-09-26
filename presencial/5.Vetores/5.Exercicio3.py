import os

os.system('cls || clear')

def soma(a, b):
    somatoria = a + b
    return somatoria

def subtracao(a, b):
    subtraia = a - b
    return subtraia

def produto(a, b):
    multiplique = a * b
    return multiplique

def divisao(a, b):
    divida = a / b
    return divida

n1 = int(input(f'Digite 1º numero: '))
n2 = int(input(f'Digite 2º numero: ')) 

somatoria = soma(n1, n2)
print(f'soma é {somatoria}')

subtraia = subtracao(n1, n2)
print(f'subtração é {subtraia}')

divida = divisao(n1, n2)
print(f'divisão é {divida}')

multiplicacao = produto(n1, n2)
print(f'divisão é {multiplicacao}')

