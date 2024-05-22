
var produtos = [
    {nome: "Banana", unidade: "cachos", precoPorUnidade: 1.50, classificacao: "fruta"},
    {nome: "Brócolis", unidade: "kg", precoPorUnidade: 16.82, classificacao: "verdura"},
    {nome: "Cenoura", unidade: "kg", precoPorUnidade: 3.99, classificacao: "legume"},
    {nome: "Alface", unidade: "unidade", precoPorUnidade: 2.25, classificacao: "verdura"},
    {nome: "Tomate", unidade: "kg", precoPorUnidade: 5.75, classificacao: "fruta"},
    {nome: "Batata", unidade: "kg", precoPorUnidade: 2.50, classificacao: "legume"},
    {nome: "Pepino", unidade: "kg", precoPorUnidade: 4.20, classificacao: "fruta"},
    {nome: "Abobrinha", unidade: "kg", precoPorUnidade: 6.30, classificacao: "legume"},
    {nome: "Espinafre", unidade: "kg", precoPorUnidade: 9.10, classificacao: "verdura"}
]

function obtemPreco(nomeProd){
    let quantidade = localStorage.getItem(nomeProd);
    let preco;
    for (let i=0; i < produtos.length(); i++){
        if (produtos[í].nome == nomeProd){
            preco = produto[i].precoPorUnidade
        }
    }
    return quantidade * preco
}
