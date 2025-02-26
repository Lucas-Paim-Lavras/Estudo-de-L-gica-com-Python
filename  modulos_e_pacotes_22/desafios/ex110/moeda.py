def metade(p=0, formato=False):
    res = p *0.5
    return res if formato is False else moeda(res)

def dobro(p=0, formato=False):
    res = p * 2
    return res if formato is False else moeda(res)

def aumentar(p=0, n=0, formato=False):
    res = p * (1 + n/100)
    return res if formato is False else moeda(res)

def diminuir(p=0, n=0, formato=False):
    res = p * (1 - n/100)
    return res if formato is False else moeda(res)

def moeda(p = 0, moeda = 'R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')

def resumo(p=0, aumenta=0, diminui=0):
    print('-'*40)
    print(f'RESUMO DO VALOR'.center(40))
    print('-'*40)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'80% de aumento: \t{aumentar(p, aumenta, True)}')
    print(f'35% de redução: \t{diminuir(p, diminui, True)}')
    print('-'*40)