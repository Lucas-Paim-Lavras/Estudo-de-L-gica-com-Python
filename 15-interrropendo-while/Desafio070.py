#Desafio 070: leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
#Qual é o total gasto na compra.
#Quantos produtos custam mais de R$1000,00
#Qual é o nome do produto mais barato.
print ('-'*30)
print ('     LOJA SUPER BARATÃO       ')
print ('-'*30)

CountMaiorMil = total = preçoBarato = count = 0
nomeBarato = ''

#Estrutura de laço de repetição para cadastrar os dados.
while True:
    nome = str(input ('Nome do Produto: ')).strip()
    preço = float(input('Preço: R$'))
    total += preço
    count += 1

    #Contador de produtos que custam mais que R$1000,00
    if preço > 1000:
        CountMaiorMil += 1
    
    #Produto mais barato
    if count == 1:            #Aqui eu to dizendo que, se tiver apenas um produto, ele será o barato.
        preçoBarato = preço
        nomeBarato = nome
    else:
        if preço < preçoBarato:        #Já aqui, se tiver outro produto com um preço menor do que o do primeiro, ele será o mais barato.
            preçoBarato = preço
            nomeBarato = nome

    #Critério de parada do while True
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar o cadastramento? [S/N] ')) .strip().upper()[0]
    if continuar == 'N':
        break
print( '-' *10, 'FIM DO PROGRAMA','-' *10,)
print('O total da compra foi R${:.2f}'.format(total))
print(f'Temos {CountMaiorMil} produto(s) cutando mais de R$1000.00')
print(f'O produto mais barato foi a/o {nomeBarato} que custa R${preçoBarato:.2f}')
