#Desafio 016: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção interia
#Ex: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.

import math
n = float(input('Digite um número:'))
i = math.floor(n)
print ('O número {} tem a parte inteira {}'. format(n, i))

#Desafio 017: Leia o cateto oposto e o adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

from math import pow, sqrt
co = float(input('Qual é o cateto oposto?'))
ca = float(input('Qual o valor do cateto adjacente?'))
h = sqrt(pow(co, 2) + pow(ca, 2))
print ('A hipotenusa do triângulo retângulo é {:.2f}'. format(h))

#Desafio 018: Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import sin, cos, tan, radians
a = float(input('Digite um valor de ângulo em graus:'))
a_graus = radians(a)
s = sin(a_graus)
c = cos(a_graus)
t = tan(a_graus)
print('O seu seno é {:.2f} \n O seu cosseno é {:.2f} \n A sua tangente é {:.2f}'. format (s, c, t))

#Desafio 019: Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Um programa que leia os nomes deles e sorteie o nome de um deles.
import random
a1 = str(input('Digite o nome do aluno 1:'))
a2 = str(input('Digite o nome do aluno 2:'))
a3 = str(input('Digite o nome do aluno 3:'))
a4 = str(input('Digite o nome do aluno 4:'))
s = random.choice([a1, a2, a3, a4])
print (f'O aluno sorteado é {s}')

#Desafio 020: Sortear a ordem de apresentação dos alunos. Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada
from random import shuffle
a1 = str(input('Digite o nome do aluno 1:'))
a2 = str(input('Digite o nome do aluno 2:'))
a3 = str(input('Digite o nome do aluno 3:'))
a4 = str(input('Digite o nome do aluno 4:'))
lista = [a1, a2, a3, a4]                      #só pra definir uma lista dos nomes
shuffle(lista)                                #Embaralha a lista de alunos
print ('A ordem de apresentação será {}'. format (lista))

#Desafio 021: Um programa em python que abra e reproduza o áudio de um arquivo em mp3
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)