import os

os.system('cls || clear')

def mergesort(lista): #função para separar as listas
    tamanho_lista = len(lista) 
    if tamanho_lista <= 1: # Verifica se a lista tem mais de 1 elemento
        return lista
    
    meio = tamanho_lista // 2 # Divide a lista em 2
    esquerda = lista[:meio] # Cria uma lista do inicio da lista até o meio dela
    direita = lista[meio:] # Cria uma lista do meio dela até o fim

    esquerda = mergesort(esquerda)
    direita = mergesort(direita)

    return merge(esquerda, direita) # chama uma segunda função para a ordenação

def merge(esquerda, direita): # Função para ordenar a lista
    ordenada = [] #cria uma lista vazia para receber a lista ordenada

    x = 0 # indece inicial da esquerda
    y = 0 # incede inicial da direita

    while x < len(esquerda) and y < len(direita): # Verifica se tem elementos na lista esquerda e direita
        
        if esquerda[x] < direita[y]: # verifica se o indice da esquerda é menor que o da direita 
            ordenada.append(esquerda[x]) # Adiciona o elemento da esquerda na lista ordenada
            x += 1
        
        else: # Se o elemento da direita for menor que o da direita  
            ordenada.append(direita[y]) # Adiciona o elemento da direita na lista
            y += 1 

    ordenada += direita[y:]
    ordenada += esquerda[x:]

    return ordenada 


lista_desordenada = []

while len(lista_desordenada) < 10:
    add_lista = int(input('Digite um numero: '))
    lista_desordenada.append(add_lista)

print(lista_desordenada)

lista_ordenada = mergesort(lista_desordenada)

print(lista_ordenada)