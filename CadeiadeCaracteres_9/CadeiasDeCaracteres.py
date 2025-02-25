frase = 'Curso em Vídeo Python'

#fatiamento
frase[9]        #pego uma letra dizendo o nome da minha variável e entre colchetes o índice da letra
frase[9:13]     #é do caracter 9 até o 13, porém, o 13 eu não pego
frase[9:21]     #ele fatia até a última letra
frase[9:21:2]   #pulando de dois e dois
frase[:5]       #mesma coisa de escrever frase[0:5] igual na calculadora científica
frase[15:]      #mesma coisa do anterior, mas vai até  final nesse caso.
frase[9::3]     #começa em nove, vai até o final pulando de 3 em 3.

#Análise: Saber informações de uma str
len(frase)       #Qual o comprimento da frase, no nosso caso, tem 21 caracteres
frase.count('o') #Quantas vezes a letra 'o' minúscula aparece
frase.count('0, 0, 13')    #Contagem de 'o' já com o fatiamento do 0 ao 13 (não conta o 13)
frase.find('deo')     #ele vai dizer onde começa o 'deo'
frase.find('Android')   #ele vai retornar de resposta com -1, isso vai significa que não foi encontrada
'Curso' in frase      #Existe curso em frase? é um operador isso aqui

#Transformação
frase.replace('python', 'Android')      #Ele vai trocar a palavra python por Android
frase.upper()         #Transforma as letras em maiusculas e mantém as maiúsculas
frase.lower()         #mantém o que tá minúsculo e torna as maiúsuclas em minúsculas
frase.capitalize()    #Apenas o primeiro caractere ficará maiúsculo
frase.title()         #analisa quantas palavras tem a frase e torna maiúsculo todas as primeiras letras
frase.strip()         #remove todos os espaços inúteis que não estejam dentro da frase
frase.rstrip()        #remove todos os espaços inúteis da direita
frase.lstrip()        #remove todos os espaços inúteis da esquerda

#Divisão: consigo dividir str's
frase.split()        #dividi em espaços as palavras de acordo com os espaços em uma lista de palavras que podemos usar isso depois
'-'.join(frase)      #junto as frases usando como separador - com uma STR única

