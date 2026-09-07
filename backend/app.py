#importando o flask e o render_template para renderizar o html
#  e jsonify para retornar json e cors para permitir requisições de outros domínios
from flask import Flask, render_template, jsonify, request 
from flask_cors import CORS

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
def api_status():
    # retornando um json com o status da API
    return jsonify({"status": "Online!",
                    "Sistema": "SISREDS"
                    })

# criando rota para analisar a url
@app.route("/api/analisar-url", methods=["POST"])
def analisar_url():
        # obtendo a url do corpo da requisição
        dados = request.get_json()
        url = dados["url"]

        # imprimindo a url recebida no console do terminal
        print(f"URL recebida: {url}")

        # retornando um json com a url recebida
        return jsonify({
        "mensagem": "URL recebida com sucesso!",
        "url": url
        })


# condicional para rodar a aplicação
if __name__ == "__main__":
    app.run(debug=True)
    