#Desafio 017: Leia o cateto oposto e o adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

from math import pow, sqrt
co = float(input('Qual é o cateto oposto?'))
ca = float(input('Qual o valor do cateto adjacente?'))
h = sqrt(pow(co, 2) + pow(ca, 2))
print ('A hipotenusa do triângulo retângulo é {:.2f}'. format(h))