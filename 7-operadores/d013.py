#Desafio 013: Leia o salário de um funcionário, e print com 15 por cento de aumento.

n = float(input('O seu salário, sem aumento é?'))
a = n*(1.15)
print ('O seu novo salário, com o aumento, será? {:.2f}'. format(a))