import os


os.system('cls || clear')

n1 = float(input('Digite a primeira nota : '))
n2 = float(input('Digite a segunda nota : '))
n3 = float(input('Digite a terceira nota : '))
soma = n1, n2, n3
media = sum(soma) / 3

if media >= 7:
    print(f'Suas notas são {n1}, {n2} e {n3} sua media é {media} e você esta aprovado!')
elif media >= 5:
    print(f'Suas notas são {n1}, {n2} e {n3} sua media é {media} e você de recuperação!')
else:
    print(f'Suas notas são {n1}, {n2} e {n3} sua media é {media} e você esta reprovado!')