#Desafio 036:
#Um programa de aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo vai ser negado.
casa = float(input('Digite o valor da casa que você deseja comprar com o empréstimo em R$'))
salario = float(input('Digite o valor do seu salário em R$'))
anos = int(input('Em quantos anos você vai pagar o imóvel?'))
prestação = casa / (12*anos)
if prestação > (0.3*salario):
    print ('O valor da prestação é superior a 30 por cento do seu salário e tem valor {}. Logo, o empréstimo não pode ser realizado.'. format(prestação))
elif prestação <= (0.3*salario):
    print ('Seu empréstimo foi aprovado. O valor da prestação mensal será {}'. format(prestação))