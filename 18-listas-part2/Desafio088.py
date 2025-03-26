#Desafio 088: Um programa que ajude um jogador da MEGA SENA  a criar palpites. O programa vai perguntar quantos jogos
#serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import sample
import time

sorteios = []
texto = 'MEGA SENA'
print('-'*30)
print(f'{texto:^30}')
print('-'*30)

quantidade = int(input('Quantos jogos você quer que eu sorteie? '))

for jogos in range (quantidade):
    jogo = sorted(sample(range(1, 61), 6))
    sorteios.append(jogo)

print('-'*30)
print('Números sorteados: ')
for i, jogos in enumerate(sorteios, start=1):
    print(f'Jogo {i}: {jogos}')
    time.sleep(0.5)
print ('Boa sorte!!')

