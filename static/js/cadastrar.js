// Função para pegar o token CSRF
function getCSRFToken() {
    return document.querySelector('input[name="csrfmiddlewaretoken"]').value;
}

const mensagensErro = {
    mensagemEmail: document.querySelector("#mensagem-email"),
    mensagemSenhas: document.querySelector("#mensagem-senhas"),
    mensagemSenhaFraca: document.querySelector("#mensagem-senha-fraca"),
    mensagemNome: document.querySelector("#mensagem-nome"),
}

async function enviarForm() {
    // Pegando valores dos inputs e colocando em um objeto
    let formBody = {
        'email': document.querySelector("#email").value,
        'nome': document.querySelector("#nome").value,
        'senha': document.querySelector("#senha").value,
        'senhaRepetida': document.querySelector("#senha-repetida").value
    }
    
    // Enviando requisição POST para o servidor
    await fetch("/cadastrar/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken()
        },
        body: JSON.stringify(formBody)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        if (!data["sucesso"]) {
            // Caso alguma validação tenha falhado, as mensagem de erro correspondente será exibida
            mensagensErro.mensagemEmail.hidden = data["emailCadastrado"] ? false : true
            mensagensErro.mensagemNome.hidden = data["nomeInvalido"] ? false : true
            mensagensErro.mensagemSenhas.hidden = data["senhasDiferentes"] ? false : true
            mensagensErro.mensagemSenhaFraca.hidden = data["senhaFraca"] ? false : true
        }
        else {
            // Recarregando a página caso o cadastro tenha sido bem sucedido. Escolhi por recarregar a pagina e não apenas mostrar a mensagem porque isso me parece mais intuitivo ao usuário
            location.reload()
        }
    })
}

// Adicionando evento para que quando o form for submetido a função "enviarForm()"  seja chamada
const form = document.querySelector("form")
form.addEventListener("submit", (e) => {
    e.preventDefault()
    enviarForm()
})



// Função para alterar visibilidade da senha quando o ícone for clicado
function alterarVisibilidadeSenha(olho) {
    const senha = document.querySelector("#senha")
    const senhaRepetida = document.querySelector("#senha-repetida")
    if (senha.type === "password") {

        senha.type = "text"
        senhaRepetida.type = senha.type
        olho.className = "fa-solid fa-eye"
    }
    else {
        senha.type = "password"
        senhaRepetida.type = senha.type
        olho.className = "fa-solid fa-eye-slash"
    }
    
}
