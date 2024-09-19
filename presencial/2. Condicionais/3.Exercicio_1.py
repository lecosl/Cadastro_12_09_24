import os

os.system('cls || clear')

n1 = int(input('Digite um numero: '))

if n1 > 10:
    print(f'{n1} é maior que 10!')
elif n1 == 10:
    print(f'{n1} é igual à 10!')
else:
    print(f'{n1} é menor que 10!')