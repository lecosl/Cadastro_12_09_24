import os

os.system('cls || clear') # Limpa o terminal.

resposta = ""
#Entrada
idade = int(input("Digite sua idade: "))
#Processamento
if idade < 18:
    resposta = "Menoridade"
else:
    resposta = "Maioridade"

#Saída
print(f"Resultado: {resposta}")
print("===FIM===")