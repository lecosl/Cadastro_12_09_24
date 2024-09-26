import os

os.system('cls || clear')

#função
def logo_senai(): #Função sem retorno
    os.system('cls || clear')
    print('=== SENAI ===')

quantidade_notas = int(input('Digite a quantidade de notas: '))


lista_notas = []

for i in range(quantidade_notas):
    logo_senai()
    nota = float(input(f'Digite {i+1}º nota: '))
    lista_notas.append(nota)
for  j in lista_notas:
    logo_senai()
    soma = sum(lista_notas) # função com retorno
    media = soma / len(lista_notas)
print(f'Suas notas foram {lista_notas} a media delas é {media}')
