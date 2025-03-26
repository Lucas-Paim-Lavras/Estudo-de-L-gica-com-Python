#Desafio 020: Sortear a ordem de apresentação dos alunos. Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada
from random import shuffle
a1 = str(input('Digite o nome do aluno 1:'))
a2 = str(input('Digite o nome do aluno 2:'))
a3 = str(input('Digite o nome do aluno 3:'))
a4 = str(input('Digite o nome do aluno 4:'))
lista = [a1, a2, a3, a4]                      #só pra definir uma lista dos nomes
shuffle(lista)                                #Embaralha a lista de alunos
print ('A ordem de apresentação será {}'. format (lista))