#Desafio 093: Um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
#e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será 
#guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

gerenciador = {}
i = 0

gerenciador['nome'] = str(input('Nome do Jogador: '))

gerenciador['gols'] = []

quantidade = int(input(f'Quantas partidas {gerenciador["nome"]} jogou? '))
for j in range (1, quantidade + 1):
    gols = int(input(f'Quantos gols na partida {j}? '))
    gerenciador['gols'].append(gols)
    gerenciador['total'] = sum(gerenciador['gols'][:])

print('-='*30)

print(gerenciador)

print('-='*30)

for k, v in gerenciador.items():
    print(f'O campo {k} tem o valor {v}')

print('-='*30)

print(f'O jogador {gerenciador["nome"]} jogou {quantidade} partidas.')
for i in range (quantidade):
    print(f'   => Na partida {i+1}, fez {gerenciador["gols"][i]} gols.')
print(f'Foi um total de {gerenciador["total"]} gols.')