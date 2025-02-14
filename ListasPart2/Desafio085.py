#Desafio 085: Um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

temp = []
valor = []
pares = []
impares = []
for c in range(1, 8):
    temp.append(int(input(f'Digite o {c}º valor: ')))
    valor.append(temp[:])
    temp.clear()
    if c % 2 == 0:
        pares.append(c)
    elif c % 2 != 0:
        impares.append(c)
print('-='*30)
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}')
