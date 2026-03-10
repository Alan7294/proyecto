const url = "http://127.0.0.1:8000/administrador"

const params = new URLSearchParams(window.location.search)

const id_admin = document.getElementById("id_admin")
const id_persona = document.getElementById("id_persona")

id_admin.value = params.get("id_admin")
id_persona.value = params.get("id_persona")

const formulario = document.getElementById("formEditar")

formulario.addEventListener("submit", async (e)=>{

e.preventDefault()

await fetch(url + "/" + id_admin.value,{

method:"PUT",

headers:{
"Content-Type":"application/json"
},

body: JSON.stringify({
id_persona: id_persona.value
})

})

alert("Administrador actualizado")

window.location.href="administrador_get.html"

})