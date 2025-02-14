#Desafio 022: Leia o nome comleto de uma pessoa e mostre: O nome com todas as letras maiúsculas; todas minúsculas; Quantas letras ao todo(sem considerar espaços); quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo:'))
print (nome.upper())
print (nome.lower())
num_caract = len(nome.replace(' ', '')) #aqui ele tá trocando espaço ' ' por ''. Ou seja, trocando espaço pr nada.
print ('O número de cacteres do nome, sem considerar os espaços, é: {}'. format(num_caract))
dividido = nome.split()
num1_caract = len(dividido[0])
print ('O número de cacteres do primeiro nome é: {}'. format(num1_caract))

#Desafio 023: Um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#exemplo: Digite um número: 1834 / Unidade: 4 / Dezena: 3 / Centena: 8 / Milhar: 1
while True:
    try:
        numero = input('Digite um número entre 0 e 9999:')
        if numero.isdigit() and 0 <= int(numero) <= 9999:
            numero_formatado = numero.zfill(4) #Esse comando zfill é pra preencher em digitos o número em 4
            unidade = numero_formatado[3]
            dezena = numero_formatado[2]
            centena = numero_formatado[1]
            milhar = numero_formatado[0]
            print('Unidade: {}'. format(unidade))
            print('Dezena: {}'. format(dezena))
            print('Centena: {}'. format(centena))
            print('Milhar: {}'. format(milhar))
            break
        else:
            print('O número deve estar entre 0 e 9999. Tente novamente')
    except ValueError:
        print('Entrada inválida. Por favor, digite um número inteiro.')


#Desafio 024: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'
cidade = str(input('Digite o nome de uma cidade:')). strip()
print(cidade[:5] == 'Santo')     #Eu usei até o 5 porque, começa em 0 e termina em 4 e a gente passa pra pegar o último caractere

#Desafio 025: Um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome
# nome = str(input('Digite seu nome:')). strip()
# print ('Seu nome tem Silva? {}'. format('SILVA' in nome.upper))

#Desafio 026: Um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra 'A'
#Em que posição ela aparece pela primeira vez.
#Em que posição ela aparece a última vez
frase = str(input('Escreva uma frase:')). strip(). upper()
print ('Nessa frase a letra "A", maiúcula aparece: {}'. format (frase.count('A')))
print ('Nessa frase, a posição que a letra "A", maúiscula, aparece pela primeira vez é: {}' . format (frase.find('A')+1))
print ('Nessa frase, a posição que a letra "A", maiúscula, aparece pela última vez é: {}' . format (frase.rfind('A')+1))

#Desafio 027: Um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
nome = str(input('Digite seu nome completo:')). strip()
dividido = nome.split()
print ('Primeiro nome: {}'. format (dividido[0]))
print ('Último nome: {}'. format (dividido[-1]))     #O item -1 retorna ao último elemento da lista