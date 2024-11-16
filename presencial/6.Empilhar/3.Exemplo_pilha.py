import os

os.system('cls || clear')
lista = []
while True:
    print('''\nMenu de opções
          1 - Adicionar um livro a lista
          2 - Visualuzar lista de livros
          3 - Remover um livo da lista
          4 - Sair do programa''')
    x = int(input('Digite a ação tomada: \n'))
    print('\n')
    match (x):
        case 1:
            y = input('\n Digite o livro que deseja adicionar a lista: ')
            lista.append(y)
        case 2 :
            if lista == [] :
                print('A lista de livros está vazia: \n')
            for livros in lista:
                print(livros)
        case 3:
            count = 1
            for livros in lista:
                print(f'{count} - {livros}')
                count += 1
            y = int(input('\n Digite o número do livro acima que deseja remover: \n'))
            lista.pop((y-1))
        case 4:
            print('Programa encerrado...')
            break
        case _:
            print('comando invalido')