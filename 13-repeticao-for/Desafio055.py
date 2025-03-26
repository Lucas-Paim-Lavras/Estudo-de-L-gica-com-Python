#Desafio 055: Leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menos peso lidos.

maior = None
menor = None

for pessoa in range (1,6):
    peso = float(input(f'Qual o peso da {pessoa}ª pessoa?'))
    if maior is None or peso > maior:
        maior = peso
        maior_pessoa = pessoa
    if menor is None or peso < menor:
        menor = peso
        menor_pessoa = pessoa

print(f'O maior peso é da {maior_pessoa}ª com valor igual a {maior}')
print(f'O menor peso é da {menor_pessoa}ª com valor igual a {menor}')