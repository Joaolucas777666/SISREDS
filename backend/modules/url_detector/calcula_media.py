import pandas as pd
import dtale


def analisar_dados(dados):
    # Calculando a média das estatísticas por classificação
    media = dados.groupby("Classificação")[
        ["Malicious", "Suspicious", "Harmless", "Undetected"]
    ].mean()

    # Frequência de valores de Malicious
    frequencia_malicious = dados.groupby(
        ["Classificação", "Malicious"]
    ).size().reset_index(name="Quantidade")

    # Frequência de valores de Suspicious
    frequencia_suspicious = dados.groupby(
        ["Classificação", "Suspicious"]
    ).size().reset_index(name="Quantidade")

    # Frequência de valores de Harmless
    frequencia_harmless = dados.groupby(
        ["Classificação", "Harmless"]
    ).size().reset_index(name="Quantidade")

    return media, frequencia_malicious, frequencia_suspicious, frequencia_harmless


# Lendo os arquivos CSV
dados1 = pd.read_csv("teste1.csv")
dados2 = pd.read_csv("teste2.csv")


# Realizando as análises
media1, malicious1, suspicious1, harmless1 = analisar_dados(dados1)
media2, malicious2, suspicious2, harmless2 = analisar_dados(dados2)


# Exibindo os resultados no D-Tale
m_geral1 = dtale.show(media1)
m_malicious1 = dtale.show(malicious1)
m_suspicious1 = dtale.show(suspicious1)
m_harmless1 = dtale.show(harmless1)

m_geral2 = dtale.show(media2)
m_malicious2 = dtale.show(malicious2)
m_suspicious2 = dtale.show(suspicious2)
m_harmless2 = dtale.show(harmless2)


# Mostrando as URLs do D-Tale
print("Teste 1 - média geral:", m_geral1.main_url())
print("Teste 1 - frequência Malicious:", m_malicious1.main_url())
print("Teste 1 - frequência Suspicious:", m_suspicious1.main_url())
print("Teste 1 - frequência Harmless:", m_harmless1.main_url())

print("\nTeste 2 - média geral:", m_geral2.main_url())
print("Teste 2 - frequência Malicious:", m_malicious2.main_url())
print("Teste 2 - frequência Suspicious:", m_suspicious2.main_url())
print("Teste 2 - frequência Harmless:", m_harmless2.main_url())



# Resultados do Teste 1:
# - Foram analisadas 30 URLs, sendo 15 legítimas e 15 maliciosas.
# - Média Malicious: 0,00 para URLs legítimas e 4,60 para URLs maliciosas.
# - Média Suspicious: 0,00 para URLs legítimas e 0,87 para URLs maliciosas.
# - Média Harmless: 60,13 para URLs legítimas e 51,80 para URLs maliciosas.
# - Nas URLs legítimas, o valor de Malicious foi 0 em todas as amostras.
# - Nas URLs maliciosas, a maioria apresentou valores de Malicious acima de 0,
#   embora algumas também tenham apresentado valor 0.
# - Os resultados indicam diferenças entre URLs legítimas e maliciosas,
#   principalmente nos indicadores Malicious e Harmless.

# Resultados do Teste 2:
# - Foram analisadas 100 URLs, sendo 50 legítimas e 50 maliciosas.
# - Malicious: 47 legítimas apresentaram 0 e 3 apresentaram 1.
#   As 50 maliciosas apresentaram valores entre 2 e 16.
# - Suspicious: todas as legítimas apresentaram 0. Entre as maliciosas,
#   27 apresentaram 0, 17 apresentaram 1, 5 apresentaram 2 e 1 apresentou 3.
# - Harmless: as legítimas apresentaram valores entre 56 e 62,
#   enquanto as maliciosas apresentaram valores entre 45 e 54.
# - Os resultados indicam que Malicious apresentou a maior capacidade
#   de diferenciação entre URLs legítimas e maliciosas no conjunto testado.

# Após análise dos resultados dos testes 1 e 2, notou-se 3 falso positivos
# em que urls legítimas obtiveram 1 atributo Malicious 
# e tambem que todas urls que obtiveram 2 atrributos malicious em diante
# eram urls malignas.  

# Diante disso, serão analisados os casos fronteira, ou seja, as URLs que
# apresentaram valores de Malicious iguais a 0 ou 1.
# Essa análise será realizada utilizando também os atributos Suspicious e
# Harmless, buscando identificar padrões que permitam diferenciar melhor
# URLs legítimas de URLs maliciosas.
#
# Esse método será utilizado para evitar que a classificação seja definida
# apenas pelo atributo Malicious. A análise conjunta dos indicadores permitirá
# avaliar as evidências de ameaça e de segurança presentes em cada URL,
# contribuindo para a definição de uma regra de classificação mais adequada
# aos resultados obtidos nos testes.


# juntandos os df do teste1 e teste2
dados_completos = pd.concat([dados1, dados2])

# filtrando os casos de urls que obtiveram valor de "malicious" igual a 0 
casos_malicious_0 = dados_completos[
    dados_completos["Malicious"] == 0
]
# filtrando os casos de urls que obtiveram valor de "malicious" igual a 1
casos_malicious_1 = dados_completos[
    dados_completos["Malicious"] == 1
]

# Exibindo os resultados no D-Tale
m_casos_malicious0 = dtale.show(casos_malicious_0)
m_casos_malicious1 = dtale.show(casos_malicious_1)

# Mostrando as URLs do D-Tale
print("\nAnálise de casos fronteira - URLs com casos malicious == 0:", m_casos_malicious0.main_url())
print("Análise de casos fronteira - URLs com casos malicious == 1:", m_casos_malicious1.main_url())

input("\nPressione Enter para encerrar o D-Tale...")
