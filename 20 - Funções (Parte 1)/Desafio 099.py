#Desafio 099: tenha uma função maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar
#todos os valores e dizer qual deles é o maior.
from time import sleep

def linha():
    print('-='*30)

def maior(*num):
    linha()
    print('Analisando os valores passados ...')
    if len(num) == 0:
        print('Nenhum valor foi informado.')
    else:
        for n in num:
            print(n, end=' ', flush = True)
            sleep(0.1)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}')
    

#Programa principal
maior (2, 1, 7, 5, 8, 24, 8765,1234)
maior (3, 2, 3, 4, 22, 32, 23, 23, 23)        
maior (4, 1, 3, 5)