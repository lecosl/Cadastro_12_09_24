import os
import random
os.system('cls || clear')

atrizes = ['Adriana Prado', 'Bárbara Borges', 'Camila Queiroz', 'Daniielle Winits', 'Fernanda Paes Leme', 'Helena Ranaldi', 'Paola Oliveira', 'Raquel Nunes', 'Viola Davis']

random.shuffle(atrizes) #embaralhe a lista
print(atrizes)

atrizes.sort()#Ordena os elementos da lista em ordem crescente
print(atrizes)

atrizes.sort(reverse = True)#Ordena os elementos da lista em ordem decrescente
print(atrizes)

