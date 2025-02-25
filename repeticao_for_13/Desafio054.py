#Desafio 054: Leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import datetime
atual = datetime.now().year
totmaior = 0
totmenor = 0

for pessoa in range (1, 8):
    while True:
        try:
            nascimento = int(input(f'Em que ano a {pessoa}ª pessoa nasceu?'))
            if 1900 <= nascimento <= atual:
                break
            else:
                print(f'Por favor, digite um ano entre 1900 e {atual}.')
        except ValueError:
            print('Entrada inválida! Por favor digite um ano válido (apenas números).')
    
    idade = atual - nascimento
    if idade >= 18:
        print('Essa pessoa é maior de idade.')
        totmaior += 1
    else:
        print('Essa pessoa é menor de idade')
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'E também tivemos {totmenor} pessoas menores de idade')
