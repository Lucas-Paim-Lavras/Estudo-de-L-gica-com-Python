#Desafio 053: Leia uma frase e diga se ela é um palíndromo, desconsiderando espaços
print ('\033[1;31mBem vindo ao nosso verificador de palíndromos!!!\033[m')
frase = str(input('Digite uma frase: ')) .strip().upper()
junto = frase.replace(' ', '')
if junto == junto [::-1]:
    print (f'É um palíndrono, pois {junto} é igual a {junto[::-1]}')
else:
    print (f'Não é um palíndrono, pois {junto} é diferente de {junto[::-1]}')
