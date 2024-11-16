import os

os.system('cls || clear')

quantidade_de_numeros = int(input("Digite a quantidade de numeros: "))

numeros = []
n_negativo = []
n_positivo = []

for i in range(quantidade_de_numeros):
    inserir_vetor = int(input('Digite um numero: '))
    numeros.append(inserir_vetor)

print(numeros)

for j in numeros:
    if j < 0:
        n_negativo.append(j)
        quantidade_negativo = len(n_negativo)

    else:
        n_positivo.append(j)
        soma = sum(n_positivo)

print(f'A quantidade de numeros negativos são {quantidade_negativo}.')
print(f'A soma de {n_positivo} é {soma}')

