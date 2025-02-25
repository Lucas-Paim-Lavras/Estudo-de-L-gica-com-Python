#Desafio 061: Refazer o desafio 051, lendo  primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão isando while
primeiro = float(input('Qual o primeiro termo da PA? '))
razao = float(input('Qual a razão da PA? '))
termos = primeiro
c = 1
while c <= 10:
    print (f'{termos} -> ', end= '')
    termos =+ termos + razao
    c += 1
print ('FIM')