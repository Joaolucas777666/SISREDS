from transformers import AutoTokenizer, AutoModel
import torch

nome_modelo = "neuralmind/bert-base-portuguese-cased"

print("Carregando tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(nome_modelo)

print("Carregando modelo...")
modelo = AutoModel.from_pretrained(nome_modelo)

texto = """
O governo anunciou nesta terça-feira uma nova medida
para ampliar o acesso da população à educação.
"""

print("\nTexto original:")
print(texto)

# Transforma o texto em tokens que o BERT consegue entender
entradas = tokenizer(
    texto,
    return_tensors="pt"
)

print("\nDados enviados para o BERT:")
print(entradas)

# Desativa o cálculo de gradientes porque ainda não estamos treinando
with torch.no_grad():
    saida = modelo(**entradas)

print("\nBERT processou o texto!")
print("Dimensão da saída:")
print(saida.last_hidden_state.shape)