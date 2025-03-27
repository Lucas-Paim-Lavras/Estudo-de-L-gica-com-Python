#Desafio 008: Escreva um programa que leia um valor em metros e converta-o para centímetros e milímetros
n = float(input('Digite o valor da medida em metros:'))
cm = n*100
mm = n*1000
print ('O valor em centímetros é {}, e o valor em milímetros é {}'. format(cm, mm))