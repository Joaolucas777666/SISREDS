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