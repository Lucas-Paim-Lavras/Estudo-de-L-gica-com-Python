#Solicita um valor ao usuário
n = input(str('Digite algo:'))

#Exibe o tipo primitivo digitado pelo usuário
print('O tipo primitivo é', type(n))

#Identifica o que é o valor digitado pelo usuário
print ('É um número?', n.isnumeric())
print ('É uma letra?', n.isalpha())
print ('Só espaços?', n.isspace())
print ('Letras minúculas?', n.islower())
print ('Pode ser impresso?', n.isprintable())
print ('Letras MAIÚSCULAS?', n.isupper())
print ('É uma letra?', n.isascii())
print ('É uma letra?', n.istitle())