import os

os.system('cls || clear') # Limpa o terminal.

# Entrada.
notas = int(input("Digite uma nota: "))

#Processameto.
if notas >= 7:
    resultado = "Aprovado"
elif notas >= 5:
    resultado = "Recuperação"
elif notas >= 4:
    resultado = "Conselho de classe"
else:
    resultado = "Reprovado"

#Saída.

print(f"Resultado: {resultado}")