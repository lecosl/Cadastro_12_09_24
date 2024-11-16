import os

os.system('cls || clear')

quantidade_de_numeros = int(input("Digite a quantidade de numeros: "))

numeros = []
pares = []
impares = []

for i in range(quantidade_de_numeros):
    inserir_vetor = int(input('Digite um numero: '))
    numeros.append(inserir_vetor)

print(numeros)

for j in numeros:
    if j % 2 == 0:
        pares.append(j)

for k in numeros:
    if k % 2 != 0:
        impares.append(k)

print(f'{pares} são pares e {impares} são impares!')
    


