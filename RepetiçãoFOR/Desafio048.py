#Desafio 048: Calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram 
# no intervalo de 1 até 500.
s = 0
for c in range (1, 501):
    if c % 2 != 0 and c % 3 == 0:
        print (c)
        s = s + c
print ('Somatório de todos os números que são múltiplos de três, ímpares e que estão entre 1 e 500 são {}'. format(s))
