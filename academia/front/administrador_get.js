const url = "http://127.0.0.1:8000/administrador"

async function cargarAdministradores(){

const response = await fetch(url)
const data = await response.json()

const tabla = document.getElementById("tablaAdmins")

tabla.innerHTML = ""

data.forEach(admin => {

tabla.innerHTML += `

<tr>

<td>${admin.id_admin}</td>
<td>${admin.id_persona}</td>

<td>

<button class="edit"
onclick="editarAdmin(${admin.id_admin},${admin.id_persona})">
Editar
</button>

<button class="delete"
onclick="eliminarAdmin(${admin.id_admin})">
Eliminar
</button>

</td>

</tr>

`

})

}

function editarAdmin(id_admin,id_persona){

window.location.href =
`administrador_put.html?id_admin=${id_admin}&id_persona=${id_persona}`

}

async function eliminarAdmin(id){

await fetch(url+"/"+id,{
method:"DELETE"
})

cargarAdministradores()

}

cargarAdministradores()