// ==============================
// MÓDULO DE URL
// ==============================

// Mostra uma mensagem no console para indicar que o script foi carregado com sucesso
console.log("SISREDS carregado com sucesso na página!");

// Obtém a URL atual da página
const urlAtual = window.location.href;

// Mostra a URL atual no console
console.log("URL atual:", urlAtual);

// envia a URL para o background.js para que ele possa enviar para o Flask
chrome.runtime.sendMessage({ 
tipo: "url",
url: urlAtual
})

// ==============================
// MÓDULO DE FAKE NEWS
// ==============================

// Captura todo o texto visível da página
const textoPagina = document.body.innerText;

// divide o texto em linhas
const linhas = textoPagina.split("\n");

console.log("Quantidade de linhas:", linhas.length);

// Analisa cada linha capturada
linhas.forEach((linha, indice) => {

    // Remove espaços desnecessários do começo e do fim
    const texto = linha.trim();

    // Ignora linhas vazias
    if (texto.length === 0) {
        return;
    }

    // Divide o texto em palavras
    const palavras = texto.split(" ");

    // Mostra o número da linha, caracteres, palavras e conteúdo
    console.log(
        indice,
        "| caracteres:", texto.length,
        "| palavras:", palavras.length,
        "| texto:", texto
    );
});

// Mostra o texto capturado no console
console.log("Texto capturado:");
console.log(textoPagina);

// ==============================
// MOSTRA ALERTA
// ==============================

// cria um alerta visual 
function mostrarAlerta(){
        // criando elemento html <div>
    const alerta = document.createElement("div");
    // colocando id na div: vai ficar assim
    //  <div id="alerta-sisreds"></div>
    alerta.id = "alerta-sisreds";

    // colocando texto dentro do alerta
    alerta.innerHTML = `
        <strong>⚠️ SISREDS identificou uma possível ameaça.</strong>
        <br><br>
        <p>Clique no ícone da extensão para mais informações.</p>

        <button id="fechar-alerta">Entendi</button>
    `;
    
    // Estilo do alerta
    alerta.style.position = "fixed";
    alerta.style.top = "17%";
    alerta.style.left = "50%";
    alerta.style.transform = "translate(-50%, -50%)";

    alerta.style.width = "400px";
    alerta.style.padding = "20px";

    alerta.style.background = "rgba(0, 0, 0, 5)";
    alerta.style.color = "white";

    alerta.style.borderRadius = "15px";

    alerta.style.textAlign = "center";

    alerta.style.zIndex = "2147483647";

    alerta.style.fontFamily = "Arial, sans-serif";

    // Adiciona o alerta à página
    document.body.appendChild(alerta);

    // Seleciona o botão Fechar
    const btnFechar = document.getElementById("fechar-alerta");

    // Estilo do botão
    btnFechar.style.position = "relative";
    btnFechar.style.zIndex = "2147483647";
    btnFechar.style.pointerEvents = "auto";
    btnFechar.style.marginTop = "10px";
    btnFechar.style.padding = "8px 18px";
    btnFechar.style.border = "none";
    btnFechar.style.borderRadius = "10px";
    btnFechar.style.background = "white";
    btnFechar.style.color = "#000000";
    btnFechar.style.fontWeight = "bold";
    btnFechar.style.cursor = "pointer";
    btnFechar.style.fontSize = "14px";
    btnFechar.style.transition = "0.2s";

    // Efeito ao passar o mouse
    btnFechar.addEventListener("mouseenter", () => {
    btnFechar.style.transform = "scale(1.05)";
        });

    btnFechar.addEventListener("mouseleave", () => {
    btnFechar.style.transform = "scale(1)";
    });

    // Quando o botão for clicado
    btnFechar.addEventListener("click", () => {

    // Remove o alerta
    alerta.remove();

    });
}


// Escuta mensagens enviadas pelo background.js
chrome.runtime.onMessage.addListener((mensagem) => {

    // Verifica se a mensagem é do tipo "mostrar-alerta"
    if (mensagem.tipo === "mostrar-alerta") {

        // Mostra o alerta na página
        mostrarAlerta();
    }
})