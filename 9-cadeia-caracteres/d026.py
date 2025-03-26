#Desafio 026: Um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra 'A'
#Em que posição ela aparece pela primeira vez.
#Em que posição ela aparece a última vez
frase = str(input('Escreva uma frase:')). strip(). upper()
print ('Nessa frase a letra "A", maiúcula aparece: {}'. format (frase.count('A')))
print ('Nessa frase, a posição que a letra "A", maúiscula, aparece pela primeira vez é: {}' . format (frase.find('A')+1))
print ('Nessa frase, a posição que a letra "A", maiúscula, aparece pela última vez é: {}' . format (frase.rfind('A')+1))