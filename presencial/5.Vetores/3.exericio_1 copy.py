import os

os.system('cls || clear')

lista_nomes = []

for i in range(4):
    nome = input(f'Digite {i+1}º um nome: ')
    lista_nomes.append(nome)

for i, j in enumerate(lista_nomes, start = 1):
    print(f'{i}º nome é: {j}')