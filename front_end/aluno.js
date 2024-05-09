// Função para criar um timer na section promoção
//var  temp = nome_variável = setTimout(timer, );


// Função para fechar aba promocional

let promo = document.getElementById('sessao_promocao');
let fechar = document.getElementById('fechar_prom');
fechar.addEventListener('click', () => close(promo));

function close(vari) {
    vari.style.display = "none";
}