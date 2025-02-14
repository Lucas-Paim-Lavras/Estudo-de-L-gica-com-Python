#Desafio 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão 20% de juros.

preço = float(input('Qual o preço do produto em R$'))
print('''Qual a condição de pagamento?
[ 1 ]: à vista dinheiro / cheque: 10 por cento de desconto.
[ 2 ]: à vista no cartão: 5 por cento de desconto.
[ 3 ]: em até 2x no cartão: preço normal
[ 4 ]: 3x ou mais no cartão: 20 por cento de juros''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('Com o desconto de 10 por cento, o valor do produto fica: R${:.2f}'.format(preço*0.9))
elif opção == 2:
    print('Com essa opção o produto sai a R${:.2f}'. format(preço*0.95))
elif opção == 3:
    print('Com essa opção, você não tem descontos, logo o valor a ser pago é R${:.2f}'. format(preço))
elif opção == 4:
    print('Nessa opção você pagará uma taxa de juros e o valor total fica R${:.2f}'. format(preço*1.2))
else:
    print('Entrada inválida! Digite apenas uma das opções!!')