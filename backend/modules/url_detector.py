# Importando bibliotecas necessárias

import os # permite que o python interaja com o sistema operacional
import base64 # permite que o python converta dados binários em texto
import requests # permite que o python faça requisições HTTP para o VirusTotal
from dotenv import load_dotenv # permite que o python carregue variáveis de ambiente

# Carregando variáveis de ambiente
load_dotenv()

# Criando função para analisar
def analisar_url(url):
    # obtendo a chave da API do VirusTotal do arquivo .env
    api_key = os.getenv("VIRUSTOTAL_API_KEY")

# a variavel api_key tem valor? se sim, imprime "API Key encontrada!", se não, imprime "API Key NÃO encontrada!"
    if api_key is not None:
        print("API Key encontrada!")
        print("Tamanho da API Key:", len(api_key))
    else:
        print("API Key NÃO encontrada!")

    # Convertendo a URL para o formato de ID utilizado pelo VirusTotal
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")

    # criando o cabeçalho da requisição com a chave da API
    headers = {
        "x-apikey": api_key
    }

    # enviando a requisição para o VirusTotal para obter informações sobre a URL
    requisicao = requests.get(
        f"https://www.virustotal.com/api/v3/urls/{url_id}",
        headers=headers
    )

    # verificando se a requisição foi bem sucedida, mostrando no terminal o status da requisição e o conteúdo retornado
    # se retorna status code 200 a requisição foi bem sucedida, se retorna 400 ou 500 a requisição falhou
    print(f"Status da requisição: {requisicao.status_code}")

    # atribuindo o conteúdo da resposta da requisição a uma variável dados, que é um dicionário com as informações da URL analisada
    dados = requisicao.json()

    # atribuindo as estatísticas da análise a uma variável estatisticas, que é um dicionário com as informações da análise da URL
    estatisticas = dados ["data"]["attributes"]["last_analysis_stats"]
    for chave, valor in estatisticas.items():
        print(f"\n{chave}: {valor}")

    

# testando a função analisar_url com uma URL de exemplo
resultado = analisar_url("https://www.youtube.com")  