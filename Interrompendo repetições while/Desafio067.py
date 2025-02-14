#Desafio 067: Mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa
#será interrompido quando o número solicitado por negativo.
resultado = 0
while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    if valor < 0:
        break
    print ('~'*50)
    for i in range (1, 11):
        resultado = valor*i
        print (f' {valor} x {i} = {resultado} ')
    print ('~'*50)
print ('PROGRAMA TABUADA ENCERRADO!')