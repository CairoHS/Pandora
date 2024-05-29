function validacao_cadastro(){
    var inpnome = document.getElementById('nome').innerHTML
    var inpsobrenome = document.getElementById('sobrenome').innerHTML
    var inpemail = document.getElementById('email').innerHTML
    var inplogin = document.getElementById('login').innerHTML
    var inpsenha = document.getElementById('senha').innerHTML

    var nome  = inpnome.value
    var sobrenome = inpsobrenome.value
    var email = inpemail.value
    var login = inplogin.value
    var senha = inpsenha.value
    
    fetch('/cadastro', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({login: login, senha: senha, nome: nome, sobrenome:sobrenome, email: email})
    })
    
    .then(response => response.json())
    .catch(error => console.error('Error:', error));
    
}