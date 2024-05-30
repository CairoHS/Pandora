function validacao_login(e){

    e.preventDefault();
    let login = document.getElementById('login').value;
    let senha = document.getElementById('senha').value;

    fetch('/login', {
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

            status_response = response.status;

            return response.json()
    })
    .then(
        data => {
            // Faça algo com a resposta do servidor, se necessário
            //console.log('Resposta do servidor:', data);
            //console.log('Status:', status_response);

            //status 200 é que a resposta chegou bem
            if(status_response == 200) {
                window.location.href = "pages/index.html";
            }
    })
    .catch(error => console.error('Error:', error));
}

let botao = document.querySelector("#botao");
botao.addEventListener('click', (e) => validacao_login(e))