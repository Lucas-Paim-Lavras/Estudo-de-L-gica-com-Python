def soma(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra ao resultado na tela.
    :para: a: o primeiro valor
    :para: b: o segundo valor
    :para: c: o terceiro valor
    """
    s = a + b + c
    print(f'A soma é {s}!')
    
soma()
soma(b=7, a=88)
soma(9, 8, 0)
soma(9, 9, 9)
