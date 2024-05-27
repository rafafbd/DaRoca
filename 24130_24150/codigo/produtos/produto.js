
var produtos = [
    {nome: "Banana", unidade: "cachos", precoPorUnidade: 1.50, classificacao: "fruta"},
    {nome: "Brócolis", unidade: "kg", precoPorUnidade: 16.82, classificacao: "verdura"},
    {nome: "Cenoura", unidade: "kg", precoPorUnidade: 3.99, classificacao: "legume"},
    {nome: "Alface", unidade: "unidade", precoPorUnidade: 2.25, classificacao: "verdura"},
    {nome: "Tomate", unidade: "kg", precoPorUnidade: 5.75, classificacao: "fruta"},
    {nome: "Batata", unidade: "kg", precoPorUnidade: 2.50, classificacao: "legume"},
    {nome: "Pepino", unidade: "kg", precoPorUnidade: 4.20, classificacao: "fruta"},
    {nome: "Abobrinha", unidade: "kg", precoPorUnidade: 6.30, classificacao: "legume"},
    {nome: "Espinafre", unidade: "kg", precoPorUnidade: 9.10, classificacao: "verdura"},
    {nome: "Maçã", unidade: "kg", precoPorUnidade: 3.00, classificacao: "fruta"},
    {nome: "Pêra", unidade: "kg", precoPorUnidade: 3.50, classificacao: "fruta"},
    {nome: "Manga", unidade: "unidade", precoPorUnidade: 1.20, classificacao: "fruta"},
    {nome: "Uva", unidade: "kg", precoPorUnidade: 7.80, classificacao: "fruta"},
    {nome: "Melancia", unidade: "kg", precoPorUnidade: 0.99, classificacao: "fruta"},
    {nome: "Abacaxi", unidade: "unidade", precoPorUnidade: 3.00, classificacao: "fruta"},
    {nome: "Couve", unidade: "unidade", precoPorUnidade: 1.80, classificacao: "verdura"},
    {nome: "Pimentão", unidade: "kg", precoPorUnidade: 4.50, classificacao: "legume"},
    {nome: "Berinjela", unidade: "kg", precoPorUnidade: 5.00, classificacao: "legume"},
    {nome: "Cebola", unidade: "kg", precoPorUnidade: 2.20, classificacao: "legume"},
    {nome: "Alho", unidade: "kg", precoPorUnidade: 15.00, classificacao: "legume"},
    {nome: "Laranja", unidade: "kg", precoPorUnidade: 2.00, classificacao: "fruta"},
    {nome: "Limão", unidade: "kg", precoPorUnidade: 3.00, classificacao: "fruta"},
    {nome: "Mamão", unidade: "kg", precoPorUnidade: 2.50, classificacao: "fruta"},
    {nome: "Couve-flor", unidade: "kg", precoPorUnidade: 7.00, classificacao: "verdura"},
    {nome: "Repolho", unidade: "kg", precoPorUnidade: 3.00, classificacao: "verdura"},
    {nome: "Milho", unidade: "unidade", precoPorUnidade: 1.00, classificacao: "legume"},
    {nome: "Ervilha", unidade: "kg", precoPorUnidade: 4.50, classificacao: "legume"},
    {nome: "Feijão", unidade: "kg", precoPorUnidade: 5.50, classificacao: "legume"},
    {nome: "Cacau", unidade: "kg", precoPorUnidade: 10.00, classificacao: "fruta"}
];

function addProduto(nome){
    let quanto = document.querySelector("#quanto-"+nome).value;
    localStorage.setItem(nome, quanto);
}


function pesquisaTipo(tipo){
    console.log(tipo);
    const produtos = document.querySelectorAll(".produto");
    for (let i = 0; i < produtos.length; i++) {
        produtos[i].style.display = 'none';
    }

    const prodTipo = document.querySelectorAll("."+tipo);
    for (let i = 0; i < prodTipo.length; i++) {
        prodTipo[i].style.display = 'flex';
    }
    
    const nav = document.querySelectorAll(".tipo-produto");
    for (let i = 0; i < nav.length; i++) {
        nav[i].style.backgroundColor = '';
        nav[i].style.borderBottom = '';
    }

    document.getElementById("tipo-"+tipo).style.backgroundColor = 'lightgray';
    document.getElementById("tipo-"+tipo).style.borderBottom = '3px solid rgb(255, 116, 13)';
}
