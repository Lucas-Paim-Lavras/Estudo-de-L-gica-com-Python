#Desafio: leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça
#a digitação novamente até ter o valor correto.

s = str(input('Qual o seu sexo? [M/F]')) .upper() .strip() [0]    #esse [0] é pra pegar apenas a primeira letra.
while s not in 'MF':
    s = str(input('Dados inválidos, por favor informe o seu sexo!')) .upper() .strip() [0]
print (f'Sexo {s} registrado com sucesso.')