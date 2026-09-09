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
     "🟢 Backend " + dados.status;
     
     // Se houver algum erro na requisição, exibe uma mensagem de erro
     } catch (erro) {
        document.getElementById("status").textContent =
        "🔴 Backend não está disponível";
        console.error("Erro ao verificar o backend:", erro);
     }
}

// executa a função quando o popup é aberto
verificarBackend(); 