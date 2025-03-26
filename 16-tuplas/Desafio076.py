#Desafio076:
print('-'*40)
print('LISTAGEM DE PREÇOS'.center(40))
print('-'*40)
listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
largura_total = 40
for i in range (0, len(listagem), 2):      #Interessante
    produto = listagem[i]
    preço = listagem [i+1]
    pontos = '.'*(largura_total-len(produto)-len(f'R$ {preço:.2f}'))
    print(f'{produto}{pontos} R${preço:.2f}')
print('-'*40)