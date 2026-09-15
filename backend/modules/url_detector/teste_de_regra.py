import pandas as pd # importando pandas
from url_detector import analisar_url # importando a função analisar_url do módulo url_detector

# Teste de regra de detecção malicious >=2 == Url Maligna

resultado_regra_lista = []

urls_malignas_regra = [

    "http://125.41.224.2:59933/bin.sh"
    
]

urls_legitimas_regra = [

    "https://www.ibm.com"
    
]

for url in urls_legitimas_regra:

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
        "Malicious": resultado.get("Malicious", ""),
        "Resultado da regra": resultado_regra
    }

    resultado_regra_lista.append(linha)


for url in urls_malignas_regra:

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
        "Malicious": resultado.get("Malicious", ""),
        "Resultado da regra": resultado_regra
    }

    resultado_regra_lista.append(linha)

# Tranforma o resultado em dataframe
dados_regra = pd.DataFrame(resultado_regra_lista)
# Salva o dataframe em "teste_regra.csv"
dados_regra.to_csv("teste_regra.csv", index=False)

print("Teste da regra concluído!")
print("teste_regra.csv")