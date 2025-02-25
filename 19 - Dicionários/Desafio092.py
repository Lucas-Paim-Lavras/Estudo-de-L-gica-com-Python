#Desafio092: Um programa que leia nome, ano de nascimento e carteria de trabalho e cadastre-os (com idade)em um dicionário
#se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e a o salário.
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se apodentar.
from datetime import date

ano_atual = date.today().year
dados = {}

dados['Nome'] = str(input('Nome: '))
dados['Ano de nascimento'] = int(input('Ano de nascimento: '))

dados['Idade'] = ano_atual - dados['Ano de nascimento']
dados['CTPS'] = int(input('Carteira de trabalho (0 se não tiver): '))

if dados['CTPS'] != 0:
    dados['Ano'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    
    ano_aposentadoria = dados['Ano'] + 35
    idade_aposentadoria = ano_aposentadoria - dados['Ano de nascimento']
    dados['Aposentadoria'] = idade_aposentadoria

print('=-'*30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
