import { api_autenticar } from "/js/conexao/server_const.js"


document.addEventListener('DOMContentLoaded', function() {
    
    fetch(`${api_autenticar}/aluno`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(
        response => {

            if(response.status == 200){

                window.location.href = "/pages/index.html";
            }
            if (!response.ok) {
                
                
                throw new Error('Erro ao enviar dados');
            }
    })
    .catch(error => console.error('Error:', error));
})