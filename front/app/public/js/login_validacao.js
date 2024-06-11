import { api_autenticar } from "/js/conexao/server_const.js"

let botao = document.querySelector("#botao");
botao.addEventListener('click', (e) => validacao_login(e))


function validacao_login(e){

    e.preventDefault();
    let login = document.getElementById('login').value;
    let senha = document.getElementById('senha').value;

    fetch(`${api_autenticar}/login`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({login: login, senha: senha})
    })
    .then(
        response => {
            if (!response.ok) {
                throw new Error('Erro ao enviar dados');
            }

            if(response.status == 200) {
                window.location.href = "pages/index.html";
            }

            return response.json()
    })
    .then(
        data => {
            // Faça algo com a resposta do servidor, se necessário
            //console.log('Resposta do servidor:', data);
            //console.log('Status:', status_response);

            //status 200 é que a resposta chegou bem
            
    })
    .catch(error => console.error('Error:', error));
}

