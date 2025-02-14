#Desafio042: Refaça o desafio 035 dos triângulos, arescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

#Eu tentando
r1 = float(input('Digite o comprimento da primeira reta:'))
r2 = float(input('Digite o comprimento da segunda reta:'))
r3 = float(input('Digite o comprimento da terceira reta:'))
if r1 < (r2 + r3) and r2 < (r1 +r3) and r3 < (r1 + r2):
    print ('As três retas não formam um triângulo')
elif r1 == r2 == r3:
    print ('Temos um triângulo equilátero. Uma vez que todos os lados tem mesma medida.')
elif (r1 == r2) or (r1 == r3) or (r2 == r3):
    print ('Temos um triângulo isósceles. Uma vez que dois lados tem mesma medida.')
elif r1 != r2 != r3:
    print ('Temos um triângulo escaleno. Visto que todos os lados tem medidas diferentes.')
else:
    print ('As três retas não formam um triângulo')

#O que o chat gpt me fez
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

# Verificar se as retas formam um triângulo
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    # Verificar o tipo de triângulo
    if r1 == r2 == r3:
        print('Temos um triângulo equilátero. Uma vez que todos os lados têm a mesma medida.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Temos um triângulo isósceles. Uma vez que dois lados têm a mesma medida.')
    else:
        print('Temos um triângulo escaleno. Visto que todos os lados têm medidas diferentes.')
else:
    print('As três retas não formam um triângulo.')
