import os

os.system("cls || clear")

while True:
    nota = float(input('Digite uma nota: '))

    if nota >= 0 and nota <= 10:
        print(f'Sua nota é: {nota}')
        break
    else:
        print('Digite a nota novamente!')
    