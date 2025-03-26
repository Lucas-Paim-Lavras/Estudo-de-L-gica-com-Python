#Desafio 019: Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Um programa que leia os nomes deles e sorteie o nome de um deles.
import random
a1 = str(input('Digite o nome do aluno 1:'))
a2 = str(input('Digite o nome do aluno 2:'))
a3 = str(input('Digite o nome do aluno 3:'))
a4 = str(input('Digite o nome do aluno 4:'))
s = random.choice([a1, a2, a3, a4])
print (f'O aluno sorteado é {s}')