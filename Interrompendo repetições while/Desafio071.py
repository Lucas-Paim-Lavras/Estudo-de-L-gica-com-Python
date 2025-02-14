#Desafio071: Simulador de caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número Inteiro)
#e o programa vau informar quantas células de cada valor serão entregues.
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('='*30)
print('BANCO PAIM'.center(25))
print('='*30)
valor = int(input('Que valor você quer sacar? '))
total = valor
cedula = 50
totced = 0

#Começo com a variável 50 que, é a minha maior nota e vou subtraindo do valor.

while True:
    
    if total >= cedula:
        total -= cedula
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totced = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO PAIM! Tenha um bom dia!')
