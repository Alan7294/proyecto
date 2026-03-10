const url = "http://127.0.0.1:8000/inscripcion"

const contenedor = document.getElementById('data')

function cargarInscripciones(){

fetch(url)

.then(response => response.json())

.then(datos => {

let resultado=""

datos.forEach(inscripcion => {

resultado += `

<li>

<p><b>ID Inscripción:</b> ${inscripcion.id_inscripcion}</p>
<p><b>ID Alumno:</b> ${inscripcion.id_alumno}</p>
<p><b>ID Clase:</b> ${inscripcion.id_clase}</p>
<p><b>Fecha:</b> ${inscripcion.fecha_inscripcion}</p>

<hr>

</li>

`

})

contenedor.innerHTML = resultado

})

.catch(error => {

console.log(error)

})

}

cargarInscripciones()