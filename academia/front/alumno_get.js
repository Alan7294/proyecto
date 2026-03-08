const url = "http://127.0.0.1:8000/alumno"
const contenedor = document.getElementById('data')

const CargaData = (datos) => {
    let resultado = ""

    for (let i = 0; i < datos.length; i++) {
        resultado += `
        <li>
            <p>id Alumno: ${datos[i].id_alumno}</p>
            <p>id Persona: ${datos[i].id_persona}</p>
            <p>id carrera: ${datos[i].carrera_alumno}</p>
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
