import os

os.system("cls || clear")

notas = []

for i in range(1, 5):
    add = float(input(f'Digite {i}º Nota: '))
    notas.append(add)

os.system("cls || clear")

for j, k in enumerate(notas, start=1): 
    print(f'{j}º nota é {k}')

media = sum(notas) / len(notas)

print(f"A media é: {media}")