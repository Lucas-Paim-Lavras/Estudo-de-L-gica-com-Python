#Desafio075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#Quantas vezes apareceu o valor 9.
#Em que posição foi digitado o primeiro valor 3.
#Quais foram os números pares.
c = 0
par = ()
tupla = ()
while c <= 3:
    c += 1
    numero = int(input('Digite um valor: '))
    tupla += (numero,)
    if numero % 2 == 0:
        par += (numero,)

#Quantas vezes o número 9 apareceu?
print (f'O número 9 aparece {tupla.count(9)} vezes. ')

#EM que posição foi digitado o primeiro valor 3.
if numero != 3:
    print('Não há número 3 na sequência.')
else:
    print(f'O número 3 aparece, pela primeira vez, na {tupla.index(3)+ 1}ª posição.')

#Quais foram os números pares.
print(f'Os valores pares digitados foi(oram): {par}')