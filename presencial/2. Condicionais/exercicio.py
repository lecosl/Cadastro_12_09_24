import os

os.system('cls || clear')

def verificar(x):
    if x % 2 == 0:
        print(f'O valor {x} é par')
    else:
        print(f'O valor {x} é impar')
    
valor = int(input('Digite um valor: '))


verificar(valor)
