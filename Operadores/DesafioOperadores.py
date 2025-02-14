#Desafio 005: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

n = int (input('Digite um número:'))
a = n-1
s = n+1
print ('Analisando o número {} seu antecessor é {}, e seu sucessor é {}'. format(n, a, s))

n = int (input('Digite um número'))
print ('Analisando o número {} seu antecessor é {}, e seu sucessor é {}'. format(n, n-1, n+1))
#Desafio 006: Crie um algoritmo que leia um número e mostre o seu dobro triplo e raiz quadrada

n = float (input('Digite um número:'))
d = 2*n
t = 3*n
r = n**(1/2)
print ('O seu dobro é {}, o seu triplo é {}, e sua raiz quadrada é {:.2f}'. format (d, t, r))

#Desafio 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Nota de matemática:'))
n2 = float(input('Nota de física:'))
m = (n1+n2)/2
print ('A média das notas é {}'. format (m))

#Desafio 008: Escreva um programa que leia um valor em metros e converta-o para centímetros e milímetros
n = float(input('Digite o valor da medida em metros:'))
cm = n*100
mm = n*1000
print ('O valor em centímetros é {}, e o valor em milímetros é {}'. format(cm, mm))

#Desafio 009: Um programa que leia um número interiro qualquer e mostre na tela a sua tabuada
n = int(input('Digite um número:'))
t1 = n*1
t2 = n*2
t3 = n*3
t4 = n*4
t5 = n*5
t6 = n*6
t7 = n*7
t8 = n*8
t9 = n*9
t10 = n*10

print ('Sua tabuada é {},\n{},\n{},\n{},\n{},\n{},\n{},\n{},\n{},\n{}'. format (t1,t2,t3,t4,t5,t6,t7,t8,t9,t10))

#Desafio 010: Programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere Us$1,00 -> R$6,01

n = float(input('Quantos reais você tem?'))
d = n/6.01
print ('Você pode comprar {:.2f} dólares'. format (d))

#Desafio 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-lo, sabendo que cada litro de tinta, pinta uma área de 2m²

l = float(input('Qual a largura da parede?'))
h = float(input('Qual a altura da parede?'))
a = l*h
t = a/2
print ('A área da parede é {:.2f} e são necessários {:.2f} litros de tinta para pintá-la'.format (a, t))

#Desafio 012: Que leia o preço de um produto e mostre o novo preço, com 5% de desconto.

n = float(input('Preço do produto, sem o desconto'))
d = n*(0.95)
print ('O preço do produto com um desconto de 5% é? {}'. format (d))

#Desafio 013: Leia o salário de um funcionário, e print com 15 por cento de aumento.

n = float(input('O seu salário, sem aumento é?'))
a = n*(1.15)
print ('O seu novo salário, com o aumento, será? {:.2f}'. format(a))

#Desafio 014: Conversor de temperatura de °C para °F

c = float (input('Informe a temperatura em °C:'))
f = (9/5)*c + 32
print ('A temperatura em °F para {} °C é: {} °F'. format (c, f))

#Desafio 015: Escreva um programa que pergunte a quantidade de km percorridos por um carro alugad e a quantidade de dias pelos quais ele foi alugad. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 pr km rodado.

d = int (input('Por quantos dias o carro foi alugado?'))
km = float (input('Quantos quilômetros foram rodados?'))
print ('O total a pagar pelo aluguel é R${:.2f}'. format(d*60 + km*0.15))
