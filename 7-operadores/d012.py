#Desafio 012: Que leia o preço de um produto e mostre o novo preço, com 5% de desconto.

n = float(input('Preço do produto, sem o desconto: R$'))
porce = int(input('Digite o desconto em porcentagem que você quer dar ao cliente: '))
d = n*(1-(porce/100))
print ('O preço do produto com um desconto de {}% é? R${:.2f}'. format (porce, d))