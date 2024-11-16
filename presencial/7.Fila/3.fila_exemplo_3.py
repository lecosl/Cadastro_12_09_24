import os

os.system('cls || clear')
fila = []

for i in range(3):
    texto = input('Digite uma Palavra ')
    fila.append(texto)
print(fila)

primeiro_elemento = fila.pop(0)
print(primeiro_elemento)
print(fila)