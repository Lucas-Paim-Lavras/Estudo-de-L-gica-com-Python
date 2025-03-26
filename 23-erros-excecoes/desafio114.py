#Crie um código em python que teste se o site Pudim está acessível pelo computador usado.

import requests

def verifica_acessibilidade_site(url):
    try:
        resposta = requests.get(url, timeout=5)

        if resposta.status_code == 200:
            print(f'O site {url} está acessível!')
        else:
            print(f'\033[1:31mO site {url} retornou o status code: {resposta.status_code}\033[m')
    
    except requests.exceptions.RequestException as erro:
        print(f'Não foi possível acessar o site {url}')


url = 'https://www.pudim.com.br/'

verifica_acessibilidade_site(url)

    
