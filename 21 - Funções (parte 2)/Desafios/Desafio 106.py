# Desafio 106: faça um mini sistema  que utilize o interactive help do python. O usuário vai digitar o comando
# e o manual vai aparecer. Quando o usuário digitar 'FIM', o programa se encerrará.
from time import sleep

c= ('\033[m',        # 0 - Sem cores
    '\033[0;30;41m', # 1 - vermelho
    '\033[0;30;42m', # 2 - verde
    '\033[0;30;43m', # 3 - amarelo
    '\033[0;30;44m', # 4 - azul
    '\033[0;30;45m', # 5 - roxo
    '\033[7;30m'     # 6 - branco
   )

def ajuda(com):
    """
    -> Sistema interativo de ajuda do Python.
    O usuário pode digitar um comando ou biblioteca para obter a documentação.
    Digite 'FIM' para encerrar o programa.
    """
    titulo(f'Acessando o manual do comando '{com}'', 4)
    print(c[6],end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg)
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0], end='')
    sleep(1)

# Programa Principal
comando = ''
while True:
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)