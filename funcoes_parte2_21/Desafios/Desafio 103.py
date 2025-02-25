#Desafio 103: Um programa que tenha a função ficha(), que receba dois parâmetros opcionais: o nome de um
# jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum
# dado não tenha sido informado corretamente

def linha():
    print('-'*40)

def ficha():
    linha()
    nome = str(input('Nome do Jogador: ')).strip()
    gols = str(input('Número de gols: ')).strip()
    if nome == '':
        nome = '<desconhecido>'
    if gols.isnumeric() == False:   
        gols = 0
    else:
        gols = int(gols)
    
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')

ficha()