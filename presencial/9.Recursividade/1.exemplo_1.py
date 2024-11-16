import os
import time as t

os.system('cls || clear')

def contagem_regressiva(x):
    if x < 0:
        return
    print(x)
    t.sleep(2)
    contagem_regressiva(x - 1)


contagem_regressiva(5)