#Desafio 096: função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a
#área do terreno.
def area(l, c):
    area = l * c
    print(f'A área de um terreno {l} x {c} é de {area} m²')

print('Controle de Terrenos')
print('-'*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)