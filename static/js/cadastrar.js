// Selecionando elementos que serão verificados

console.log("Cadastrar.js")
const senha = document.querySelector("#senha")
const senhaRepetida = document.querySelector("#senha-repetida")
const form = document.querySelector("form")
const mensagensErro = {
    mensagemSenhas: document.querySelector("#mensagem-senhas"),
    mensagemSenhaFraca: document.querySelector("#mensagem-senha-fraca"),
    mensagemNome: document.querySelector("#mensagem-nome")
}

const regexNome = /^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$/;
const regexSenha = /(?=^.{8,}$)((?=.*\d)(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$/g


// Adicionando função para executrar quando o form for submetido. Caso alguma validação não passe a submissão não irá acontecer.
form.addEventListener("submit", (e) => {
    // verificando se a senhas são iguais
    if (senha.value !== senhaRepetida.value) {
        e.preventDefault()
        mensagensErro.mensagemSenhas.hidden = false
    }
    else {
        mensagensErro.mensagemSenhas.hidden = true
    } 

    // Verificando se a senha é fraca
    if (!regexSenha.test(senha.value)) {
        e.preventDefault()
        mensagensErro.mensagemSenhaFraca.hidden = false
    }
    else {
        mensagensErro.mensagemSenhaFraca.hidden = true
    }

    // Verificando se o nome é válido
    if (!regexNome.test(nome.value)) {
        e.preventDefault()
        mensagensErro.mensagemNome.hidden = false
    }
    else {
        mensagensErro.mensagemNome.hidden = true
    }

})

// Função para alterar visibilidade da senha quando o icone for clicado
function alterarVisibilidadeSenha(olho) {
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
