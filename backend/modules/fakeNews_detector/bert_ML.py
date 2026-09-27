# Importa o tokenizer e o modelo BERT para classificação
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Importa o pandas para trabalhar com o dataset
import pandas as pd

# Importa o PyTorch, utilizado no treinamento do modelo
import torch

# Importa Dataset e DataLoader para organizar os dados em lotes
from torch.utils.data import Dataset, DataLoader


# ============================================================
# NOME DO MODELO BERT
# ============================================================

bert = "neuralmind/bert-base-portuguese-cased"


# ============================================================
# CARREGANDO O TOKENIZER
# ============================================================

print("\nCarregando tokenizer...")

# O tokenizer transforma o texto em tokens e números
# que o BERT consegue entender.
tokenizer = AutoTokenizer.from_pretrained(bert)


# ============================================================
# CARREGANDO O BERT
# ============================================================

print("\nCarregando BERT...")

# Carrega o BERT preparado para classificação de textos.
#
# num_labels=2 significa que teremos duas classes:
#
# 0 = notícia falsa
# 1 = notícia verdadeira
#
carrega_BERT = AutoModelForSequenceClassification.from_pretrained(
    bert,
    num_labels=2
)


# ============================================================
# CARREGANDO O DATASET DE TREINAMENTO
# ============================================================

# Lê o arquivo CSV que contém as notícias de treinamento.
dataset_treino = pd.read_csv("dataset_treino.csv")


# X = textos das notícias
# y = rótulos das notícias
#
# .tolist() transforma a coluna do pandas
# em uma lista Python.
X_treino = dataset_treino["texto"].tolist()

y_treino = dataset_treino["rotulo"].tolist()


# Mostra quantos textos serão utilizados no treinamento.
print("\nTotal de textos para treinamento:", len(X_treino))


