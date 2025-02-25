#Desafio073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Mostre:
#A) Apenas os cinco primeiros colocados;
#B) Os últimos 4 colcoados da tabela;
#C) Uma lista com os times em ordem alfabética
#D) Em que posição na tabela está o time do cruzeiro.
print ('-='*40)
print('Vamos analisar a tabela do brasileirão de 2024'.center(80))
print ('-='*40)

times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco da Gama', 'Vitória', 'Atlético Mineiro', 'Fluminense', 'Grêmio', 'Red Bull Bragantino', 'Juventude', 'Athletico Paranaense', 'Criciúma', 'Atlético Goianiense', 'Cuiabá')
print (f'A lista de times é: {times}')

#Resposta da letra A:
print ('-='*40)
print (f'Os cinco primeiros times são {times[0:5]}')

#Resposta da letra B:
print ('-='*40)
print (f'Os últimos colocados da tabela são {times[16:]}')

#Resposta da letra C:
print ('-='*40)
print (f'Os times em ordem alfabétca fica {sorted(times)}')

#Respsta da letra D:
print ('-='*40)
cruzeiro = times.index('Cruzeiro')
print (f'O cruzerio está na {cruzeiro}ª posição.')