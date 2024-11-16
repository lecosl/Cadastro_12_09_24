import os
import time as t

os.system('cls || clear')

numero = int(input('Digite um numero: ' ))


def soma(x):
    if x == 0 :
        return 0
    else:
        print(f'{x} + {x - 1}')
        t.sleep(2)
        return x + soma(x - 1)

print(f'Soma: {soma(numero)}')