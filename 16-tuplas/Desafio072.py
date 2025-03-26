#Desafio072: Um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zero até vinte.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numero = 0
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while numero >= 20 or numero <= 0:
    print('Por favor. Digite apenas um número do intervalo de 0 e 20.')
    numero = int(input('Digite um número entre 0 e 20: '))
print (f'Você digitou o número {extenso[numero]}.')
