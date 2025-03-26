#Desafio 100: Um progama que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar().
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares
# sorteados pela função anterior

from time import sleep
from random import randint


def sorteio():
    numeros = []
    print('Sorteando 5 valores da lista: ', end='')
    for n in range (0, 5):
        numeros.append(randint(1, 1000000))
    for num in numeros:
        print(f'{num} ', end=' ', flush = True)
        sleep(0.3)
    print('PRONTO!')
    return numeros
    
def SomaPar(numeros):
    par = soma = 0
    for num in numeros:
        if num % 2 == 0:
            par = num
            soma += num
    print(f'Somando os valores pares de {numeros}, temos {soma}')


#Programa Principal
numerosSorteados = sorteio()
SomaPar(numerosSorteados) 

