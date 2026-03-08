const url = "http://127.0.0.1:8000/inscripcion";

const formularioData = document.forms['formularioData'];
const id_alumno = document.getElementById('id_alumno');
const id_clase = document.getElementById('id_clase');
const fecha_inscripcion = document.getElementById('fecha_inscripcion');

formularioData.addEventListener('submit', (e) => {
    e.preventDefault();

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            id_alumno: id_alumno.value,
            id_clase: id_clase.value,
            fecha_inscripcion: fecha_inscripcion.value
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
