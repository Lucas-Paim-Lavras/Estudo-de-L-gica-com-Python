def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

# Programa principal
n = 2
print(f'No programa principal, n vale {n}')    #n é uma variável global pois é definida no programa principal. Vale, tanto pra função quanto pra fora dela
teste()
print(f'No programa principal, x vale {x}')     #Como x é uma variável local da função teste, ela não é definida fora dela



