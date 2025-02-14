#Desafio 028: Um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O computador deve escrever na tela se o usuáro venceu ou perdeu.
import random
ThinkNum = random.randint (0, 5)
n = int(input('Tente adivinhar: Qual o número que eu estou "pensando" entre 0 e 5 '))
if n == ThinkNum:
    print ('Yeah! Você acertou! :D')
else:
    print ('Puts, você errou :(')

#Desafio 029: Leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.
v = float(input('Qual a velocidade registrada?'))
x = (v-80)
if v > 80:
    print ('Você ultrapassou o limite de velocidade. Sua multa é {}'. format (x*7))
else:
    print('Você não foi multado.')

#Desafio 030: Um programa que defina se um número é par ou ímpar.
n = int(input('Digite um número:'))
if n % 2 == 0:
    print('O número é par:')
else:
    print('O número é ímpar:')

#Desafio 031: Pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.
d = float(input('Qual a distância da viagem em km?'))
if d <= 200:
    print('O valor da passagem é: {}'. format (d*0.5))
else:
    print('O valor da passagem é: {}'. format (d*0.45))

#Desafio 032: Um programa que leia um ano qualquer e mostre se ele é bissexto
a = int(input('Digite um ano qualquer:'))
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print ('O ano é bissexto!')
else:
    print ('O ano não é bissexto!')

#Desafio 032: usando a biblioteca calendar
import calendar
a = int(input('Digite um ano qualquer:'))
if calendar.isleap(a):
    print ('É um ano bissexto!')
else:
    print ('Não é um ano bissexto!')

#Desafio 033: Leia três números e mostre qual é o maior e qual o menor
n1 = float(input('Digite o primeiro número:'))
n2 = float(input('Digite o segundo número:'))
n3 = float(input('Digite o terceiro número:'))

#Maior número:
if n1 > n2 and n1 > n3:
    print('{} é o maior número'. format(n1))
else:
    print('')
if n2 > n1 and n2 > n3:
    print('{} é o maior número'. format(n2))
else:
    print('')
if n3 > n2 and n3 > n1 :
    print('{} é o maior número'. format(n3))
else:
    print('')

#Menor número:
if n1 < n2 and n1 < n3:
    print('{} é o menor número'. format(n1))
else:
    print('')
if n2 < n1 and n2 < n3:
    print('{} é o menor número'. format(n2))
else:
    print('')
if n3 < n2 and n3 < n1 :
    print('{} é o menor número'. format(n3))
else:
    print('')

#Desafio 034: Pergunte o salário de um funcionário e calcule o valor do seu aumento. 
#Para salários superiores a R$1250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.
p = float(input('Qual o salário do funcionário?'))
if p <= 1250:
    print ('Quem ganhava R${:.2f} passa a ganhar R${:.2f}' . format(p, p*1.15))
else:
    print ('Quem ganhava R${:.2f} passa a ganhar R$ {:.2f}' .format(p, p*1.1))

#Desafio 035: Um programa que leia o comprimento de três retas e diaga ao isiário se elas podem ou não formar um triângulo.
r1 = float(input('Digite o comprimento da primeira reta'))
r2 = float(input('Digite o comprimento da segunda reta'))
r3 = float(input('Digite o comprimento da terceira reta'))
if r1 > (r2 + r3) or r2 > (r1 +r3) or r3 > (r1 + r2):
    print ('As três retas formam um triângulo')
else:
    print ('As três retas não formam um triângulo')

