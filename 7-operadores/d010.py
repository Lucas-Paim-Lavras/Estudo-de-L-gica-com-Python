#Desafio 010: Programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere Us$1,00 -> R$6,01

n = float(input('Quantos reais você tem?'))
d = n/6.01
print ('Você pode comprar {:.2f} dólares'. format (d))