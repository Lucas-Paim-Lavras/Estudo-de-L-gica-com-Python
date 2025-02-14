#Desafio069: leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:
#Quantas pessoas tem mais de 18 anos.
#Quantos homens foram cadastrados
#Quantas mulheres tem menos de 20 anos.
totmaior = 0
totmenor = 0
CountMan = 0
CountWomanMenos = 0

#Estrutura de laço de repetição para cadastrar os dados.
while True:
    idade = int(input('Qual a sua idade? '))
       
    #fazer com que o usuário responda corretamente o sexo.
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o seu sexo? [M/F]')) .strip().upper()[0]
    
    #Contar a quantidade de homens
    if sexo == 'M':
        CountMan += 1
    elif sexo == 'F' and idade < 20:
        CountWomanMenos += 1
    
    #Conta a quantidade de pessoas maiores de 18 anos
    if idade > 18:
        totmaior += 1
    else:
        totmenor += 1
    
    #Critério de parada do while True
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar o cadastramento? [S/N]')) .strip().upper()[0]
    if continuar == 'N':
        print('Obrigado!Segue a análise de dados.')
        break

print(f'Há {totmaior} pessoas com idade maior que 18 anos e {totmenor} pessoas com idade menor que 18 anos. ')
print (f'Há {CountMan} homem(ns).')
print (f'Há {CountWomanMenos} mulher(es) com menos de 20 anos.')
