import os

os.system("cls || clear")

def verificar():
    for j in range(1, 16):
        if j % 2 != 0:
            print(f'{j} é impar')

verificar()
