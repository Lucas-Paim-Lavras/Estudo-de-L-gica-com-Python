#Desafio 105: Um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um discionário com as seguintes
# informações: 
#Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)
# Adicione também as docstrings da função.

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita múltiplos valores)
    :param sit: (opcional) indica se deve ou não adicionar a situação da turma
    :return: um dicionário com as informações da análise
    """
    resultado = {
        'total':len(n),
        'maior':max(n),
        'menor':min(n),
        'media':sum(n) / len(n)
    }
    if sit:
        if resultado['media'] >= 7.0:
            resultado['sit'] = 'BOA'
        elif resultado ['media'] >= 5:
            resultado['sit'] = 'RAZOÁVEL'
        elif resultado['media'] < 5:
            resultado['sit'] = 'RUIM'
    
    return resultado

#Programa principal
resp = notas(5.5, 4.5, 6.5, sit=True)
print(f'\nSegue o relatório das notas \n \n{resp}\n')
