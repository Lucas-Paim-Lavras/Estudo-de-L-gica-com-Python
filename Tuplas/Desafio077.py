#Desafio 077: Tenha uma tupla com várias palavras (Não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.

palavras = ('Casa', 'Carro', 'Relogio', 'Arvore', 'Computador', 'Gato', 'Cachorro', 'Livros', 'Praia', 'Montanha', 'Escola', 'Telefone', 'Viagem', 'Cidade', 'Estrada')
vogais = ('a', 'e', 'i', 'o', 'u')
for i in range (0, len(palavras)):        #Usou laço
    print(f'\nNa palavra {palavras[i]} temos', end=' ')
    for letra in palavras[i]:                   #Usou laço
        if letra.lower() in vogais:            #Usou uma estrura condicional
            print(letra, end=' ')

    