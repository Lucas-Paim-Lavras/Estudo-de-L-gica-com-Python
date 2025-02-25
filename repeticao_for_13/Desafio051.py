#Desafio051: leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

#Leitura do primeiro termo de uma PA
a1 = int(input('Digite o primeiro termo de uma Progressão aritmética. a1 = '))

#leitura da razão de uma PA
r = int(input('Digite o valor da razão de uma Progressão aritmética. r = '))

n = 11

an = a1 + (n-1)*r

#Estrura de laço
print ('Os 10 primeiros termos da PA n')
for c in range(a1, an, r):
    print (c)
