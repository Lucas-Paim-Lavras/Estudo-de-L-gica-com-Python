#Leia um número inteiro e diga se ele é um número primo
print('\033[1;33mBem vindo ao verificador de números primos!!!\033[m')
tot = 0
n = int(input('Digite um número para saber se ele é primo: '))
if n <= 0:
    print('Não existe número primo negativo. Tente novamente.')
for c in range (1, n + 1):
    if n % c == 0:
        print('\033[33m', end='  ')
        tot = tot + 1
    else:
        print('\033[31m', end='  ')
    print(f'{c}', end='')
print(f'\n\033[mO número {n} foi divísel {tot} vezes')
if tot == 2:
    print('Logo, ele é primo')
else:
    print('Logo ele é não primo')
