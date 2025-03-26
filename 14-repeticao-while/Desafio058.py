#Melhore o jogo do desafio 028 onde o pc vai 'pensar' em um número de 0 a 10. Só que agora o jogardor vai tentar
#adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
tentativas = 1
plural ='s'
ThinkNum = random.randint (0, 10)
n = int(input('Tente adivinhar: Qual o número que eu estou "pensando" entre 0 e 10 '))
while n != ThinkNum:
    tentativas += 1           #incremento as tentativas, mesmo que esteja certo ou errado.
    n = int(input('Você errou! Digite outro número: '))
tentativas += 1

if tentativas > 1:
    plural = plural
print (f'Yeah! Você acertou e precisou de {tentativas} tentativa{plural} para isso!')
