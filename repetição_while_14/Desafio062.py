#Supre PA v3.0
primeiro = float(input('Qual o primeiro termo da PA? '))
razao = float(input('Qual a razão da PA? '))
termos = primeiro
soma = 0
c = 1
total = 0
mostrados = 10
while mostrados != 0:
    total += mostrados
    while c <= total:
        print (f'{termos} -> ', end= '')
        termos = termos + razao
        c += 1
    print ('PAUSA')
    soma = total
    mostrados = int(input('Quantos termos você quer mostrar a mais?'))
print (f'Progressão Finalizada com {soma} termos mostrados.')