#Desafio 063: Um programa que mostre a quantidade de termos de uma sequência de Fibonacci
print ('-'*50)
print ('SEQUÊNCIA DE FIBONACCI')
print ('-'*50)
termos = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*50)
if termos ==1:
    print (f'{t1}', end= '')
else:
    print (f'{t1} -> {t2}', end= '')
cont = 3
while cont <= termos:
    t3 = t1 + t2
    print (f' -> {t3}', end= '')
    t1 = t2
    t2 = t3
    cont += 1
print (' -> FIM')