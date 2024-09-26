import os

os.system('cls || clear')

#função
def logo_senai(): #Função sem retorno
    os.system('cls || clear')
    print('=== SENAI ===')
def calcular_media(listas_notas):
    soma = sum(lista_notas)
    media_calculada = soma / len(lista_notas)
    return media_calculada



quantidade_notas = int(input('Digite a quantidade de notas: '))


lista_notas = []

for i in range(quantidade_notas):
    logo_senai()
    nota = float(input(f'Digite {i+1}º nota: '))
    lista_notas.append(nota)
media = calcular_media(lista_notas)
for  j in lista_notas:
    print(f'Notas: {j}')
print(f'Suas notas foram {lista_notas} a media delas é {media}')
