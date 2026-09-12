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


input("\nPressione Enter para encerrar o D-Tale...")