import os

os.system('cls || clear') # Limpa o terminal.

n1 = float(input("Digite o primeiro numero: "))
operacao = input("Escolha uma operação (+, -, * ou / ): ")
n2 = float(input("Digite o segundo numero: "))

match (operacao):
    case "+":
        resultado = n1 + n2
    case "-":
        resultado = n1 - n2
    case "*":
        resultado = n1 * n2
    case "/":
        resultado = n1 / n2
    case _ :
        resultado = "Opção invalida"
        
print(f"Resultado: {n1} {operacao} {n2} = {resultado}")