#Desafio 091: Um programa que 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número dado.

from random import randint
from time import sleep
from operator import itemgetter

resultados = {'jogador 1': randint(1, 6),
              'jogador 2': randint(1, 6),
              'jogador 3': randint(1, 6),
              'jogador 4': randint(1, 6)}
ranking = []
print('Valores sorteados:')
for k, v in resultados.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)

ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)    #Comando essencial para ordenar dicionários. Me dá um resultado em lista com várias tuplas dentro.
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.5)