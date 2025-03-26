#Desafio 018: Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import sin, cos, tan, radians
a = float(input('Digite um valor de ângulo em graus:'))
a_graus = radians(a)
s = sin(a_graus)
c = cos(a_graus)
t = tan(a_graus)
print('O seu seno é {:.2f} \n O seu cosseno é {:.2f} \n A sua tangente é {:.2f}'. format (s, c, t))