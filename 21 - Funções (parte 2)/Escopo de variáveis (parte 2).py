def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')

# Programa Principal
n1 = 2
funcao()
print(f'N1 global vale {n1}')


def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
a = 5
teste(a)
print(f'A fora vale {a}')

