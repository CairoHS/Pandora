document.addEventListener('DOMContentLoaded', function() {
    
    fetch('/get/aluno', {
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
                    window.location.href = "/login.html";
                }
                throw new Error('Erro ao enviar dados');
            }
    })
    .catch(error => console.error('Error:', error));
})