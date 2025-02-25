// Função para alterar visibilidade da senha quando o ícone for clicado
function alterarVisibilidadeSenha(olho) {
    const senha = document.querySelector("#senha")
    if (senha.type === "password") {
        senha.type = "text"
        olho.className = "fa-solid fa-eye"
    }
    else {
        senha.type = "password"
        olho.className = "fa-solid fa-eye-slash"
    }
}
