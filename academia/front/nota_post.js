const url = "http://127.0.0.1:8000/notas"

const formularioData = document.forms['formularioData']

const id_inscripcion = document.getElementById('id_inscripcion')
const nota = document.getElementById('nota')
const id_docente = document.getElementById('id_docente')

formularioData.addEventListener('submit',(e)=>{

e.preventDefault()

fetch(url,{

method:'POST',

headers:{
'Content-Type':'application/json'
},

body:JSON.stringify({

id_inscripcion:id_inscripcion.value,
nota:nota.value,
id_docente:id_docente.value

})

})

.then(response=>response.json())

.then(data=>{

console.log("Respuesta servidor:",data)

alert("Nota registrada correctamente")

window.location.href="notas_get.html"

})

.catch(error=>{

console.log("Error:",error)

alert("Error al registrar nota")

})

})