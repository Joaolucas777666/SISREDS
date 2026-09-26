# Importando biblioteca Path para trabalhar
# caminhos de diretorios
from pathlib import Path
import pandas as pd

# caminho da pasta que contem o dataset que vamos utilizar
pasta_dataset = Path("Fake.br-Corpus/full_texts")

# lista onde serão armazenados os dados
dados = []

    # Lê as notícias falsas
for arquivo in (pasta_dataset / "fake").glob("*.txt"):
    # Aqui estamos abrindo o arquivo.
    # A função open() abre um arquivo.
    # "arquivo" É o arquivo encontrado pelo for.
    # "r" significa read, ou seja leitura
    # encoding="utf-8" Define a codificação utilizada para ler o arquivo.
    # "as f" Aqui damos um apelido para o arquivo aberto: f
    with open(arquivo, "r", encoding="utf-8") as f:
        texto = f.read()

    dados.append({
        "texto": texto,
        "rotulo": 0
    })


# Lê as notícias verdadeiras
for arquivo in (pasta_dataset / "true").glob("*.txt"):
    # Aqui estamos abrindo o arquivo.
    # A função open() abre um arquivo.
    # "arquivo" É o arquivo encontrado pelo for.
    # "r" significa read, ou seja leitura
    # encoding="utf-8" Define a codificação utilizada para ler o arquivo.
    # "as f" Aqui damos um apelido para o arquivo aberto: f
    with open(arquivo, "r", encoding="utf-8") as f:
        texto = f.read()

    dados.append({
        "texto": texto,
        "rotulo": 1
    })


# Cria a tabela
dataset = pd.DataFrame(dados)


# Embaralha as notícias
dataset = dataset.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)


# Salva o CSV
dataset.to_csv(
    "dataset_BERT.csv",
    index=False,
    encoding="utf-8"
)


# Mostra informações
print("Dataset criado com sucesso!")
print("Total de notícias:", len(dataset))
print()
print(dataset["rotulo"].value_counts())

    

