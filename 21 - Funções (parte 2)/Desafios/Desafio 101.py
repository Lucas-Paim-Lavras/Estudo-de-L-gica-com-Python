# Desafio101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
#nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto
#negado, opicional ou obrigatório nas eleições.
def line():
    print('-'*30)

def voto(nasc):
    from datetime import date
    line()
    AnoAtual = date.today().year
    if nasc > AnoAtual:
        return 'ERRO! Digite um ano válido!'
    
    idade = AnoAtual - nasc
    
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 16 <= idade < 18 or idade > 70:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'
        

#Programa principal
line()
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))