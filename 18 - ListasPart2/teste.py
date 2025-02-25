#Teste 01:
teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])   #copia para não fazer uma ligação entre as listas e copiar na primeira e na segunda, a mesma coisa
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

#Teste 02:
galera = [['João', 40], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print (galera[2][1])

#Teste 03:
galera = [['João', 40], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')

#Teste 04:
galera = list()
dado = list()
totmaior = totmenor = 0

#Pega os dados de nome e idade:
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])               #Não esquecer o símbolo da cópia '[:]'
    dado.clear()

#Analisa os dados:
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade;')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')

