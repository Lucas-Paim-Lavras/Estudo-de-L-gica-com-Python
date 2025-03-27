#Desafio 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Nota de matemática:'))
n2 = float(input('Nota de física:'))
m = (n1+n2)/2
print ('A média das notas é {}'. format (m))