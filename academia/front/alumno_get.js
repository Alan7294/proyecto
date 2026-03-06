const url = "http://127.0.0.1:8000/alumno"
const contenedor = document.getElementById('data')

const CargaData = (datos) => {
    let resultado = ""

    for (let i = 0; i < datos.length; i++) {
        resultado += `
        <li>
            <p>ID: ${datos[i].id_alumno}</p>
            <p>Nombre: ${datos[i].nombre}</p>
            <p>Apellido paterno: ${datos[i].apellido_pat}</p>
            <p>Apellido materno: ${datos[i].apellido_mat}</p>
            <p>CI: ${datos[i].ci}</p>
            <p>Correo: ${datos[i].correo}</p>
            <p>Fecha nacimiento: ${datos[i].fecha_nacimiento}</p>
            <p>Carrera: ${datos[i].carrera_alumno}</p>
            <hr>
        </li>
        `
    }

    contenedor.innerHTML = resultado
}

fetch(url)
    .then(response => response.json())
    .then(data => {
        CargaData(data)
    })
    .catch(error => {
        console.log(error)
    })
