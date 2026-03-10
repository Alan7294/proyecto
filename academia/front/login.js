const url = "http://127.0.0.1:8000/usuario"

const form = document.getElementById("formLogin")
const usuarioInput = document.getElementById("usuario")
const passwordInput = document.getElementById("password")
const tipoUsuario = document.getElementById("tipo_usuario")

form.addEventListener("submit",(e)=>{

e.preventDefault()

const usuario = usuarioInput.value
const password = passwordInput.value
const tipo = tipoUsuario.value

fetch(url)

.then(response => response.json())

.then(data => {

const encontrado = data.find(u => 
u.nombre_usuario === usuario &&
u.contraseña === password &&
String(u.id_tipo) === tipo
)

if(encontrado){

if(tipo == "3"){
window.location.href="panel_admin.html"
}

if(tipo == "2"){
window.location.href="panel_docente.html"
}

if(tipo == "1"){
window.location.href="panel_alumno.html"
}

}else{

alert("Datos incorrectos")

}

})

.catch(error => console.log(error))

})