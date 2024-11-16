import os

os.system('cls || clear')
fila = []

for i in range(3):
    num = int(input('Digite um numero: '))
    fila.append(num)
print(fila)

primeiro_elemento = fila.pop(0)
print(primeiro_elemento)
print(fila)