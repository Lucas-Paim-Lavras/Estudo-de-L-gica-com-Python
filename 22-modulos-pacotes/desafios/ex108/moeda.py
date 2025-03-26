def metade(p=0):
    res = p *0.5
    return res

def dobro(p=0):
    res = p * 2
    return res

def aumentar(p=0, n=0):
    res = p * (1 + n/100)
    return res

def diminuir(p=0, n=0):
    res = p * (1 - n/100)
    return res

def moeda(p = 0, moeda = 'R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')