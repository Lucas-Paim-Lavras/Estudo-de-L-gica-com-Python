#Desafio 102: Tenha uma função fatorial() que receba dois parãmetros: o primeiro que indique o número a calcular
# e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.

def linha():
    print('-'*40)

def fatorial (num=1, show=False):
    """
    -> Calcule o fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) mostrar ou não a conta
    :return: o valor do fatorial de um número n
    """
    linha()
    f = 1
    for c in range (num, 0, -1):
        if show:
            print (c, end = '')
            if c > 1:
                print(' x ', end = '')
            else:
                print(' = ', end = '')
        f *= c
    return f

# Programa Principal
print(fatorial(5, show=True))
