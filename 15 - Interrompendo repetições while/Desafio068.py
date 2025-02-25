#Desafio 068: um programa que joga par ou ímpar com o computador. O jogo será interrompido quando o jogador perder
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print ('-=' *20)
print ('VAMOS TIRAR PAR OU ÍMPAR?')
print ('-=' *20)
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint (0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PIÍ':
        tipo = str (input('Par ou ímpar? ')) .strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print ('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:     #O resto da divisão inteira de um número ímpar por 2 é 1.
            print ('Você venceu!')
            v += 1
        else:
            print ('Você perdeu!')
            break
    print('Vamos jogar novamente ... ')
print(f'GAME OVER! Você venceu {v} vezes!') 



