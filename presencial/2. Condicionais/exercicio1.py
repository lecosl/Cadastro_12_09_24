import os

os.system('cls || clear')

def inflacao(x):
    if x < 100:
       valor = x * 0.1
       infla =  valor + x
    
    else:
        valor = x * 0.2
        infla = valor + x

    return infla


valor_produto = int(input('Digite o valor de um produto: '))

inflacao(valor_produto)

print(f'O valor inflacionado é {inflacao(valor_produto)}')
