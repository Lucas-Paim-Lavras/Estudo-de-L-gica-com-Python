#Desafio 087: A partir do desafio anterior.
# A) A soma de todos os valores pares
# B) A soma dos valores da terceira coluna
# C) O maior valor da segunda linha
pares = []
SomaPares = soma3 = maior = 0

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range (0, 3):
    for j in range (0, 3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
        if matriz[i][j] % 2 == 0:
            SomaPares += matriz[i][j]
        
        #Soma elementos da terceira coluna
        if j == 2:
            soma3 += matriz[i][j]
        
#Maior valor da segunda linha
maior = max(matriz[1])        

print('-='*30)
for i in range (0, 3):
    for j in range (0,3):
        print(f'[{matriz[i][j]:^7}]', end='')
    print()
print('-='*30)
print(f'A soma dos valores pares é {SomaPares}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {maior}')