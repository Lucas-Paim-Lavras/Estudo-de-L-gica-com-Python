#Desafio 081: Extraindo dados de uma lista.
# a)Quantos números foram digitados
# b) A lista de valores, ordenada de forma decrescente
# c) Se o valor 5 foi digitado e está ou não na lista.
numero = 5
valor = []
continuar = ' '
while True:
    numeros = int(input('Digite um valor: '))
    valor.append(numeros)
    valor.sort(reverse=True)
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0].capitalize()
        if continuar in ['Sim', 'Não', 'S', 'N', 'n', 's']:
            break
        print('Entrada Inválida. Digite apenas [Sim/Não] ou [S/N]')
    if continuar == 'N':
        break

print("-="*30)
print(f'Você digitou {len(valor)} elementos.')
print(f'Os valores em ordem decrescente são {valor}')
if numero in valor:
    print(f'O número {numero} faz parte da lista!')
else:
    print(f'O número {numero} não foi encontrado na lista!')
