#Desafio 091: Um programa que 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número dado.

from random import randint
from time import sleep
from operator import itemgetter

resultados = {}
ranking = []

print('Valores sorteados:')
for j in range (1, 5):
    resultados['resultado']=randint(1, 6)
    for r in resultados.values():
        print(f'O jogador {j} tirou {r}')
        sleep(0.5)

ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)    #Comando essencial para ordenar dicionários. Me dá um resultado em lista com várias tuplas dentro.

print('Ranking dos jogadores: ')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.5)
