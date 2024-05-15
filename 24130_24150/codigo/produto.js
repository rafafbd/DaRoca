
produtos = [
    {nome: "Banana", unidade: "cachos", precoPorUnidade: 1.50, classificacao: "fruta"}
]

function addProduto(nome, quantidade){
    let quanto = document.querySelector("#quanto-"+nome).value;
    localStorage.setItem(nome, quanto)
}
