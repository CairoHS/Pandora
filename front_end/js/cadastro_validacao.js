function validacao_cadastro(e){
    e.preventDefault();
    let nome = document.getElementById('nome').value;
    let sobrenome = document.getElementById('sobrenome').value;
    let email = document.getElementById('email').value;
    let login = document.getElementById('login').value;
    let senha = document.getElementById('senha').value;


    fetch('/cadastro', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({login: login, senha: senha, nome: nome, sobrenome:sobrenome, email: email})
    })
    .then(
        response => {
            if (!response.ok) {
                throw new Error('Erro ao enviar dados');
            }
            response_status = response.status;
            return response.json()
    })
    .then(
        data => {
            // Faça algo com a resposta do servidor, se necessário
            console.log('Resposta do servidor:', data);
            console.log('Status:', response_status);         
    })
    .catch(error => console.error('Error:', error));
    
}

let botao = document.querySelector("#botao");
botao.addEventListener('click', (e) => validacao_cadastro(e))