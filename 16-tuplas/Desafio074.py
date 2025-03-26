#Desafio074: Um programa que gere 5 números aleatórios e colocar em uma tupla.
#depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
import random
maior = menor = 0
numeros = ()
print('Os valores sorteados são: ')

for c in range (0, 5):
    numero = random.randint(0, 100)
    print(numero, end=' -> ' if c < 4 else '')  # Remove a última setinha
    numeros += (numero,)

#Maior e menor
    if c == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
print()
print (f'O maior valor foi {maior} e o menor foi {menor}')



