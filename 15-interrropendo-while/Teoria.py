cont = 1
while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print ('Acabou!')

#Testar o While True pra dizer que ele fica infinito. Se eu coloco no exercício anterior um while True ele conta
# pra sempre.

cont = 1
while True:
    print(cont, '-> ', end='')
    cont += 1
print ('Acabou!')

#Testando o exercício do 999 usando break e o while True
n = s = 0
while True:
    n = int (input('Digite um número: '))
    if n == 999:
        break         #O interessante do comando break é que ele sai do while, não contando o 999. Lembrar as setinhas no tablet.
    s += n
print ('A soma vale {}'.format(s))