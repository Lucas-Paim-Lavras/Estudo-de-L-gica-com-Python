#Desafio 006: Crie um algoritmo que leia um número e mostre o seu dobro triplo e raiz quadrada

n = float (input('Digite um número:'))
d = 2*n
t = 3*n
r = n**(1/2)
print ('O seu dobro é {}, o seu triplo é {}, e sua raiz quadrada é {:.2f}'. format (d, t, r))