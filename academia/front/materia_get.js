const url = "http://127.0.0.1:8000/materia"

async function cargarMaterias(){

try{

const response = await fetch(url)

if(!response.ok){
throw new Error("Error al obtener materias")
}

const data = await response.json()

const tabla = document.getElementById("tablaMaterias")

tabla.innerHTML=""

data.forEach(materia=>{

tabla.innerHTML += `

<tr>

<td>${materia.id_materia}</td>
<td>${materia.nombre_materia}</td>
<td>${materia.descripcion}</td>

<td>

<button class="delete"
onclick="eliminarMateria(${materia.id_materia})">
Eliminar
</button>

</td>

</tr>

`

})

}catch(error){

console.error(error)
alert("No se pudieron cargar las materias")

}

}

async function eliminarMateria(id){

if(!confirm("¿Eliminar esta materia?")) return

await fetch(url+"/"+id,{
method:"DELETE"
})

cargarMaterias()

}

cargarMaterias()