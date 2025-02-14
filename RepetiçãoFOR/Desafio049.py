#Desafio 049: refaça o desafio 009, monstrando a tabuada de um número que o usuário escolher, só que agora, utilizando um laço for.

n = int(input('Digite o número que você deseja a tabuada: '))
for t in range (0, 11):
    print (n*t)
    