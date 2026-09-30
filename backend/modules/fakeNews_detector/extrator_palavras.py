# Importando biblioteca para trabalhar com NLP
import spacy


# Palavras que normalmente não ajudam na busca
STOPWORDS = {
    "a", "à", "ao", "aos", "as", "às",
    "o", "os", "um", "uma", "uns", "umas",
    "de", "da", "das", "do", "dos",
    "e", "é", "em", "no", "na", "nos", "nas",
    "por", "para", "com", "sem",
    "que", "se", "ser", "são",
    "foi", "foram", "era", "eram",
    "como", "mais", "menos",
    "já", "não", "sim",
    "seu", "sua", "seus", "suas",
    "esse", "essa", "esses", "essas",
    "este", "esta", "estes", "estas",
    "isso", "isto",
    "ele", "ela", "eles", "elas",
    "sobre", "entre", "também",
    "muito", "muita", "muitos", "muitas"
}


# Adjetivos muito genéricos que não ajudam
# na identificação de uma notícia
ADJETIVOS_GENERICOS = {
    "novo",
    "nova",
    "novos",
    "novas",
    "grande",
    "grandes",
    "importante",
    "importantes",
    "principal",
    "principais",
    "último",
    "última",
    "últimos",
    "últimas"
}


# Carrega o modelo de português do spaCy
nlp = spacy.load("pt_core_news_sm")


def extrair_entidades(texto):
    """
    Identifica entidades importantes presentes no texto.
    """

    # Processa o texto
    doc = nlp(texto)

    entidades = []

    # Percorre as entidades encontradas
    for entidade in doc.ents:

        # Remove espaços desnecessários
        nome = entidade.text.strip()

        # Remove artigos do início da entidade
        palavras = nome.split()

        while palavras and palavras[0].lower() in STOPWORDS:
            palavras.pop(0)

        nome = " ".join(palavras)

        # Evita entidades muito pequenas
        if len(nome) >= 3:
            entidades.append(nome)

    return entidades


def extrair_palavras_frequentes(texto, quantidade=10):
    """
    Identifica palavras relevantes através da frequência.
    """

    # Processa o texto utilizando o spaCy
    doc = nlp(texto)

    palavras = []

    # Percorre cada palavra do texto
    for token in doc:

        # Ignora pontuação
        if token.is_punct:
            continue

        # Ignora stopwords
        if token.text.lower() in STOPWORDS:
            continue

        # Ignora números isolados
        if token.like_num:
            continue

        # Ignora adjetivos genéricos
        if (
            token.pos_ == "ADJ"
            and token.text.lower() in ADJETIVOS_GENERICOS
        ):
            continue

        # Mantém substantivos, nomes próprios e adjetivos
        if token.pos_ in ["NOUN", "PROPN", "ADJ"]:
            palavras.append(token.text.lower())

    # Conta a frequência das palavras
    frequencias = {}

    for palavra in palavras:
        frequencias[palavra] = frequencias.get(palavra, 0) + 1

    # Ordena pela frequência
    palavras_ordenadas = sorted(
        frequencias.items(),
        key=lambda item: item[1],
        reverse=True
    )

    # Retorna as palavras mais frequentes
    return [
        palavra
        for palavra, frequencia in palavras_ordenadas[:quantidade]
    ]


def extrair_termos_busca(texto, quantidade=10):
    """
    Combina entidades do spaCy com palavras relevantes,
    evitando duplicações.
    """

    # Extrai entidades
    entidades = extrair_entidades(texto)

    # Extrai palavras relevantes
    palavras = extrair_palavras_frequentes(
        texto,
        quantidade
    )

    # Guarda todas as palavras presentes nas entidades
    palavras_das_entidades = set()

    for entidade in entidades:

        palavras_entidade = entidade.lower().split()

        for palavra in palavras_entidade:
            palavras_das_entidades.add(palavra)

    # Remove palavras que já estão dentro das entidades
    palavras_filtradas = [
        palavra
        for palavra in palavras
        if palavra not in palavras_das_entidades
    ]

    # Junta os resultados
    termos = entidades + palavras_filtradas

    # Remove duplicatas mantendo a ordem
    termos_unicos = list(dict.fromkeys(termos))

    return termos_unicos


# ---------------------------------------------------------
# TESTE
# ---------------------------------------------------------

noticia_teste = """
A campanha do senador Flávio Bolsonaro (PL-RJ) 
aposta na reação de torcidas organizadas à 
proibição das bets para devolver ao presidente
Luiz Inácio Lula da Silva (PT) o desgaste 
provocado pelas polêmicas em torno de 
Nossa Senhora Aparecida.
"""


# Extrai os termos
termos = extrair_termos_busca(noticia_teste)


# Exibe o resultado
print("Termos encontrados para busca:")
print()

for termo in termos:
    print("-", termo)