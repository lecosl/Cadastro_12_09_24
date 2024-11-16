import os

os.system('cls || clear')
comeco = 51
while True:
    if comeco % 7 != 0:
        comeco = comeco + 1
        print(comeco)
    else:
        print(f'O valor Divisivel por 7 acima de 50 é {comeco}')
        break