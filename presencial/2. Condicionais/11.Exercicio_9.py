import os

os.system('cls || clear')

valor = float(input('Digite um valor: '))

os.system('cls || clear')

x = valor * 0.1

valor_desconto = valor - x 

print(f'O valor digitado foi {valor}, o desconto é {x} e o valor com desconto é {valor_desconto:.2f}')

