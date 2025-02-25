#Teste 01
for c in range(1, 6):     #No terminal aparece apenas 5 Oi's. Isso porque no python, no fatiamento, o sexto caracter não aparece.
    print('Oi')
print('FIM')

#Teste 02
for c in range(0, 6):     #No terminal aparece apenas 5 Oi's. Isso porque no python, no fatiamento, o sexto caracter não aparece.
    print('Oi')
print('FIM')

#Teste 03
for c in range(1, 7):     #No terminal aparece apenas 5 Oi's. Isso porque no python, no fatiamento, o sexto caracter não aparece.
    print(c)
print('FIM')

#Teste 04
for c in range(6, 0):        #Nesse caso ele vai direto pro FIM
    print(c)
print ('FIM')

#Teste 05
for c in range(6, 0,-1):     #O -1 indica que vai ser ao contrário. 
    print(c)
print('FIM')

#Teste 06
for c in range(0, 7, 2):    #Nesse caso eu vou fazer com que ele conte de 0 a 6 de dois em dois. Ótima forma pra determinar números pares.
    print(c)
print ('FIM')

#Teste 07
n = int(input('Digite um número'))
for c in range (0, n):
    print(c)
print ('Fim')

#Teste 08:
n = int(input('Digite um número'))
for c in range (0, n+1):
    print(c)
print ('Fim')

#Teste 09:
i = int(input('Início:'))
f = int(input('Fim:'))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM.')

#Teste 10:
for c in range(0, 12):
    n = int(input('Digite um valor: '))
print('Fim')

#Teste 11:
s = 0
for c in range (0, 4):
    n = int(input('Digite um valor'))
    s = s + n
print('O somatório de todos os valores foi {}'. format(s))
