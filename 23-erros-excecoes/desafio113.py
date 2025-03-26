# Desafio 113: Reescreva a fun~]ao leiaint() do desafio 104, incluindo agora a possibilidade da digitação de 
# um número de tipo inválido. Aproveite e crie també uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31m\nUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mErro: por favor, digite um número real válido!')
            continue
        except KeyboardInterrupt:
            print('\033[1;31m\nUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

# Programa Principal

num = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real: ')

print(f'O valor inteiro digitado foi {num} e o real foi {r}')



    