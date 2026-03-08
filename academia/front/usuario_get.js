const url = "http://127.0.0.1:8000/usuario"
const contenedor = document.getElementById('data')

const CargaData = (datos) => {
    let resultado = ""

    for (let i = 0; i < datos.length; i++) {
        resultado += `
        <li>
            <p>id usuario: ${datos[i].id_usuario}</p>
            <p>id persona: ${datos[i].id_persona}</p>
            <p>nombre de usuario: ${datos[i].nombre_usuario}</p>
            <p>contraseña: ${datos[i].contraseña}</p>
            <p>tipo de usuario: ${datos[i].id_tipo}</p>
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
