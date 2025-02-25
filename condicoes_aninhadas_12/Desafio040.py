#Desafio 040: Leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
n1 = float(input('Digite a nota de Ciências:'))
n2 = float(input('Digite a nota de Matemática:'))
media = (n1+n2)/2
if media < 5:
    print ('Aluno \033[1;30;41mREPROVADO\033[m')
elif 5 <= media <= 6.9:
    print ('Aluno \033[1;31mRECUPERAÇÃO\033[m')
elif 7.0 <= media <= 10.0:
    print ('Aluno \033[1;32mAPROVADO\033[m')
else:
    print('Entrada inválida. As notas devem estar entre 0 e 10. Tente novamente!')
