#Desafio 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas
# a) A média de idade do grupo
# b) Qual é o nome do homem mais velho
# c) Quantas mulheres têm menos de 20 anos.

SomaIdade = 0
MediaIdade = 0
MaiorIdadeHomem = 0
NomeVelho = ''
totmulher20 = 0
for p in range (1, 5):
    print(f'----{p}ª Pessoa----')
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]?')). strip().upper()
    SomaIdade += idade
    if p == 1 and sexo == 'M':
        MaiorIdadeHomem = idade
        NomeVelho = nome
    if sexo == 'M' and idade > MaiorIdadeHomem:
        MaiorIdadeHomem = idade
        NomeVelho = nome
    if sexo == 'F' and idade < 20:
        totmulher20 += 1 
MediaIdade = SomaIdade/4
print(f'A média das idades é: {MediaIdade}')
print(f'O homem mais velho tem {MaiorIdadeHomem} e se chama {NomeVelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')