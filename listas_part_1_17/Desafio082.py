#Desafio 082: dividindo valores em várias listas

lista = []
pares = []
impares = []
continuar = ' '
while True:
    numeros = (int(input('Digite um número: ')))
    lista.append(numeros)
    if numeros % 2 == 0:
        pares.append(numeros)
    elif numeros %  2 != 0:
        impares.append(numeros)
    while True:
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0].capitalize()
        if continuar in ['Sim', 'Não', 'S', 'N', 'n', 's']:
            break
        print('Entrada Inválida. Digite apenas [Sim/Não] ou [S/N]')
    if continuar == 'N':
        break
print('-='*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de pares é {impares}')