const url = "http://127.0.0.1:8000/persona"

const formularioData = document.forms['formularioData']

const nombre_persona = document.getElementById('nombre_persona')
const apellido_pat = document.getElementById('apellido_pat')
const apellido_mat = document.getElementById('apellido_mat')
const ci = document.getElementById('ci')
const correo = document.getElementById('correo')
const fecha_nacimiento = document.getElementById('fecha_nacimiento')

formularioData.addEventListener('submit',(e)=>{

e.preventDefault()

fetch(url,{

method:'POST',

headers:{
'Content-Type':'application/json'
},

body:JSON.stringify({

nombre_persona:nombre_persona.value,
apellido_pat:apellido_pat.value,
apellido_mat:apellido_mat.value,
ci:ci.value,
correo:correo.value,
fecha_nacimiento:fecha_nacimiento.value

})

})

.then(response=>response.json())

.then(data=>{

console.log("Respuesta servidor:",data)

alert("Persona registrada correctamente")

window.location.href="persona_get.html"

})

.catch(error=>{

console.log("Error:",error)

})

})