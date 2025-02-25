#Leia dois valores e mostre um menu na tela:
#[1] Somar ; [2] Multiplicar ; [3] Maior ; [4] Novos números ; [5] Sair do programa
#O programa deverá realizar a operação solicitada em cada caso.

print ('Olá pessoal! Eu sou o \033[1;36mSMM\033[m. \033[1;36mS\033[momo, \033[1;36mM\033[mutiplico ou digo qual o \033[1;36mM\033[maior valor Digite dois valores!')
n1 = float(input('Valor 1: '))
n2 = float(input('Valor 2: '))
while True:
    option = int(input('''O que você deseja fazer?
                   [1] Somar
                   [2] Multiplicar
                   [3] Maior
                   [4] Novos números
                   [5] Sair do programa
                   Digite uma opção: '''))
    while option < 1 or option > 5:
        option = int(input('Entrada inválida, digite um valor entre 1 e 5: '))
    if option == 1:
        print (f'A soma de {n1} com {n2} é {n1+n2}.')
    elif option == 2:
        print (f'A multiplicação de {n1} com {n2} é {n1*n2}.')
    elif option == 3:
        if n1 > n2:
            print(f'O {n1} é maior!')
        elif n2 > n1:
            print(f'O {n2} é maior!')
        else:
            print('Não existe valor maior, os dois são iguais!')
    elif option == 4:
            print ('Ok! Digite outros valores!')
            n1 = float(input('Valor 1: '))
            n2 = float(input('Valor 2: '))
    elif option == 5:
        print ('Ok, Ok ... Já estou saindo :( ... \033[1;36mSMM\033[m Câmbio, Desligo.)')
        break