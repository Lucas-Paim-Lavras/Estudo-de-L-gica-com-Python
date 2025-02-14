#Um programa que leia um número qualquer e mostre o seu fatorial
n = int(input('Digite um número: '))
contador = n
factorial = 1
while contador > 0:
    if contador == 1:
        print (f'{contador} = ', end='')
    else:
        print (f'{contador} x ', end='')
    factorial *= contador
    contador -= 1
print (factorial)