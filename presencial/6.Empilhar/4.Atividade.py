import os

os.system('cls || clear')


lista = []

while True:
    print('''\n Menu
          1 - Adicione um elemento na pilha
          2 - remover elemeto da pilha
          3 - limpe a pilha
          4 - busque na pilha
          5 - Verificar se a pilha está vazia
          6 - encerar o programa''')
    x = int(input('Digite a decisão tomada: '))

    match (x):

        case 1:
            for i in range(20):
                adicionar = input('Digite uma palavra: ')
                lista.append(adicionar)
        case 2:
            lista.pop() 
        case 3:
            if lista == []:
                print('A lista ja está vazia!')
            else:
                lista.clear()
                print('A pilha foi limpa!')
        case 4:
            if lista == []:
                print('A lista está vazia!')
            for i in lista:
                print(i)
        case 5:
            if lista == []:
                print('A lista ja está vazia!')
            else:
                print('A lista contem elementos!')
        case 6:
            print('Encerar programa...')
            break
        case _:
            print('invalido!')

            

