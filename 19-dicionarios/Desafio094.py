#Desafio 094: Unindo discionários e listas

dados = {'nomes':[], 
         'sexos':[],
         'idades':[],
         'mulheres':[],
         'MaiorMedia':[]
         }
c = 0

while True:
    nome = str(input('Nome: '))
    dados['nomes'].append(nome)
    
    while True:
        sexo = str(input('Sexo [M/F]: ')) .strip().upper()[0]
        if sexo in ['M', 'F', 'm', 'f', 'Masculino', 'Feminino']:
            dados['sexos'].append(sexo)
            if sexo in ['F', 'f', 'Feminino']:
                dados['mulheres'].append(nome)
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    
    idade = int(input('Idade: '))
    dados['idades'].append(idade)
    
    while True:
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0].capitalize()
        c += 1
        if continuar in ['Sim', 'Não', 'S', 'N', 'n', 's']:
            break
        print('Entrada Inválida. Digite apenas [Sim/Não] ou [S/N]')
    if continuar in ['N', 'Não', 'n']:
        break

#Exibir os dados
print('-='*30)
print(dados)

#Calcular e exibir a média de idade
print(f'  A) Ao todo temos {c} pessoas cadastradas.')
media = sum(dados['idades'])/c
print(f'  B) A média de idade é de {media:.2f} anos.')

#Listar as mulheres cadastradas
print(f'  C) As mulheres cadastradas foram {", ".join(dados["mulheres"]) if dados["mulheres"] else "Nenhuma"}')

#Listar pessoas com idade acima da média
print('  D) Lista de pessoas com idade acima da média:')
for i in range(len(dados['nomes'])):
    if dados['idades'][i] > media:
        print(f'    Nome = {dados["nomes"][i]}; Sexo = {dados["sexos"][i]}; Idade = {dados["idades"][i]}')

print('<< ENCERRADO >>')