#Desafio 022: Leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas; todas minúsculas; Quantas letras ao todo(sem considerar espaços); quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo:'))
print (nome.upper())
print (nome.lower())
num_caract = len(nome.replace(' ', '')) #aqui ele tá trocando espaço ' ' por ''. Ou seja, trocando espaço pra nada.
print ('O número de caracteres do nome, sem considerar os espaços, é: {}'. format(num_caract))
dividido = nome.split()
num1_caract = len(dividido[0])
print ('O número de cacteres do primeiro nome é: {}'. format(num1_caract))