#Desafio 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar no serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo de alistamento
# O programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import datetime
ano = int(input('Digite o seu ano de nascimento:'))
ano_atual = datetime.now().year
dif = ano_atual - ano
falta = 18 - dif
passou = dif -18
if dif == 18:
    print ('Está na hora de se alistar!')
elif dif < 18:
    print ('Você não precisa se alistar por agora ainda falta(m) {} ano(s)'. format(falta))
elif dif > 18:
    print ('Já passou {} anos do tempo de alistamento. Faça-o o mais rápido possível!!!!'. format(passou))
