const url = "http://127.0.0.1:8000/usuario"

const contenedor = document.getElementById('data')
const buscador = document.getElementById('buscador')

let usuarios = []

function mostrarUsuarios(datos){

let resultado = ""

datos.forEach(usuario => {

resultado += `

<li>

<p><b>ID Usuario:</b> ${usuario.id_usuario}</p>
<p><b>ID Persona:</b> ${usuario.id_persona}</p>
<p><b>Usuario:</b> ${usuario.nombre_usuario}</p>
<p><b>Contraseña:</b> ${usuario.contraseña}</p>
<p><b>Tipo Usuario:</b> ${usuario.id_tipo}</p>

<hr>

</li>

`

})

contenedor.innerHTML = resultado

}

function cargarUsuarios(){

fetch(url)

.then(response => response.json())

.then(data => {

usuarios = data
mostrarUsuarios(usuarios)

})

.catch(error => console.log(error))

}

buscador.addEventListener("keyup", () => {

let texto = buscador.value.toLowerCase()

let filtrados = usuarios.filter(u =>

u.nombre_usuario.toLowerCase().includes(texto) ||
String(u.id_persona).includes(texto)

)

mostrarUsuarios(filtrados)

})

cargarUsuarios()