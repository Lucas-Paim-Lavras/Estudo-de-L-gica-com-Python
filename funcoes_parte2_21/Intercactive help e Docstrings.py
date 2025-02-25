import time

def contador(i, f, p):
    #Docstrings
    """
    -> Faz a contagem e mostra na tela.
    :parametro i: início da contagem
    :parametro f: fim da contagem
    :parametro p: passo da contagem         
    :return: sem retorno
    
    Função criada por Lucas Paim
    """
    c = i
    while c <= f:
        print(f'{c}', end='..', flush = True)
        c += p
    print('FIM')

help(contador)