#Desafio 050: leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar. Desconsidere-o
s = 0
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))
n5 = int(input('Digite o quinto número: '))
n6 = int(input('Digite o sexto número: '))

numeros = [n1, n2, n3, n4, n5, n6]
for c in numeros:
    if c % 2 == 0:
        s = s + c
    else:
        print(f'O número {c} é ímpar e será desconsiderado')
print(f'A soma de todos os números pares é {s}')