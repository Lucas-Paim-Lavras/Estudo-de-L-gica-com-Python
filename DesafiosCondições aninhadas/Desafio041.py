#Desafio 041: leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - entre 4 e 9 anos: MIRIM
# - entre 10 e 14 anos: INFANTIL
# - entre 14 e 19 anos: JUNIOR
# - 20 anos: SÊNIOR
# - Acima de 20 anos: MASTER
from datetime import datetime
nascimento = int(input('Qual o ano do seu nascimento?'))
ano_atual = datetime.now().year
idade = ano_atual - nascimento
if idade <= 9:
    print ('Sua categoria é MIRIM.')
elif 9 < idade <= 14:
    print ('Sua categoria é INFANTIL.')
elif 14 < idade <= 19:
    print ('Sua categoria é JUNIOR.')
elif 19 < idade <= 20:
    print ('Sua categoria é SÊNIOR.')
elif 20 > idade > 110:
    print ('Sua categoria é MASTER.')
else:
    print('Entrada inválida ... é difícil alguém viver tanto tempo assim e participar de um campeonato de natação ;)')
