#Desafio 043: Leia o peso e a altura de uma pessoa, calcule seu IMC e mostre o seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obsedidade mórbida
from math import pow
peso = float(input('Qual o seu peso em quilogramas: ')) 
altura = float(input('Qual a sua altura em metros: '))
imc = peso/(pow(altura, 2))
if imc < 18.5:
    print ('Seu IMC deu {:.2f}, logo você está ABAIXO DO PESO. Procure uma ou um especialista!'. format(imc))
elif 18.5 <= imc <= 25:
    print ('Seu IMC deu {:.2f}, logo você está no PESO IDEAL. Continue!!'. format (imc))
elif 25 < imc <= 30:
    print ('Seu IMC deu {:.2f}, logo você está com SOBREPESO. Procure uma ou um especialista!'. format(imc))
elif 30 < imc <= 40:
    print ('Seu IMC deu {:.2f}, logo você está com obesidade. Procure uma ou um especialista!'. format(imc))
elif imc > 40:
    print ('Seu IMC deu {:.2f}, logo você está com obesidade mórbida. Procure uma ou um especialista!'. format(imc))
else:
    print ('Entrada Inválida. Verifique os dados')