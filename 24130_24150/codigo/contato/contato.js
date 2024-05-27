

function apagar(){
    console.log("A função apagar foi chamada")
    document.getElementById("icon-ruim").style.background = '';
    document.getElementById("icon-neutro").style.background = '';
    document.getElementById("icon-bom").style.background = '';
}

function glow(aval){
    apagar()
    console.log("teste 2")
    let cor;
    switch (aval){
        case "ruim":
            cor = "coral"
            break
        case "neutro":
            cor = "goldenrod"
            break
        case "bom":
            cor = "lightgreen"
    }
    let gradiente = 'radial-gradient('+cor+', #013C31)';
    document.getElementById("icon-"+aval).style.background = gradiente;
}

document.getElementById("ruim").addEventListener("click", function() {
    glow("ruim");
});

document.getElementById("neutro").addEventListener("click", function() {
    glow("neutro");
});

document.getElementById("bom").addEventListener("click", function() {
    glow("bom");
});