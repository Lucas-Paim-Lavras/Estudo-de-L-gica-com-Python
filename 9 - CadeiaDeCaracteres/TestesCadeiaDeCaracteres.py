#teste 01
frase = 'Curso em Vídeo Python'
print (frase)

#teste 02
frase = 'Curso em Vídeo Python'
print (frase[3:13])

#teste 03
frase = 'Curso em Vídeo Python'
print (frase[:15])

#teste 04
frase = 'Curso em Vídeo Python'
print (frase[3:])

#teste 05
frase = 'Curso em Vídeo Python'
print (frase[3:15:3])

#teste 06
frase = 'Curso em Vídeo Python'
print (frase[::2])

#teste 07: uso de três aspas para textos longos
print("""Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().
Gostou da aula? Então torne-se um Gafanhoto APOIADOR do CursoemVídeo acessando o site cursoemvideo.com/apoie
Aula do Curso de Python criado pelo professor Gustavo Guanabara para o portal CursoemVideo.com.""")

#teste 08
frase = 'Curso em Vídeo Python'
print (frase.count('o'))

#teste 09
frase = 'Curso em Vídeo Python'
print(frase.count ('O'))

#teste 10
frase = 'Curso em Vídeo Python'
print(frase.upper().count ('O'))     #contar a quantidade de O's jogada pra ser maiúscula

#teste 11
frase = 'Curso em Vídeo Python'
print (len(frase))

#teste 12
frase = '   Curso em Vídeo Python'
print (len(frase))

#teste 13
frase = '    Curso em Vídeo Python'
print (len(frase.strip()))

#teste 14
frase = 'Curso em Vídeo Python'
print (frase.replace('Python', 'Android'))
print (frase)         #uma str é imutável

#teste 15
frase = 'Curso em Vídeo Python'
frase = frase.replace ('Python', 'Android')    #aqui eu mudei a minha variável
print (frase)

#teste 16
frase = 'Curso em Vídeo Python'
print ('Curso' in frase)

#teste 17
frase = 'Curso em Vídeo Python'
print(frase.find('Curso'))     #vai mostrar onde é a posição incial da palavra curso

#teste 18
frase = 'Curso em Vídeo Python'
print (frase.find('vídeo'))    #vai mostrar -1, dizendo que não encontrou

#teste 19
frase = 'Curso em vídeo Python'
print (frase.lower().find ('vídeo'))

#teste 20
frase = 'Curso em vídeo Python'
print (frase.split())              #separa em palavras, como em uma lista

#teste 21
frase = 'Curso em vídeo Python'
dividido = frase.split ()
print(dividido[0])               #mostra apenas o primeiro elemento da lista 

#teste 22
frase = 'Curso em vídeo Python'
dividido = frase.split()
print(dividido[0][3])             #mostra apenas uma letra da variável dividido


