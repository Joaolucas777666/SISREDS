// Teste de background.js

console.log("SISREDS: background.js carregado com sucesso!");

// Escuta mensagens enviadas por outras partes da extensão
chrome.runtime.onMessage.addListener(async (mensagem) => {

    // Mostra a mensagem recebida no console
    console.log("Mensagem recebida:", mensagem);

    // Se a mensagem for do tipo "url", envia a URL para o Flask
    if (mensagem.tipo === "url") {

        // Faz uma requisição POST para o Flask com a URL recebida
        const resposta = await fetch(
            "http://127.0.0.1:5000/api/analisar-url",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    url: mensagem.url
                })
            }
        );

        // Converte a resposta do Flask para JSON
        const dados = await resposta.json();

        // Mostra os dados recebidos do Flask no console
        console.log("Dados recebidos do Flask:", dados);
    }

});