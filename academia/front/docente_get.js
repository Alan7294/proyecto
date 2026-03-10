const url = "http://127.0.0.1:8000/docente"

const contenedor = document.getElementById('data')

function cargarDocentes(){

fetch(url)

.then(response => response.json())

.then(datos => {

let resultado=""

datos.forEach(docente => {

resultado+=`

<li>

<p><b>ID Docente:</b> ${docente.id_docente}</p>
<p><b>ID Persona:</b> ${docente.id_persona}</p>
<p><b>ID Especialidad:</b> ${docente.id_especialidad}</p>

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

cargarDocentes()