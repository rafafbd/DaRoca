function verificaForm(Nome, Email, Senha, confirma){
    let nome = Nome;
    let email = Email
    let senha = Senha
    let confirmaSenha = confirma
    if (nome == "" || email == "" || senha ==  "" || confirmaSenha == "") {
        alert("Preencha todos os campos para se inscrever.")
        return false
    }
    if (senha != confirmaSenha){
        alert("Senha incorreta.");
        return false
    }
    
    return true
}

function cadastro(){
    let senha = document.getElementById("senha").value
    let confirmaSenha = document.getElementById("confirm").value
    let nome = document.getElementById("nome").value
    let email = document.getElementById("email").value
    if (verificaForm(nome, email, senha, confirmaSenha)){
        alert("Cadastrado com sucesso")
    }
}
