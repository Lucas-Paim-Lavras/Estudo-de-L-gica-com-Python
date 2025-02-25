#Teste 01:
num = [1, 2, 3, 4]
num[2] = 3                    #listas são mutáveis
print (num)

#Teste 02:
num = [1, 2, 3, 4]
num[2] = 3
num.append(7)               
print (num)

#Teste 03:
num = [9, 8, 7, 9, 20, 10]
num[2] = 3
num.append(7)
num.sort()           
print (num)

#Teste 04:
num = [9, 8, 7, 9, 20, 10]
num[2] = 3
num.append(7)
num.sort(reverse=True)           
print (num)

#Teste 05:
num = [9, 8, 7, 9, 20, 10]
num[2] = 3
num.append(7)
num.sort(reverse=True)           
print (num)
print(f'Essa lista tem {len(num)} elementos')

#Teste 06:
num = [9, 8, 7, 9, 20, 10]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)      
print (num)
print(f'Essa lista tem {len(num)} elementos') 

#Teste 07:
num = [9, 8, 7, 9, 20, 10]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)  
num.pop()       
print (num)
print(f'Essa lista tem {len(num)} elementos')

#Teste 08:
num = [9, 8, 7, 9, 20, 10]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)  
num.pop(2)       
print (num)
print(f'Essa lista tem {len(num)} elementos')

#Teste 09:
num = [9, 8, 7, 9, 20, 10]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 7)
num.remove(7)     #removo apenas o primeiro elemento (ele procura o número da lista)
print (num)
print(f'Essa lista tem {len(num)} elementos')

#Teste 10:
num = [9, 8, 7, 9, 20, 10]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 7)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4!')
print (num)
print(f'Essa lista tem {len(num)} elementos')

#Teste 11:
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v} ...', end= '')

#Teste 12:
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

#Teste 13:    Achei chique!
valores = []

for cont in range (0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

#teste 14:
a = [2, 3, 4, 7]
b = a

print (f'Lista A: {a}')
print (f'Lista B: {b}')

#Teste 15:
a = [2, 3, 4, 7]
b = a         #A partir do momento que eu igualo duas listas o python cria uma ligação entre elas. Tudo que muta em uma muta na outra
b[2] = 8
print (f'Lista A: {a}')
print (f'Lista B: {b}')

#Teste 16:
a = [2, 3, 4, 7]
b = a[:]         #Aqui eu faço com que o B receba os valores de 'a' uma cópia de 'a' não tendo relação entre os dois.
b[2] = 8
print (f'Lista A: {a}')
print (f'Lista B: {b}')