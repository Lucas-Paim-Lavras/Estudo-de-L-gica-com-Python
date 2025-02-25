#Desafio 065: Um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
#os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar

continuar = 'S'
soma = media = maior = menor = n = c = 0

while continuar == 'S':
    n = float(input('Digite um número: '))
    soma += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    media = soma/c

    #validação para aceitar apenas "S" e "N"
    while True:
        continuar = str(input('Quer continuar? [S/N] ')). upper(). strip()
        if continuar in ['S', 'N']:
            break
        print('Entrada Inválida! Digite apenas "S" ou "N"')
print (f'Você digitou {c} números e a média foi {media}')
print (f'O maior valor foi {maior} e o menor foi {menor}')

