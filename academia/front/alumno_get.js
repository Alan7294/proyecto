const url = "http://127.0.0.1:8000/alumno"

async function cargarAlumnos(){

const response = await fetch(url)

const data = await response.json()

const tabla = document.getElementById("tablaAlumnos")

tabla.innerHTML=""

data.forEach(alumno=>{

tabla.innerHTML+=`

<tr>

<td>${alumno.id_alumno}</td>
<td>${alumno.id_persona}</td>
<td>${alumno.carrera_alumno}</td>

<td>

<button onclick="eliminarAlumno(${alumno.id_alumno})" class="delete">
Eliminar
</button>

</td>

</tr>

`

})

}

async function eliminarAlumno(id){

await fetch(url+"/"+id,{
method:"DELETE"
})

cargarAlumnos()

}

cargarAlumnos()