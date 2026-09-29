#transforma o texto das notícias em números que o BERT consegue entender.
#AutoModelForSequenceClassification → carrega nosso BERT já treinado para fazer a classificação em 2 classes
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import pandas as pd # Usaremos o Pandas para abrir o dataset_teste.csv.
import torch # É o PyTorch, que vamos usar para executar o modelo e trabalhar com tensores.
from torch.utils.data import Dataset, DataLoader #Dataset → organiza as notícias. DataLoader → entrega as notícias ao BERT em lotes.

# accuracy_score → quantidade geral de acertos.
# precision_score → precisão das classificações.
# recall_score → capacidade de encontrar corretamente uma determinada classe.
# f1_score → combina Precision e Recall.
# confusion_matrix → mostra onde o modelo acertou e onde confundiu as classes.
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# CARREGANDO O TOKENIZER

caminho_modelo = "modelo_treinado"

print("\nCarregando tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(caminho_modelo)

# CARREGANDO MODELO TREINADO 

print("\nCarregando modelo treinado...")
modelo = AutoModelForSequenceClassification.from_pretrained(caminho_modelo)

print("\nModelo carregado com sucesso!")

# CHAMANDO O DATASET PARA O TESTE

print("\nCarregando dataset_teste.csv")

dataset_teste = pd.read_csv("dataset_teste.csv")

# transformando texto e rotulo do dataset em lista python, para auxiliar na leitura
X_teste = list(dataset_teste["texto"])
y_teste = list(dataset_teste["rotulo"])

print("\nTotal de textos para teste", len(X_teste))

# CRIANDO O DATASET DE TESTE 

class DatasetNoticias(Dataset):

    def __init__(self, textos):
        self.textos = textos

    def __len__(self):
        return len(self.textos)

    def __getitem__(self, indice):

        texto = self.textos[indice]

        entradas = tokenizer(
            texto,
            padding="max_length",
            truncation=True,
            max_length=256,
            return_tensors="pt"
        )

        return {
            "input_ids": entradas["input_ids"].squeeze(),
            "attention_mask": entradas["attention_mask"].squeeze()
        }

# CRIANDO DATALOADER 

dataset = DatasetNoticias(X_teste)

print("\nTotal de notícias no Dataset:", len(dataset))


dataloader = DataLoader(
    dataset,
    batch_size=8,
    shuffle=False
)

print("Total de batches:", len(dataloader))

# COLOCANDO O MODELO EM MODO DE AVALIAÇÃO

modelo.eval()

print("\nModelo colocado em modo de avaliação")

# LISTA QUE VAI ARMAZENAR AS PREVISÕES DO MODELO

previsoes = []

# FAZENDO PREVISÕES SEM CALCULAR GRADIENTE

with torch.no_grad():

    for lote in dataloader:
        #dados que o BERT precisa para interpretar os textos.
        input_ids = lote["input_ids"]
        attention_mask = lote["attention_mask"]
        #as notícias entram no BERT
        saida = modelo(
            input_ids=input_ids,
            attention_mask=attention_mask
        )
        # como usamos duas classes (0 e 1)
        # o modelo produz dois valores:
        # Ex: Notícia 1:
                        #classe 0 → 1.82
                        #classe 1 → -0.35
        logits = saida.logits
        # para escolher a maior delas que usamos:
        previsoes_lote = torch.argmax(logits, dim=1)
        # junta as previsões dos batches
        previsoes.extend(previsoes_lote.tolist())

print("\nTotal de previsões realizadas:", len(previsoes))

# COMPARANDO AS PREVISÕES COM OS RÓTULOS REAIS

print("\nCalculando métricas...")

acuracia = accuracy_score(y_teste, previsoes)

precisao = precision_score(y_teste, previsoes)

recall = recall_score(y_teste, previsoes)

f1 = f1_score(y_teste, previsoes)


print("\n===== RESULTADOS DA AVALIAÇÃO =====")

print(f"Acurácia:  {acuracia:.4f}")
print(f"Precisão:  {precisao:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-score:  {f1:.4f}")

# MATRIZ DE CONFUSÃO

matriz = confusion_matrix(y_teste, previsoes)

print("\n===== MATRIZ DE CONFUSÃO =====")
print(matriz)

# MATRIZ DE CONFUSÃO

matriz = confusion_matrix(y_teste, previsoes)

print("\n===== MATRIZ DE CONFUSÃO =====")
print(matriz)


# SALVANDO OS RESULTADOS DA AVALIAÇÃO

with open("resultado_avaliacao.txt", "w", encoding="utf-8") as arquivo:

    arquivo.write("===== AVALIAÇÃO DO MODELO BERT =====\n\n")

    arquivo.write(f"Total de notícias avaliadas: {len(y_teste)}\n\n")

    arquivo.write("MÉTRICAS:\n")
    arquivo.write(f"Acurácia: {acuracia:.4f}\n")
    arquivo.write(f"Precisão: {precisao:.4f}\n")
    arquivo.write(f"Recall: {recall:.4f}\n")
    arquivo.write(f"F1-score: {f1:.4f}\n\n")

    arquivo.write("MATRIZ DE CONFUSÃO:\n")
    arquivo.write(str(matriz))

print("\nResultados salvos em: resultado_avaliacao.txt")