import os

os.system("cls || clear")

login = "abc"
senha = "123"
tentativa = 0

while True:

    if tentativa != 3:
        login1 = input('Digite o login: ')
        senha1 = input('Digite a senha: ')
        if login == login1 and senha == senha1:
            print('Login e senha estão corretos')
            break
        else:
            print('Tente novamente! ')
            tentativa +=1
    else:
        print('Limite atingido! ')
        break




