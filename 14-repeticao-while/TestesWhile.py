#Teste 01:
for c in range (1, 10):
    print (c)
print ('Fim')     #Isso usando a estrutura de repetição for

#Teste 02: Usando o While quando eu sei o limite, posso usar o while ou o for. Se eu não sei o limite, precio usar o while
c = 1
while c < 10:
    print (c)
    c = c + 1
print('Fim')

#Teste 03: Quero fazer um programa que, quanddo eu digitar o valor '0' ele para
n = 1
while n != 0:   #Condição de parada
    n = int(input('Digite um valor:'))
print ('Fim')

#Teste 04: Posso colocar uma condição para que ele continue ou não.
resposta = 'S'                    #É preciso definir a variável antes de usar o While.
while resposta == 'S':
    n = int(input('Digite um valor: '))
    resposta = str(input('Quem continuar? [S/N]')). upper()
print ('Fim')

#Teste 05: um programa que leia números e diga, quantos são pares e quantos são ímpares.
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares.' )
