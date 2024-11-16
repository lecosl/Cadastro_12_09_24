import os

os.system('cls || clear')

pilha = [1, 1, 2, 3, 5]
print('pilha: ', pilha)

pilha.append(8)
print('Inserindo um elemento', pilha)

pilha.append(13)
print('inserindo outro elemento', pilha)

pilha.pop()
print('removendo um elemento', pilha)

pilha.pop()
print('removendo outro elemento', pilha)