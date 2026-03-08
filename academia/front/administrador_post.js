const url = "http://127.0.0.1:8000/administrador";

const formularioData = document.forms['formularioData'];
const id_persona = document.getElementById('id_persona');

formularioData.addEventListener('submit', (e) => {
    e.preventDefault();

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            id_persona: id_persona.value
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log("Respuesta del servidor:", data);
    })
    .catch(error => {
        console.log("Error:", error);
    });
});
