# Importa o tokenizer e o modelo BERT para classificação
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Importa o pandas para trabalhar com o dataset
import pandas as pd

# Importa o PyTorch, utilizado no treinamento do modelo
import torch

# Importa Dataset e DataLoader para organizar os dados em lotes
from torch.utils.data import Dataset, DataLoader



# NOME DO MODELO BERT
bert = "neuralmind/bert-base-portuguese-cased"



# CARREGANDO O TOKENIZER
print("\nCarregando tokenizer...")
# O tokenizer transforma o texto em tokens e números
# que o BERT consegue entender.
tokenizer = AutoTokenizer.from_pretrained(bert)



# CARREGANDO O BERT
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



# CARREGANDO O DATASET DE TREINAMENTO
# Lê o arquivo CSV que contém as notícias de treinamento.
dataset_treino = pd.read_csv("dataset_treino.csv")


# X = textos das notícias
# y = rótulos das notícias
#
# list transforma a coluna do pandas
# em uma lista Python.
X_treino = list(dataset_treino["texto"])
y_treino = list(dataset_treino["rotulo"])


# Mostra quantos textos serão utilizados no treinamento.
print("\nTotal de textos para treinamento:", len(X_treino))


# CLASSE PARA ORGANIZAR NOTÍCIAS
class DatasetNoticias(Dataset): #Dataset é a classe que herdamos da blioteca PyTorch
    def __init__(self, textos, rotulos):
        self.textos = textos
        self.rotulos = rotulos
    
    # Informa quantas notícias existem no dataset
    def __len__(self):
        return len(self.textos)

    # Pega uma notícia específica pelo índice
    def __getitem__(self, indice):

        texto = self.textos[indice]
        rotulo = self.rotulos[indice]

        # Transforma o texto em números
        #  que o BERT consegue entender
        entradas = tokenizer(
            texto, #pegando o texto da notícia e passando para o tokenizer
            padding="max_length", #Determina que todas as notícias terão o mesmo tamanho de entrada.
            truncation=True, #Se uma notícia tiver mais de 512 tokens, ela será cortada para caber no limite.
            max_length=512, #cada notícia terá espaço para 512 tokens.
            return_tensors="pt" # devolva os resultados no formato de tensores do PyTorch   
        )
        return {
                        "input_ids": entradas["input_ids"].squeeze(),
                        "attention_mask": entradas["attention_mask"].squeeze(),
                        "labels": torch.tensor(rotulo)
        }

# CRIANDO DATASET
dataset = DatasetNoticias(X_treino, y_treino)

# Mostra quantas notícias existem no dataset
print("\nTotal de notícias no Dataset", len(dataset))

# Pega a primeira notícia do Dataset
primeira_noticia = dataset[0]

print(primeira_noticia)


# CRIANDO O DATALOADER 
# para trabalhar com notícias em lotes

dataloader = DataLoader(
    dataset,
    batch_size=8, # separa as 5760 noticias em lotes(batch) de 8, ou seja 5760/8 = 720 por batch
    shuffle=True # embaralha as noticias do dataset
)

print("Total de batches:", len(dataloader))

# Cria um iterador para percorrer os lotes do DataLoader
# e pega o primeiro lote.
primeiro_lote = next(iter(dataloader))


# Mostra o formato dos dados do primeiro lote
print("Formato dos input_ids:", primeiro_lote["input_ids"].shape)

print("Formato da attention_mask:", primeiro_lote["attention_mask"].shape)

print("Formato dos labels:", primeiro_lote["labels"].shape)

# ESCOLHENDO DISPÓSITIVO

# Verifica se o PyTorch encontrou uma GPU CUDA disponível.
# Se encontrar, utiliza a GPU.
# Caso contrário, utiliza o processador (CPU).
dispositivo = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

print("Dispositivo utilizado:", dispositivo)

# ENVIANDO O BERT PARA O DISPOSITIVO

carrega_BERT.to(dispositivo)

print("BERT enviado para:", dispositivo)

# CRIANDO O OTIMIZADOR

# O otimizador será responsável por ajustar
# os parâmetros do BERT durante o treinamento.
otimizador = torch.optim.AdamW(
    carrega_BERT.parameters(),
    lr=2e-5
)

print("Otimizador criado com sucesso!")

# CONFIGURANDO O TREINAMENTO

# Define quantas vezes o BERT vai passar por todo
# o conjunto de notícias de treinamento.
epocas = 3 # 3 vezes

# Coloca o BERT em modo de treinamento.
carrega_BERT.train()


# INICIANDO O TREINAMENTO

for epoca in range(epocas):

    # Guarda a soma das perdas de todos os lotes
    # dessa época.
    perda_total = 0

    print(f"\nIniciando época {epoca + 1} de {epocas}...")


    # Percorre os 720 lotes do DataLoader.
    for lote in dataloader:

        # Pega os tokens das notícias
        # e envia para o dispositivo.
        input_ids = lote["input_ids"].to(dispositivo)

        # Pega a máscara de atenção
        # e envia para o dispositivo.
        attention_mask = lote["attention_mask"].to(dispositivo)

        # Pega os rótulos das notícias
        # e envia para o dispositivo.
        labels = lote["labels"].to(dispositivo)


        # Zera os gradientes da etapa anterior.
        otimizador.zero_grad()


        # Envia o lote para o BERT.
        #
        # O labels permite que o BERT calcule
        # automaticamente a perda (loss).
        saida = carrega_BERT(
            input_ids=input_ids,
            attention_mask=attention_mask,
            labels=labels
        )


        # Obtém a perda calculada pelo BERT.
        perda = saida.loss


        # Calcula os gradientes.
        perda.backward()


        # Atualiza os parâmetros do BERT.
        otimizador.step()


        # Soma a perda desse lote
        # à perda total da época.
        perda_total += perda.item()


    # Calcula a perda média da época.
    perda_media = perda_total / len(dataloader)


    # Mostra o resultado da época.
    print(
        f"Época {epoca + 1}/{epocas} "
        f"- Perda média: {perda_media:.4f}"
    )