from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# CAMINHO DO MODELO TREINADO 

caminho_modelo = "modelo_treinado"

# CARREGANDO TOKENIZER

tokenizer = AutoTokenizer.from_pretrained(caminho_modelo)

# CARREGANDO MODELO TREINADO

modelo = AutoModelForSequenceClassification.from_pretrained(caminho_modelo)

# COLOCANDO O MODELO EM MODO DE AVALIAÇÃO

modelo.eval()

def classificar_noticia(texto):
    entradas = tokenizer(
        texto,
        padding="max_length",
        truncation=True,
        max_length=256,
        return_tensors="pt"
    )

    with torch.no_grad():
        saida = modelo(
            input_ids=entradas["input_ids"],
            attention_mask=entradas["attention_mask"]
        )

    # Transforma os logits em probabilidades
    probabilidades = torch.softmax(saida.logits, dim=1)

    # Pega a classe com maior probabilidade
    classe = torch.argmax(probabilidades, dim=1).item()

    # Pega a porcentagem da classe escolhida
    confianca = probabilidades[0][classe].item() * 100

    return classe, confianca

# TESTE DO CLASSIFICADOR

texto_teste = input("\nDigite uma notícia para analisar: ")

resultado, confianca = classificar_noticia(texto_teste)

if resultado == 0:
    print("\nResultado: NOTÍCIA FALSA")
else:
    print("\nResultado: NOTÍCIA VERDADEIRA")

print(f"Confiança do modelo: {confianca:.2f}%")