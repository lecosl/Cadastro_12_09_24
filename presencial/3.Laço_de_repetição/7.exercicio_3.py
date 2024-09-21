import os

os.system('cls || clear')

dia = int(input('Digite um dia da semana (Considere 1 para Domingo e 7 para sabado): '))

match(dia):
    case 1:
        print('Final de semana! ')
    case 2:
        print('Dia de semana! ')
    case 3:
        print('Dia de semana! ')
    case 4:
        print('Dia de semana! ')
    case 5:
        print('Dia de semana! ')
    case 6:
        print('Dia de semana! ')
    case 7:
        print('Final de semana! ')

    case _:
        print('Numero invalido! ')