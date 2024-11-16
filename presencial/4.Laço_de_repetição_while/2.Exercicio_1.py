import os

os.system('cls || clear')
x = []
while True:
    n = int(input('Digite um numero: '))

    if n < 0:
        x.append(n)
        print(f'A quantidade de numeros negativos são: {len(x)}')
    else:
        break
print(f'A quantidade de numeros negativos são: {len(x)}, e eles são {x}')