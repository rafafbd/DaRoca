function addProduto(nomeDoProduto) {
    let quantidadeInput = document.getElementById("'quanto-" + nomeDoProduto+"'").value;
    let quantidade = parseInt(quantidadeInput.value) || 1; //isso faz com que se nenhuma quantidade for selecionada adicionar só 1
    console.log(quantidadeInput)
    let produtosDaCesta = JSON.parse(localStorage.getItem('produtosCesta')) || [];
    // a linha acima recupera os produtos existentes ou inicia uma nova lista

    let index = produtosDaCesta.findIndex(produto => produto.nome === nomeDoProduto);
    if (index !== -1) {
        produtosDaCesta[index].quantidade += quantidade;
        // se o produto ja foi adicionado a lista só vai atualizar a quantidade ex:
        //peguei 2kg de batata mas vou pegar mais 2
        //ent aqui no codigo ao inves de aparecer 2 e outro de 2 vai aparecer como 4 kg de batata

    } 
    else {
        produtosDaCesta.push({ nome: nomeDoProduto, quantidade: quantidade });
    }
    localStorage.setItem('produtosCesta', JSON.stringify(produtosDaCesta));
    //vai salvar a lista ja com as novas modificaçoes no localStorage

    quantidadeInput.value =' '; //zera o campo de quantidade

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
