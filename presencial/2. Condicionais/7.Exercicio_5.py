import os

os.system('cls || clear')

login = input('Digite o Login: ')
senha = input('Digite uma senha: ')
if login == "Leo" and senha == "123":
    print('Bem-vindo!')
else:
    print('Login e senha invalida!')