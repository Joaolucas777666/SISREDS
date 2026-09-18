// Função para verificar o status do backend utilizando fetch
//  e async/await que significa que a função é assíncrona e 
// pode usar await para esperar por Promises
async function verificarBackend() {

     try {

// Faz uma requisição para o Flask, o fetch retorna uma Promise, então usamos await para esperar a resposta
const resposta= await fetch("http://127.0.0.1:5000/api/status");

// Converte a resposta para JSON
const dados = await resposta.json();

// Mostra os dados no console
console.log(dados);

// Atualiza o conteúdo do elemento com o ID "status" com o status do backend
// utilizando método get ElementById para selecionar o elemento e textContent para definir o texto
document.getElementById("status").textContent =
     "Backend " + dados.status + " Estamos de olho...👀";
     
     // Se houver algum erro na requisição, exibe uma mensagem de erro
     } catch (erro) {
        document.getElementById("status").textContent =
        "🔴 Backend não está disponível";
        console.error("Erro ao verificar o backend:", erro);
     }
}


// FUNÇÃO PARA BUSCAR O RESULTADO DA ANÁLISE

// Função assíncrona porque vamos esperar
// o Chrome retornar os dados armazenados.
async function mostrarResultado() {
     // Busca no armazenamento local da extensão
    // o dado que foi salvo pelo background.js.
    // "resultadoAnalise" é o nome que usamos
    // no background.js para guardar o resultado.
    // e urlAnalisada é o nome que usamos 
    // para guardar a url  
    const dados = await chrome.storage.local.get(["resultadoAnalise", "urlAnalisada"]);

     // Mostra no console tudo que foi encontrado
     console.log(">>> RESULTADO ARMAZENADO:", dados);

     if (!dados.resultadoAnalise){

          console.log("Nenhum resultado de análise encontrado.");

          return;
     }

     // seleciona o botão "Ver detalhes"
     const btnDetalhes = document.getElementById("btnDetalhes");

     // Por padrão, o botão fica escondido.
    //  Ele só será mostrado se a página for
    // suspeita ou maliciosa.
    btnDetalhes.hidden = true

     // Remove qualquer tema anterior. 
     document.body.classList.remove(
          "tema-legitimo",
          "tema-suspeita",
          "tema-maliciosa"
     );

// Verifica se a classificação é maliciosa.
if (dados.resultadoAnalise.classificacao === "Maliciosa") {

     // deixa o tema de acordo com a classificação maliciosa
     document.body.classList.add("tema-maliciosa");

    // Exibe o alerta para o usuário.
    document.getElementById("resultado").textContent =
        "🔴 Atenção! Foi identificada uma possível ameaça nesta página.";

}

// Verifica se a classificação é suspeita.
else if (dados.resultadoAnalise.classificacao === "Suspeita") {

     // deixa o tema de acordo com a classificação suspeita
     document.body.classList.add("tema-suspeita");

    // Exibe o alerta para o usuário.
    document.getElementById("resultado").textContent =
        "🟡 Atenção! Esta página apresenta características suspeitas.";
}

// Verifica se a classificação é legítima.
else {

    // deixa o tema de acordo com a classificação legítima 
    document.body.classList.add("tema-legitima");

}
// Se for Maliciosa ou Suspeita, mostra o botão.
if (
    dados.resultadoAnalise.classificacao === "Maliciosa" ||
    dados.resultadoAnalise.classificacao === "Suspeita"
) {

    // Seleciona o botão "Ver detalhes".
    const btnDetalhes =
        document.getElementById("btnDetalhes");

    // Mostra o botão.
    btnDetalhes.hidden = false;

    // Quando o usuário clicar no botão...
    btnDetalhes.addEventListener("click", () => {

        // Mostra a URL analisada.
        document.getElementById("urlAnalisada").textContent =
            "URL analisada: " + dados.urlAnalisada;

        // Mostra a área de detalhes.
        document.getElementById("detalhes").hidden = false;

        // Esconde o botão depois de clicar.
        btnDetalhes.hidden = true;
    });
}

}





// executa a função quando o popup é aberto
verificarBackend();
mostrarResultado();

