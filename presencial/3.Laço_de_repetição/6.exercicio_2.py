import os

os.system('cls || clear')

print('===============Menu===============')
print('Codigo       Prato       Valor')
print('1            Picanha     R$ 25,00')
print('2            Lasanha     R$ 20,00')
print('3            Strogonoff     R$ 18,00')
print('4            Bife Acebolado     R$ 15,00')
print('5            Pão com ovo     R$ 5,00')

opcao = int(input('Digite um Codigo: '))

match(opcao):
    case 1:
        print('Picanha no valor de R$ 25,00')
    case 2:
        print('Lasanha no valor de R$ 20,00')
    case 3:
        print('Strogonoff no valor de R$ 18,00')
    case 4:
        print('Bife acebolado no valor de R$ 15,00')
    case 5:
        print('Pão com ovo no valor de R$ 5,00')
    case _:
        print('Codigo invalido!')
    