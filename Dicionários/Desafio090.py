#Desafio 090: leia nome e média de um aluno, guardando também a situação em um dicionário. No final mostre o conteúdo da estrutura na tela.

aluno = {}

aluno ['nome'] = str(input('Nome: '))
aluno ['media'] = float(input(f'Média de {aluno["nome"]}: '))
print(f'Nome é igual a {aluno["nome"]}.')
print(f'Média é igual a {aluno["media"]}')
if aluno['media'] < 6:
    print(f'Situação é igual a Reprovado!')
else:
    print(f'Situação é igual a Aprovado!')