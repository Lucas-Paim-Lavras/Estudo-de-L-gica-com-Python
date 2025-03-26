#Desafio 024: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'
cidade = str(input('Digite o nome de uma cidade:')). strip()
print(cidade[:5] == 'Santo')     #Eu usei até o 5 porque, começa em 0 e termina em 4 e a gente passa pra pegar o último caractere

#Desafio 025: Um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome
# nome = str(input('Digite seu nome:')). strip()
# print ('Seu nome tem Silva? {}'. format('SILVA' in nome.upper))