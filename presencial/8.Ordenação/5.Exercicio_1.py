import os
import random
os.system('cls || clear')


lista = []
vazia = 0
while True:
    print('''\n Menu
          1 - Adicione um elemento na Lista
          2 - Buscar
          3 - Buscar em ordem crescente
          4 - Buscar em ordem decrescente
          5 - Randomizar
          6 - Sortear
          7 - Encerar''')
    x = int(input('Digite a decisão tomada: '))

    match (x):
        case 1:
            adicionar = int(input('Digite um numero: '))
            lista.append(adicionar)
            print(f'O numero {adicionar} foi adicionado a lista! ')
        
        case 2:
            print(f'A lista oiginal: {lista}')

        case 3:
            lista1 = sorted(lista)
            print(f'Lista em ordem crescente: {lista1}')
        case 4:
            lista2 = sorted(lista, reverse = True)
            print(f'Lista em ordem decrescente: {lista2}')
        case 5:
            lista3 = lista.copy()
            random.shuffle(lista3)
            print(f'A lista randomizada: {lista3}')
        case 6:
            sorteio = random.choice(lista)
            print(f'O numero sortiado foi: {sorteio}')
        case 7:
            print('Fim...')
            break