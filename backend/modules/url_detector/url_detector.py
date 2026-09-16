# Importando bibliotecas necessárias

import os # permite que o python interaja com o sistema operacional
import base64 # permite que o python converta dados binários em texto
import requests # permite que o python faça requisições HTTP para o VirusTotal
import time # trabalha com tempo e espera.

from dotenv import load_dotenv # permite que o python carregue variáveis de ambiente
from queue import Queue # cria filas 
from threading import Thread # permite executar o processador da fila em segundo plano, sem travar o restante do sistema.


# Carregando variáveis de ambiente
load_dotenv()

# Cria a fila que vai armazenar as URLs
# que aguardam para serem analisadas.
fila_urls = Queue()
INTERVALO_REQUISICAO = 15 # Tempo mínimo entre as requisições ao VirusTotal.

#função para enviar URL para a fila
def adicionar_fila(url):

    # cria fila exclusiva para guardar o resultado desta url
    fila_resultado = Queue()

    # coloca na fila principal 
    # a url + a fila onde o resultado devera ser colocado
    fila_urls.put((url, fila_resultado))

    # aguarda o resultado da anlise
    resultado = fila_resultado.get()

    # retorna o resultado para quem chamou a função
    return resultado


# criando função para processar a fila
def processar_fila():

    while True:

        # Pega a próxima tarefa da fila.
        # A tarefa contém a URL e a fila específica
        # onde o resultado deverá ser colocado.
        url, fila_resultado = fila_urls.get()

        print(f"\nAnalisando URL: {url}")

        # Envia a URL para o motor de análise.
        resultado = analisar_url(url)

        # Coloca o resultado na fila específica
        # dessa URL.
        fila_resultado.put(resultado)

        # Informa que terminou o processamento dessa URL.
        fila_urls.task_done()

        # Espera 15 segundos antes de processar
        # a próxima URL.
        print(
            f"Aguardando {INTERVALO_REQUISICAO} segundos "
            "para a próxima requisição"
        )

        time.sleep(INTERVALO_REQUISICAO)




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

    # verificando se a requisição foi bloqueada pelo limite da API

    if requisicao.status_code == 429:
        print("Limite de requisições da API do VirusTotal atingido.")
        print("Resposta da API:")
        print(dados)
        return {"erro": "Limite da API atingido"}

    # verificando se a requisição apresentou outro erro

    if requisicao.status_code != 200:

        print("Erro na requisição ao VirusTotal.")

        return {
            "erro": f"Erro HTTP {requisicao.status_code}"
        }

    # verificando se a resposta possui os dados esperados

    if "data" not in dados:

        print("Resposta inesperada do VirusTotal:")

        print(dados)

        return {
            "erro": "Resposta inesperada da API"
        }

    # atribuindo as estatísticas da análise a uma variável estatisticas, que é um dicionário com as informações da análise da URL

    estatisticas = dados["data"]["attributes"]["last_analysis_stats"]

    for chave, valor in estatisticas.items():

        print(f"\n{chave}: {valor}")

    # Classificando a URL de acordo com a quantidade de mecanismos
# que a identificaram como maliciosa.
    if estatisticas["malicious"] >= 2:
        classificacao = "Maligna"

    elif estatisticas["malicious"] == 1:
        classificacao = "Suspeita"

    else:
        classificacao = "Legitima"

# Adicionando a classificação às estatísticas da análise.
    estatisticas["\nclassificacao"] = classificacao

    return estatisticas

# Inicia o processamento da fila em segundo plano.
# O daemon=True significa, de forma simples, 
#que essa thread acompanha a execução principal 
#do programa e não impede o Python de ser encerrado.
Thread(target=processar_fila, daemon=True).start()