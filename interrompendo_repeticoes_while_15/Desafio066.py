#Desafio 066: leia vários números inteiros. O programa só vai parar quando o usuário digitar o valor 999, que é a
#condição de parada. No final, mostre quantos números foram digitadose qual foi a soma entre eles. (desconsiderando o 999)

n = soma = c = 0
while True:
    n = float(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    soma = soma + n
    c += 1
print (f'Você digitou {c} números e a soma entre eles é {soma}')
print ('FIM')