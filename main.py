#Mostra menu
def mostrar_menu():
    print('Menu de Opções')
    print('1 - Cadastra o Usuário:')
    print('2 - lista de todos usuários cadastrados:')
    print('3 - sair.')
#Cadastrar usuário
def cadastrar_usuario(usuarios):

    nome = input('Digite o nome do Usuário: ')
    idade = input('Digite a idade do Usuário: ')
    email = input('Digite o email do Usuário: ')

    usuario = {'nome': nome, 'idade': idade, 'email': email}
    usuarios.append(usuario)
    print('Usuário cadastrado!')
 
def litar_usuarios(usuarios):
    if len(usuarios) == 0:
        print('Nenhm usuário cadastrado!')
    else:
        print('Lista de usuário cadastrado!')

        for i, usuario in enumerate(usuarios, start=1):
            print(f'Usuário: {i} ' )
            print(f'Nome: {usuarios['nome']}')
            print(f'Idade: {usuarios['idade']}')
            print(f'Email: {usuarios['email']}')

# Mostra menu
def mostrar_menu():
    print('Menu de Opções')
    print('1 - Cadastrar Usuário')
    print('2 - Listar todos os usuários cadastrados')
    print('3 - Sair')


# Cadastrar usuário
def cadastrar_usuario(usuarios):
    nome = input('Digite o nome do Usuário: ')
    idade = input('Digite a idade do Usuário: ')
    email = input('Digite o email do Usuário: ')

    usuario = {'nome': nome, 'idade': idade, 'email': email}
    usuarios.append(usuario)
    print('Usuário cadastrado!\n')


# Listar usuários
def listar_usuarios(usuarios):
    if len(usuarios) == 0:
        print('Nenhum usuário cadastrado!')
    else:
        print('Lista de usuários cadastrados:')
        for i, usuario in enumerate(usuarios, start=1):
            print(f'Usuário {i}:')
            print(f'Nome: {usuario["nome"]}')
            print(f'Idade: {usuario["idade"]}')
            print(f'Email: {usuario["email"]}\n')


# Início do programa
usuarios = []
opcao = 0

while opcao != 3:
    mostrar_menu()
    opcao = int(input('Digite a opção desejada: '))
    match (opcao):

        case 1:
            cadastrar_usuario(usuarios)
        case 2:
            listar_usuarios(usuarios)
        case _ :
            print('Opção inválida. Tente novamente.\n')
print('Programa Finalizado!')