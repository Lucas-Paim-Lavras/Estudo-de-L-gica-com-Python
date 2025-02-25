#Teste 01
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') #O parênteses serve para tuplas.
print (lanche)

#Teste 02
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') #O parênteses serve para tuplas.
print (lanche[1])       #me mostra apenas o índice 1 que é o suco.

#Teste 03
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') #O parênteses serve para tuplas.
print (lanche[3])

#Teste 04
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') #O parênteses serve para tuplas.
print (lanche[-2])       #Quando colocamos os negativos é invertido e, claro, não existe -0.

#Teste 05
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') #O parênteses serve para tuplas.
print (lanche[1:3])    #segue a mesma lógica de fatiamento, não mostra o último elemento

#Teste 06
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') #O parênteses serve para tuplas.
print (lanche[2:])

#Teste 07
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') #O parênteses serve para tuplas.
print (lanche[:2])       #ignorou o elemento 2

#Teste 08
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') #O parênteses serve para tuplas.
print (lanche[-2:])   #ele começa na pizza e vai até o final

# #Teste 09
# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') #O parênteses serve para tuplas.
# #Tuplas são imutáveis
# lanche[1] = 'Refrigerante'
# print (lanche[1])   #Não vai dar certo. Poi tuplas são imutáveis

#Teste 10
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') #O parênteses serve para tuplas.
for comida in lanche:     #Antes usávamos o for como range agora usamos como itens.  
    print (f'Eu vou comer {comida}')
print ('Comi pra caramba')

#Teste 11
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita') #O parênteses serve para tuplas.
print(len(lanche))
# for comida in lanche:     #Antes usávamos o for como range agora usamos como itens.  
#     print (f'Eu vou comer {comida}')
print ('Comi pra caramba')

#Teste 12:
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for cont in range (0, len(lanche)):
    print(lanche[cont])   #Repara que aqui ele vai mostrar cada uma dos lanches. porque a formatação vai ficar lanche[0] depois lanche[1] e assim por diante.
    #O resultado é o mesmo de quando é usando FOR COMIDA IN LANCHE:

#Teste 13: Eu posso precisar mostrar a posição do elemento da tupla e eu posso fazer da seguinte maneira.
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba')

#Teste 14: O recurso enumerate
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida}na posição {pos}')  
    #Talvez essa é mais difícil mas me dá a oportunidade de colocar duas variáveis no for

#Teste 15:
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(sorted(lanche))  #Eu ordeno os itens da tupla.

#Teste 16:
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b    #Aqui vai concatenar as duas. Não é comutativo.
print (c)

#Teste 17:
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b 
print (len(c))      #Aqui ele vai mostrar quantos elementos vai ter a variável c

#Teste 18:
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.count(5))      #Quantas vezes tá aparecendo número 5 dentro de c

#Teste 19:
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print (c)
print(c.index(5))     #Ele pede pra mostrar em que posição está uma variável.

#Teste 20: E no caso em que as variáveis aparecem mais de uma vez. por exemplo a posição do 2
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(5))  #Aqui mostra, realmente, a posição do primeiro que aparece. Mas se eu qusier mostrar a posição do outro 5. devo usar

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(5, 1))  #Eu desloquei o meu intervalo para que ele comece a partir do primeiro, desconsiderando o 5 que tá na posição 0.

#Teste 21:
sexo = 'm'
peso = (74, 88, 29)
pessoa = ('Paim', 39, sexo , peso)
print (pessoa)       #Posso colocar números, strings e etc na mesma variável composta. Até mesmo outra variável e outra variável composta

#Teste 22:
pessoa = ('Paim', 39, 'M' , 74)
del(pessoa)  #Não consigo apagar apenas um elemento de uma tupla.
print(pessoa)