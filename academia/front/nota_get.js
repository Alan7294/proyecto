const url = "http://127.0.0.1:8000/nota"
const contenedor = document.getElementById('data')

const CargaData = (datos) => {
    let resultado = ""

    for (let i = 0; i < datos.length; i++) {
        resultado += `
        <li>
            <p>id nota: ${datos[i].id_nota}</p>
            <p>id inscripcion: ${datos[i].id_inscripcion}</p>
            <p>Nota: ${datos[i].nota}</p>
            <p>Fecha de registro: ${datos[i].fecha_registro}</p>
            <p>docente: ${datos[i].id_docente}</p>
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
