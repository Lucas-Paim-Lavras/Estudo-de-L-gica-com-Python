#Desafio 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-lo, sabendo que cada litro de tinta, pinta uma área de 2m²

l = float(input('Qual a largura da parede?'))
h = float(input('Qual a altura da parede?'))
a = l*h
t = a/2
print ('A área da parede é {:.2f} e são necessários {:.2f} litros de tinta para pintá-la'.format (a, t))