import kagglehub
import os
import pandas as pd

# transforma texto em numeros
from sklearn.feature_extraction.text import TfidfVectorizer
# ML que vai ser utilizado
from sklearn.linear_model import LogisticRegression
# dividir nossos dados aleatoriamente em conjuntos diferentes
from sklearn.model_selection import train_test_split

# Baixa a versão mais recente do dataset
path = kagglehub.dataset_download("sid321axn/malicious-urls-dataset")

print("Path to dataset files:", path)

# Caminho do arquivo CSV
arquivo = os.path.join(path, "malicious_phish.csv")

# Abre o dataset
df = pd.read_csv(arquivo)

X = df["url"] # vai conter as urls do dataset
y = df["type"] # vai conter o tipo das urls do dataset (Resposta esperada)

print("\nExemplos de X")
print(X.head())

print("\nExermplos de y")
print(y.head())

#transforma as urls em numeros para a ML entender
vetorizador = TfidfVectorizer(analyzer="char")

# ML aprende e memoriza os padroes de caracteres
X =vetorizador.fit_transform(X)

X_treino, X_teste, y_treino, y_teste = train_test_split(

    X, #URLs transformadas pelo TF-IDF
    y, #classificação correta de cada URL
    test_size=0.2, #reserva 20% dos dados para teste e usa 80% para treinamento
    random_state=42, #faz com que a divisão seja reproduzível. Se você executar novamente, terá a mesma divisão
    stratify=y # mantém aproximadamente a mesma proporção das quatro classes nos conjuntos de treinamento e teste.

)

print("\nDados de treinamento:", X_treino.shape)
print("Dados de teste:", X_teste.shape)

# cria o modelo de ML
modelo = LogisticRegression(max_iter=1000)

# treina  o modelo
modelo.fit(X_treino, y_treino)

print("\nModelo treinado com sucesso")

# NAO EXECUTE AGORA!

