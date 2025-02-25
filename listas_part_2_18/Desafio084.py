#Desafio 084: Leia o nome e peso de várias pessoas e guaradar tudo em uma lista.
# A)Quantas pesoas foram cadastradas?
# B) Uma listagem com as pessoas mais pesadas
# C) uma listagem com as pessoas mais leves.

pessoas = []
dado = []
continuar = ' '
maior = menor = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso em kg: ')))
    if len(pessoas) == 0:               #Quando aprender função. Defini-la pra não precisar fazer mais.
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado [1]
        if dado [1] < menor:
            menor = dado [1]
    pessoas.append(dado[:])
    dado.clear()
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0].capitalize()
        if continuar in ['Sim', 'Não', 'S', 'N', 'n', 's']:
            break
        print('Entrada Inválida. Digite apenas [Sim/Não] ou [S/N]')
    if continuar == 'N':
        break

print('-='*30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior} kg. Peso de', end= ' ')
for p in pessoas:
    if p[1] == maior:
        print (f'[{p[0]}]')
print(f'O menor peso foi de {menor} kg. Peso de', end= ' ')
for p in pessoas:
    if p[1] == menor:
        print (f'[{p[0]}]')