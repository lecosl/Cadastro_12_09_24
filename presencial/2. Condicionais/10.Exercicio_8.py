import os

os.system('cls || clear')

quantidade_maca = int(input('Digite a quantidade de maçã desejada: '))

os.system('cls || clear')

if quantidade_maca < 12:
    valor_maca = 1.30
    x = valor_maca * quantidade_maca
    print(f'O valor da maçã é R${valor_maca:.2f}, e você pediu {quantidade_maca} maçãs e o valor total é: R${x:.2f}')
else: 
    valor_maca = 1
    x = valor_maca * quantidade_maca
    print(f'O valor da maçã com desconto é R${valor_maca:.2f}, e você pediu {quantidade_maca} maçãs e o valor total é: R${x:.2f}')