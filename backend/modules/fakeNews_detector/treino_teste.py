import pandas as pd
# importando train_test_split para dividir
# o dataset em treino e testes
from sklearn.model_selection import train_test_split

# carrega o dataset
dataset = pd.read_csv("datasets/dataset_BERT.csv")

# X = texto das noticias
# y = rotulos das noticias (true=1, false=0)
X = dataset["texto"]
y = dataset["rotulo"]

# Separa 80% para treinamento e 20% para validação + teste
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X,
    y,
    test_size=0.20, #separa 20% para teste.
    random_state=42, #mantém a mesma divisão toda vez que executar.
    stratify=y # mantém a proporção de fake/verdadeira nos dois grupos.
)

# criando dataset do treino
dataset_treino = pd.DataFrame({
    "texto": X_treino,
    "rotulo": y_treino
})

# criando dataset do teste
dataset_teste = pd.DataFrame({
    "texto": X_teste,
    "rotulo": y_teste
})

# Salva os dataset_treino.csv
dataset_treino.to_csv(
    "dataset_treino.csv",
    index=False,
    encoding="utf-8"
)

# Salva os dataset_teste.csv
dataset_teste.to_csv(
    "dataset_teste.csv",
    index=False,
    encoding="utf-8"
)

print("Datasets criados com sucesso!")
print()
print("Treinamento:", len(dataset_treino))
print("Teste:", len(dataset_teste))

