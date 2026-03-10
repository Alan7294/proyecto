const url = "http://127.0.0.1:8000/nota"

const contenedor = document.getElementById('data')

function cargarNotas(){

fetch(url)

.then(response => response.json())

.then(datos => {

let resultado = ""

datos.forEach(nota => {

resultado += `

<li>

<p><b>ID Nota:</b> ${nota.id_nota}</p>
<p><b>ID Inscripción:</b> ${nota.id_inscripcion}</p>
<p><b>Nota:</b> ${nota.nota}</p>
<p><b>Fecha Registro:</b> ${nota.fecha_registro}</p>
<p><b>ID Docente:</b> ${nota.id_docente}</p>

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

cargarNotas()