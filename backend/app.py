#importando o flask e o render_template para renderizar o html
#  e jsonify para retornar json e cors para permitir requisições de outros domínios
from flask import Flask, render_template, jsonify, request 
from flask_cors import CORS
from modules.url_detector.url_detector import adicionar_fila

# criando a aplicação flask
app = Flask(__name__)

# permitindo requisições de outros domínios
CORS(app)

# criando a rota para a página inicial
@app.route("/")

# criando a função para renderizar o html
def inicio():
    return render_template("index.html")

# criando rota de teste da API
@app.route("/api/status")
# criando a função para retornar o status da API
def api_status():
    # retornando um json com o status da API
    return jsonify({"status": "Online!",
                    "Sistema": "SISREDS"
                    })

# criando rota para analisar a url
@app.route("/api/analisar-url", methods=["POST"])
# criando a função para analisar a url
def analisar_url_api():
        # obtendo a url do corpo da requisição
        dados = request.get_json()
        url = dados["url"]

        # imprimindo a url recebida no console do terminal
        print(f"\nURL recebida: {url}")

        resultado = adicionar_fila(url)

        print(f"\nUrl analisada com Sucesso!: {resultado}")

        return jsonify(resultado)

# condicional para rodar a aplicação
if __name__ == "__main__":
    app.run(debug=True)
    