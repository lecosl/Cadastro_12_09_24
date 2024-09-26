import os

os.system('cls || clear')

# Soliciatar dados do usuario
lista_notas = []

# lista_notas[0] = float(input('Digite uma nota'))
# lista_notas[1] = float(input('Digite uma nota'))
# lista_notas[2] = float(input('Digite uma nota'))
# lista_notas[3] = float(input('Digite uma nota'))

# #Exibir dados
# print(lista_notas[0])
# print(lista_notas[1])
# print(lista_notas[2])
# print(lista_notas[3])

for i in range(3):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)

#Para cada
for cada_nota in lista_notas:
    print(cada_nota)