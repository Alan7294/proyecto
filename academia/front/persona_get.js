const url = "http://127.0.0.1:8000/persona"

const contenedor = document.getElementById('data')
const buscador = document.getElementById('buscador')

let personas = []

function mostrarPersonas(datos){

let resultado = ""

datos.forEach(persona => {

resultado += `
<li>

<p><b>ID:</b> ${persona.id_persona}</p>
<p><b>Nombre:</b> ${persona.nombre_persona}</p>
<p><b>Apellido Paterno:</b> ${persona.apellido_pat}</p>
<p><b>Apellido Materno:</b> ${persona.apellido_mat}</p>
<p><b>CI:</b> ${persona.ci}</p>
<p><b>Correo:</b> ${persona.correo}</p>
<p><b>Fecha Nacimiento:</b> ${persona.fecha_nacimiento}</p>

<hr>

</li>
`

})

contenedor.innerHTML = resultado

}

function cargarPersonas(){

fetch(url)

.then(response => response.json())

.then(data => {

personas = data
mostrarPersonas(personas)

})

.catch(error => console.log(error))

}

buscador.addEventListener("keyup", () => {

let texto = buscador.value.toLowerCase()

let filtrados = personas.filter(p =>

p.nombre_persona.toLowerCase().includes(texto) ||
String(p.ci).includes(texto)

)

mostrarPersonas(filtrados)

})

cargarPersonas()