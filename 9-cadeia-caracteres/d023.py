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