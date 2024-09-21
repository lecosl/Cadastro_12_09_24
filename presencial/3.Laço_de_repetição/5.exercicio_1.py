import os

os.system('cls || clear')

n1 = int(input('Digite o primeiro numero: '))
operacao = input('Digite a operação entre ( + - * / ): ')
n2 = int(input('Digite o segundo numero: '))

match(operacao):
    case "+":
        resultado = n1 + n2
        print(f'{n1} + {n2} = {resultado}')
    case "-":
        resultado = n1 - n2 
        print(f'{n1} - {n2} = {resultado}')
    case "*":
        resultado = n1 * n2 
        print(f'{n1} * {n2} = {resultado}')
    case "/":
        resultado = n1 / n2 
        print(f'{n1} / {n2} = {resultado}')

    case _:
        print('Operação invalida!')

