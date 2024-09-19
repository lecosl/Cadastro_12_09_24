import os

os.system('cls || clear')

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
media = (n1 + n2) / 2
soma = n1 + n2
produto = n1 * n2

print(f'Media: {media}')
print(f'Soma: {soma}')
print(f'Produto: {produto}')
if n1 > n2:
    print(f'Maior valor {n1}')
    print(f'Menor valor: {n2}')
elif n1 == n2:
    print(f'{n1} e {n2} são igauis! ')

else:
    print(f'Maior valor: {n2}')
    print(f'Menor valor: {n1}')