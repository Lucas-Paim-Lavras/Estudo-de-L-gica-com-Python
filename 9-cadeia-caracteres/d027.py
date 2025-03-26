#Desafio 027: Um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
nome = str(input('Digite seu nome completo:')). strip()
dividido = nome.split()
print ('Primeiro nome: {}'. format (dividido[0]))
print ('Último nome: {}'. format (dividido[-1]))     #O item -1 retorna ao último elemento da lista