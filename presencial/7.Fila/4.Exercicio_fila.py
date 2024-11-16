import os

os.system('cls || clear')


lista = []
vazia = 0
while True:
    print('''\n Menu
          1 - Adicione um elemento na Fila
          2 - remover elemeto da Fila
          3 - limpe a Fila
          4 - busque na Fila
          5 - Verificar se a Fila está vazia
          6 - encerar o programa''')
    x = int(input('Digite a decisão tomada: '))

    match (x):

        case 1:
            for i in range(25):
                if len(lista) <= 25:
                    adicionar = input('Digite uma palavra: ')
                    lista.append(adicionar)

            print('Limite atingido!')
                
        case 2:
            if lista: 
                item_removido = lista.pop(0)
                print(f'{item_removido} foi removido') 
            else:
                print('A Fila está vazia, impossivel Remover qualquer elemento!')
        case 3:
            if lista == []:
                print('A Fila ja está vazia!')
            else:
                lista.clear()
                print('A fila foi limpa!')
        case 4:
            if lista == []:
                print('A fila está vazia!')
            for i in lista:
                print(i)
        case 5:
            if lista == []:
                print('A fila ja está vazia!')
            else:
                print('A fila contem elementos!')
        case 6:
            print('Encerar programa...')
            break
        case _:
            print('invalido!')
