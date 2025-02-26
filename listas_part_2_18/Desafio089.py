#Desafio 089: Leia o nome e duas notas de varios alunos e guarde tudo em uma lista composta. No final
#mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
import statistics
ficha = []
while True:
    nome = str(input('Nome: ')).strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome,[nota1, nota2], media])
    continuar = str(input('Quer continuar? [S/N]'))
    if continuar in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    option = int(input('Mostrar notas de qual aluno: (999 interrompe)'))
    if option == 999:
        print('FINALIZANDO ...')
        break
    if option <= len(ficha)-1:
        print(f'Notas de {ficha[option][0]} são {ficha[option][1]}')
print('<<<< VOLTE SEMPRE! ')