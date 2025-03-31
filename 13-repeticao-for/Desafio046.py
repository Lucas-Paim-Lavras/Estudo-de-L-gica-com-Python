#Um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifícios, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
from emoji import emojize
import pygame

#Inicializando o mixer do pygame
pygame.mixer.init()

#Carregando o som de fogos de artifício
pygame.mixer.music.load('/home/youx/Downloads/fogos.mp3')

print (emojize('Vamos fazer a contagem regressiva para o ano de 2025???? :star-struck:'))

#Contagem regressiva
for c in range (10, -1, -1):
    print(f'\033[35m{c}\033[m')
    sleep(1)

#Mensagem de Feliz Ano Novo
print (emojize(':star::star::star:FELIZ ANO NOVO!!!:fireworks: :sparkler: '))

#Reproduzir som de fogos
pygame.mixer.music.play()

# Esperar até o som terminar para não fechar o programa imediatamente
while pygame.mixer.music.get_busy():
    sleep (1)