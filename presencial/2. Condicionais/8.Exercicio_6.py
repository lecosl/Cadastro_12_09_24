import os

os.system('cls || clear')

login = int(input('Digite sua idade: '))
if login > 18:
    print(f'Sua idade é: {login} Anos. Voto não obrigatorio!')
elif login < 65:
    print(f'Sua idade é: {login} Anos. Voto não obrigatorio!')
else:
    print(f'Sua idade é: {login} Anos. Voto obrigatorio!')