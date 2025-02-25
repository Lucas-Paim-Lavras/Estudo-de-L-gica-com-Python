#Desafio 079: o usuário pode digitar vários valores numéricos e cadastre-os em uma lista. Caso o número
#já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados
#, em ordem crescente.
continuar = ' '
valor = []
while True:
    numeros = int(input('Digite um valor: '))
    if numeros not in valor:
        print ('Valor adicionado com sucesso ...')
    else:
        ultimo = valor.pop()
        print('Valor duplicado! Não vou adicionar!')
    valor.append(numeros)
    valor.sort()
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0].capitalize()
        if continuar in ['Sim', 'Não', 'S', 'N', 'n', 's']:
            print('Certo. Continuemos')
            break
        print('Entrada Inválida. Digite apenas [Sim/Não] ou [S/N]')
    if continuar == 'N':
        break
print('-='*30)
print(f'Você digitou os valores {valor}')