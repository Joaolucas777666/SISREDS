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
        <p>Clique no ícone da extensão para mais informações.</p>
    `;

    // Estilo do alerta
    alerta.style.position = "fixed";
    alerta.style.top = "10%";
    alerta.style.left = "50%";
    alerta.style.transform = "translate(-50%, -50%)";

    alerta.style.width = "350px";
    alerta.style.padding = "20px";

    alerta.style.background = "rgba(120, 0, 0, 0.95)";
    alerta.style.color = "white";

    alerta.style.borderRadius = "20px";

    alerta.style.textAlign = "center";

    alerta.style.zIndex = "999999";

    alerta.style.fontFamily = "Arial, sans-serif";

    document.body.appendChild(alerta);
}

// executar função alerta
mostrarAlerta();