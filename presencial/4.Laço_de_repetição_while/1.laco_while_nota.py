import os
os.system('cls || clear')

while True:
    nota = float(input('Digite uma nota: '))
    if nota >= 0:
        break
    print('Digite novamente!')

print(f'Nota: {nota}')
