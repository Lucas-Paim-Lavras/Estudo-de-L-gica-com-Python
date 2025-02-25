#teste 1:
def soma(a, b):
    s = a + b
    print (s)
#Programa Principal
soma(5, 8)
soma(9, 8)
soma(7, 6)


#teste 2
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')
# Programa Principal
soma(5, 8)

#teste 3
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')
# Programa Principal
soma(b = 5, a = 8)

#teste 4: Empacotamento (apenas no python)
def contador(* num):
    print(num)

#Programa principal
contador (2, 1, 7)
contador (8, 90)               #Cria Tuplas
contador (4, 1, 3, 5)

#teste 5
def contador(* num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')

#Programa principal
contador (2, 1, 7)
contador (8, 90)               #Cria Tuplas
contador (4, 1, 3, 5)

#teste 6
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')

#Programa principal
contador (2, 1, 7)
contador (8, 90)               #Cria Tuplas
contador (4, 1, 3, 5)

#teste 7
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

#Programa principal
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

#teste 8
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

#Programa principal
soma(5, 2)
soma(5, 6, 9)
