#Desafio 098: um programa que receba três parâmetros: início, fim e passo e realize a contagem. Seu programa tem que
#realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1.
# b) De 10 até 0, de 2 em 2.
# c) Uma contagem personalizada.

from time import sleep

def linha():
    print('-='*30)

def contador1():
    linha()
    print('Contagem de 1 até 10 de 1 em 1: ')
    for c in range (1, 11):
        print(f'{c} ', end= ' ', flush = True)  # O método flush() mantém os números na mesma linha
        sleep(0.1)
    print ('FIM')

def contador2():
    linha()
    print('Contagem de 10 até 0 de 2 em 2: ')
    for c in range (10, -1, -2):
        print(f'{c} ', end= ' ', flush = True)
        sleep(0.1)
    print ('FIM')   

def personalizado(inicio, fim, passo):
    linha()
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if passo == 0:
        passo = 1 if inicio < fim else -1
    
    if inicio < fim:
        for c in range (inicio, fim + 1, abs(passo)):  # Usa abs() para garantir passo positivo na contagem crescente
            print(f'{c} ', end='', flush=True)
            sleep(0.3)
    else:
        for c in range (inicio, fim - 1, -abs(passo)):  # Usa -abs() para garantir passo negativo na contagem decrescente
            print(f'{c} ', end='', flush=True)
            sleep(0.3)

    print ('FIM')  

#Contadores normais:
contador1()
contador2()

#Personalizado:
linha()
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
personalizado(inicio, fim, passo)