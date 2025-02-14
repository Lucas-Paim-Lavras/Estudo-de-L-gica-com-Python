#Usando a biblioteca math
import math
n = float (input('Digite um número:'))
raiz = math.sqrt(n)
print ('A raiz de {} é igual a {:.2f}'. format (n, math.ceil(raiz)))

#Usando uma função específica da biblioteca math, no caso, a sqrt
from math import sqrt
n = float (input('Digite um número:'))
raiz = sqrt(n)
print ('A raiz de {} é igual a {:.2f}'. format (n, raiz))

#Usando dois comandos específicos da biblioteca math
from math import sqrt, floor
n = float (input('Digite um número:'))
raiz = sqrt(n)
print ('A raiz de {} é igual a {:.2f}'. format (n, floor (raiz)))

#Usando a biblioteca random que, gera valores aleatórios entre 0 e 1.
import random
num = random.random ()
print (num)

#Usando a função randint da biblioteca random pra gerar um valor aleatório de 1 a 100.
import random
num = float(random.randint (1, 100))
print (num)

import emoji
print (emoji.emojize('Olá mundo :thumbs_up:'))