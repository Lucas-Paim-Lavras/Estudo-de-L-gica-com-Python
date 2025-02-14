#exemplo
tempo = float(input('Quanto tempo tem o seu carro?'))
print('carro novo' if tempo <= 3 else 'carro velho')

#Teste
nome = str(input('Qual é seu nome?')). strip()
if 'Lucas' == nome:
    print('Que nome lindo você tem!!', 'Bom dia {}'.format(nome))
else:
    print('Seu nome é feio ...')
print('Bom dia, {}'.format (nome))

#problema clássico
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
n = (n1+n2)/2
print('A sua média doi {:.2f}'. format(n))
if n >= 7:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruim! Estude mais')
    