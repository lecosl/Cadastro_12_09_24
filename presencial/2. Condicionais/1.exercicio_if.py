import os

os.system('cls || clear') # Limpa o terminal.

n1 = float(input("Digite o primeiro numero: "))
operacao = input("Escolha uma operação (+, -, * ou / ): ")
n2 = float(input("Digite o segundo numero: "))


if operacao == "+":
    resultado = (n1 + n2)  

elif operacao == "-":
    resultado = 2(n1 - n2)

elif operacao == "*":
    resultado = (n1 * n2)

elif operacao == "/":
    resultado = (n1 / n2)

else:
    resultado = "Operação invalida"

    
print(f"Resultado: {n1} {operacao} {n2} = {resultado}")