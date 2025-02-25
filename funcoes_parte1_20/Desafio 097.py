#Desafio 097: Que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(msg):
    tamanho = len(msg) + 2
    print('-'*(tamanho))
    print(f'{msg.center(tamanho)}')
    print('-'*(tamanho))

escreva('BERIMBAL CABEÇA DE MELÃO')
escreva('WWE LUTA LIVRE NA TV')