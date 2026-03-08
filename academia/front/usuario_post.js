const url = "http://127.0.0.1:8000/usuario";

const formularioData = document.forms['formularioData'];
const id_persona = document.getElementById('id_persona');
const nombre_usuario = document.getElementById('nombre_usuario');
const contraseña = document.getElementById('contraseña');
const id_tipo = document.getElementById('id_tipo');

formularioData.addEventListener('submit', (e) => {
    e.preventDefault();

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            id_persona: id_persona.value,
            nombre_usuario: nombre_usuario.value,
            contraseña: contraseña.value,
            id_tipo: id_tipo.value
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
