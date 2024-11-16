import os

os.system('cls || clear')
lista = []
lista_idade = []

def cadastro_usuario(lista_cadastro):
    cadastrar = input('Digite um nome de usuario para cadastrar: ')
    lista_cadastro.append(cadastrar)

quantidade_cadastrada = int(input('Digite a quantidade de usuarios que deseja cadastra: '))
quantidade_elementos = len(lista)

while True:
    print('''\nMenu de opções
          1 - Adicionar um usuario a lista
          2 - Visualuzar lista de usuarios
          3 - Sair do programa\n''')
    x = int(input('Digite a ação tomada: \n'))
    print('\n')

    match (x):
        case 1:
        
            if quantidade_cadastrada > quantidade_elementos :
                cadastro_usuario(lista)
                print(f'Usuario cadastrado com sucesso! \n')
            else:
                print('Limete de Usuario atingido\n')
        case 2:
            if lista == []:
                print('A lista está vazia!\n')
            for i, j in enumerate(lista):
                print(f'{i+1} - {j}')
        case 3:
            print('Fim do programa!!!')
            break
