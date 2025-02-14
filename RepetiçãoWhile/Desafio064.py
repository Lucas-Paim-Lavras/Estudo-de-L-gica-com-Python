#Desafio 064: pede valores enquanto não for 999 e some os valores, com exceção do 999. PRIMEIRA FORMA
n = 0
soma = 0
c = 0
while n != 999:
    n = float(input('Digite um número [999 para parar]: '))
    soma = soma + n
    c += 1
print (f'Você digitou {c-1} números e a soma entre eles é {soma-999}')
print ('FIM')


#Desafio 064: pede valores enquanto não for 999 e some os valores, com exceção do 999. SEGUNDA FORMA
n = 0
soma = 0
c = 0
n = float(input('Digite um número [999 para parar]: '))
while n != 999:
    soma = soma + n
    c += 1
    n = float(input('Digite um número [999 para parar]: '))
print (f'Você digitou {c} números e a soma entre eles é {soma}')
print ('FIM')