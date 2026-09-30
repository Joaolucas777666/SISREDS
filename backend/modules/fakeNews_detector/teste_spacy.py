import spacy

# Carrega o modelo de português
nlp = spacy.load("pt_core_news_sm")

texto = """
O Ministério da Educação anunciou novos investimentos
para universidades federais em Brasília em 2026.
O ministro afirmou que serão investidos R$ 500 milhões
no programa.
"""

# Processa o texto
doc = nlp(texto)

print("Entidades encontradas:\n")

for entidade in doc.ents:
    print(f"Texto: {entidade.text}")
    print(f"Tipo: {entidade.label_}")
    print("---")