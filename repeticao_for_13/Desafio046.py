#Um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifícios, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
from emoji import emojize
print (emojize('Vamos fazer a contagem regressiva para o ano de 2025???? :star-struck:'))
for c in range (10, -1, -1):
    sleep(1)
    print(c)
print (emojize(':star::star::star:FELIZ ANO NOVO!!!:fireworks: :sparkler: '))