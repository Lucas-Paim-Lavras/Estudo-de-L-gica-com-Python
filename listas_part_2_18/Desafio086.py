#Desafio 086: Crie uma matriz 3x3 e preencha com valores lidos pelo teclado. No final mostre a matriz na tela, com a formatação correta.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range (0, 3):
    for j in range (0, 3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))

print('-='*30)
for i in range (0, 3):
    for j in range (0,3):
        print(f'[{matriz[i][j]:^7}]', end='')
    print()