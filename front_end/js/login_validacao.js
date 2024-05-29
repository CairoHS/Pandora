function validacao_login(){
    var inplogin = document.getElementById('login')
    var inpsenha = document.getElementById('senha')
    var login = inplogin.value
    var senha = inpsenha.value

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({login: login, senha: senha})
    })
    .then(response => response.json())
    .catch(error => console.error('Error:', error));
}
