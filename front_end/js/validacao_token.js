import { api_autenticar } from "/js/conexao/server_const"

document.addEventListener('DOMContentLoaded', function() {
    
    fetch(`${api_autenticar}/aluno`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(
        response => {
            console.log(response.status)
            if (!response.ok) {
                
                if(response.status == 401 || response.status == 403){
                    window.location.href = "/login";
                }
                throw new Error('Erro ao enviar dados');
            }
    })
    .catch(error => console.error('Error:', error));
})