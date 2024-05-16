// Função para fechar aba promocional

let promo = document.getElementById('sessao_promocao');
let fechar = document.getElementById('fechar_prom');
fechar.addEventListener('click', () => close(promo));

function close(vari) {
    vari.style.display = "none";
}



// TIMER