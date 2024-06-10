
// var produtos = [
//     {nome: "Banana", unidade: "cachos", precoPorUnidade: 1.50, classificacao: "fruta"},
//     {nome: "Brócolis", unidade: "kg", precoPorUnidade: 16.82, classificacao: "verdura"},
//     {nome: "Cenoura", unidade: "kg", precoPorUnidade: 3.99, classificacao: "legume"},
//     {nome: "Alface", unidade: "unidade", precoPorUnidade: 2.25, classificacao: "verdura"},
//     {nome: "Tomate", unidade: "kg", precoPorUnidade: 5.75, classificacao: "fruta"},
//     {nome: "Batata", unidade: "kg", precoPorUnidade: 2.50, classificacao: "legume"},
//     {nome: "Pepino", unidade: "kg", precoPorUnidade: 4.20, classificacao: "fruta"},
//     {nome: "Abobrinha", unidade: "kg", precoPorUnidade: 6.30, classificacao: "legume"},
//     {nome: "Espinafre", unidade: "kg", precoPorUnidade: 9.10, classificacao: "verdura"}
// ]

function obtemPreco(nomeProd){
    let quantidade = parseInt(localStorage.getItem(nomeProd));
    let preco;
    for (let i=0; i < produtos.length; i++){
        if (produtos[i].nome == nomeProd){
            preco = produtos[i].precoPorUnidade
        }
    }
    return quantidade * preco
}

function dadosDoProduto(){
    
    //aqui pegamos a lista que foi colocada no localStorage
    var produtosDaCesta = JSON.parse(localStorage.getItem('produtosCesta'));
    var precoTotalTodosProdutos = 0.0;
    console.log(JSON.parse(localStorage.getItem('produtosCesta')))
    var cesta = "<table>";
    cesta += "<tr><th>Nome</th><th>Quantidade</th><th>Preço total</th><tr>";

    produtosDaCesta.forEach(function(produto) {
        var precoTotal = obtemPreco(produto.nome);
        precoTotalTodosProdutos += precoTotal;
        cesta += "<tr><td>"+produto.nome+"</td>"+
                                    "<td>quantidade:" +produto.quantidade+ "</td>"+
                                    "<td> Preço total:R$" + precoTotal.toFixed(2) + "</td></tr>";
    });

            cesta += "<tr><td colspan='2'>Total</td><td>R$ "+precoTotalTodosProdutos.toFixed(2)+"</td></tr>";
    cesta +="</table>"
    document.querySelector("#pedido").innerHTML = cesta;
}

dadosDoProduto()
