
function buscaProdutos(){
    fetch('http://localhost:3000/produtos')
        .then(resposta =>{
            return resposta.json()
        })
        .then( (dados) =>{
            exibeProdutos(dados);
        })
}

function exibeProdutos(produtos){
    console.log("oi")
    let prod = "";
    let tipo;
    for (let i=0; i<produtos.length; i++){
        switch(produtos[i].categoria){
            case 1:
                tipo = 'legume';
                break;
            case 2:
                tipo =  'fruta';
                break
            case 3:
                tipo = 'verdura';
        }
    prod += 
        "<div class='produto "+tipo+ "'>"+
            "<img src='/imagens/" +produtos[i].imagem+ "' alt='' class='imagem-produto'>"+
            "<div class='produto-info'>"+
                "<p>NOME: "+produtos[i].nome+"</p>"+
                "<p>PREÇO: "+produtos[i].valor.toFixed(2).replace(".", ",")+"R$</p>"+
            "</div>"+
            "<div class='container-adicionar'>"+
            "<button class='botao-adicionar' onclick='addProduto(\"" + produtos[i].nome + "\")'>Adicionar na cesta</button>" +
            "<input type='number' class='quantos-itens' id ='quanto-"+produtos[i].nome+"'>"+
            `</div>
        </div>`
}

document.querySelector("#display-produtos").innerHTML = prod;
}

buscaProdutos()
