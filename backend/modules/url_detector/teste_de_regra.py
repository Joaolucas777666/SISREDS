import pandas as pd # importando pandas
from url_detector import analisar_url # importando a função analisar_url do módulo url_detector
import time

# Teste de regra de detecção malicious >=2 == Url Maligna

resultado_regra_lista = []

urls_malignas_regra = [

    "http://125.41.224.2:59933/bin.sh",
    "http://125.43.246.211:40926/bin.sh",
    "http://101.59.79.119:50248/i",
    "http://105.186.221.48:45881/i",
    "http://113.228.148.143:56788/i",
    "http://182.116.48.4:52963/i",
    "http://101.59.79.119:50248/bin.sh",
    "http://113.228.148.143:56788/bin.sh",
    "https://workerstats.net/downloadables/nig20083.zip	",
    "https://workerstats.net/downloadables/getthem20083.zip",
    "https://get.actvated.win/Update.zip",
    "https://srv.conti.pk/contis.exe",
    "http://194.59.31.231:65416/b/kal64",
    "http://194.59.31.231:65416/b/amd64",
    "http://194.59.31.231:65416/b/kswpad",
    "https://get.activatd.win/",
    "http://5.75.162.206:9003/fission_payload.sh",
    "https://copiose.org/test_proliv/b?o=df2d61526e27a2bc",
    "http://112.93.139.83:48371/i",
    "http://213.232.114.14/sshd",
    "https://45.145.12.239/main.exe",
    "http://101.85.133.18:60949/i",
    "http://61.52.147.68:37007/i",
    "http://221.14.170.47:43520/i",
    "http://190.109.227.236:33009/i"


]

urls_legitimas_regra = [

    "https://www.ibm.com",
    
"https://www.intel.com",
    "https://www.amd.com",
    "https://www.nvidia.com",
    "https://www.cisco.com",
    "https://www.oracle.com",
    "https://www.redhat.com",
    "https://www.jetbrains.com",
    "https://www.eclipse.org",
    "https://www.w3.org",
    "https://developer.mozilla.org",
    "https://stackoverflow.com",
    "https://www.linuxfoundation.org",
    "https://www.r-project.org",
    "https://www.mathworks.com",
    "https://www.autodesk.com",
    "https://www.adobe.com",
    "https://www.sony.com",
    "https://www.samsung.com",
    "https://www.nintendo.com",
    "https://www.playstation.com",
    "https://www.xbox.com",
    "https://www.spotify.com",
    "https://www.intuit.com",
    "https://www.salesforce.com"

    
]

for i, url in enumerate (urls_legitimas_regra):

    # Laço utilizado para percorrer a lista de URLs.
    # O enumerate() permite obter o índice de cada URL.
    print(f"Analisando URL {i + 1} de {len(urls_legitimas_regra)}: {url}")
    resultado = analisar_url(url)

    if "erro" in resultado:

        resultado_regra = "Não analisada"

    else:

        # se o atributo "malicious" for maior ou igual a 2
        # classifique como maligna.

        if resultado["malicious"] >= 2:
            resultado_regra = "Maligna"
        else:
            resultado_regra = "Legitima"

    linha = {
        "Classificação real": "Legitima",
        "Url": url,
        "Malicious": resultado.get("malicious", ""),
        "Resultado da regra": resultado_regra
    }

    resultado_regra_lista.append(linha)

    # Tranforma o resultado em dataframe
    dados_regra = pd.DataFrame(resultado_regra_lista)
    # Salva o dataframe em "teste_regra.csv"
    dados_regra.to_csv("teste_regra.csv", index=False)

    # Espera 15 segundos antes da próxima requisição.
    # Não espera depois da última URL.
    if i < len(urls_legitimas_regra) - 1:
        print("Aguardando 15 segundos...")
        time.sleep(15)


for i, url in enumerate (urls_malignas_regra):
    # Laço utilizado para percorrer a lista de URLs.
    # O enumerate() permite obter o índice de cada URL.
    print(f"Analisando URL {i + 26} de 50: {url}")
    resultado = analisar_url(url)

    if "erro" in resultado:

        resultado_regra = "Não analisada"

    else:

        # se o atributo "malicious" for maior ou igual a 2
        # classifique como maligna.

        if resultado["malicious"] >= 2:
            resultado_regra = "Maligna"
        else:
            resultado_regra = "Legitima"

    linha = {
        "Classificação real": "Maligna",
        "Url": url,
        "Malicious": resultado.get("malicious", ""),
        "Resultado da regra": resultado_regra
    }

    resultado_regra_lista.append(linha)

    # Tranforma o resultado em dataframe
    dados_regra = pd.DataFrame(resultado_regra_lista)
    # Salva o dataframe em "teste_regra.csv"
    dados_regra.to_csv("teste_regra.csv", index=False)

    # se ainda não for a ultima url, espere 15 segundos...
    if i < len(urls_malignas_regra) - 1:
        print("Aguardando 15 segundos...")
        time.sleep(15)




print("Teste da regra concluído!")
print("teste_regra.csv")