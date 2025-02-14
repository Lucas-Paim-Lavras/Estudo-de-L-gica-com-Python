#Teste 1: funcionalidades
pessoas = {'nome': 'Lucas', 'sexo': 'M', 'idade':24}
del pessoas['sexo'] #Deletei
pessoas['nome'] = 'Leandro'  #Modifiquei
pessoas['peso'] = 88.5    #adicionei, sem usar o append.()
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for k, v in pessoas.items():     # não tem o enumerate, daí, a gente usa o items
    print(f'{k} = {v}')

#Teste 2: Adicionar um dicionário dentro de uma lista
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf':'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])
print(brasil[1]['sigla'])

#Teste 3:
estado = {}
brasil = []
for c in range(0, 3):
    estado['unidade federativa'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())     #método de copiar de dicionários (SUPER ÚTIL)
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()