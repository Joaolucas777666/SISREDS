// Teste do background.js
// Mostra uma mensagem no console quando o arquivo é carregado.
console.log("SISREDS: background.js carregado com sucesso!");


// Escuta mensagens enviadas por outras partes da extensão,
// como o content.js.
chrome.runtime.onMessage.addListener(async (mensagem) => {

    // Mostra no console a mensagem que foi recebida.
    // Isso permite verificar se o content.js conseguiu
    // enviar a mensagem para o background.js.
    console.log(">>> BACKGROUND RECEBEU UMA MENSAGEM <<<");
    console.log("Mensagem recebida:", mensagem);


    // Verifica se o tipo da mensagem recebida é "url".
    // O content.js envia a mensagem com tipo: "url".
    if (mensagem.tipo === "url") {

        // Informa no console que uma URL foi recebida
        // e que será enviada para o servidor Flask.
        console.log(">>> É uma URL! Enviando para o Flask...");


        // Faz uma requisição HTTP para o Flask. Por isso usa o metodo fetch.
        // Usa o aiwait para esperar a resposta do Flask antes de continuar a execução do código.
        // O método POST será utilizado para enviar a URL
        // para o endpoint /api/analisar-url.
        const resposta = await fetch(
            "http://127.0.0.1:5000/api/analisar-url",
            {

                // Define o método da requisição.
                method: "POST",

                // Define os cabeçalhos da requisição.
                headers: {

                    // Informa ao Flask que os dados enviados
                    // estão no formato JSON.
                    "Content-Type": "application/json"
                },

 
                // Define os dados que serão enviados para o Flask.
                // nesse caso, a URL que foi recebida do content.js.
                // O JSON.stringify converte o objeto JavaScript em uma string JSON.
                body: JSON.stringify({

                    // Cria o campo "url" no JSON.
                    // mensagem.url contém a URL recebida
                    // anteriormente pelo content.js.
                    url: mensagem.url
                })
            }
        );


        // Mostra no console que o Flask respondeu
        // à requisição enviada pelo background.js.
        console.log(">>> Flask respondeu!");


        // Converte a resposta recebida do Flask
        // para um objeto JavaScript no formato JSON.
        const dados = await resposta.json();


        // Mostra no console os dados retornados pelo Flask.
        console.log("Dados recebidos do Flask:", dados);
    }
});