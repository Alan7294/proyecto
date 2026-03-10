const url = "http://127.0.0.1:8000/docente"

const formularioData = document.forms['formularioData']
const id_persona = document.getElementById('id_persona')
const id_especialidad = document.getElementById('id_especialidad')

formularioData.addEventListener('submit',(e)=>{

e.preventDefault()

fetch(url,{

method:'POST',

headers:{
'Content-Type':'application/json'
},

body:JSON.stringify({

id_persona:id_persona.value,
id_especialidad:id_especialidad.value

})

})

.then(response=>response.json())

.then(data=>{

console.log("Respuesta servidor:",data)

alert("Docente registrado correctamente")

window.location.href="docente_get.html"

})

.catch(error=>{

console.log("Error:",error)

})

})