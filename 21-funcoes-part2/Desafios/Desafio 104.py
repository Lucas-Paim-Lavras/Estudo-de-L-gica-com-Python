#Desafio 104: Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do python, só que fazendo a validação para aceitar apenas um valor numérico.
# n = leiaint('Digite um n')

#Minha solução
def leiaInt(msg):
    while True:
        n = input(msg)
        if n.lstrip('-').isdigit():
            return int(n)
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido!\033[m')


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')






#Guanabara
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.lstrip().isnumeric():
            valor = int(n)      #transformo o n em um número inteiro
            ok = True
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido!\033[m')
        if ok:
            break
    return valor


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
