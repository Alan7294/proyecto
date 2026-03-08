const url = "http://127.0.0.1:8000/inscripcion"
const contenedor = document.getElementById('data')

const CargaData = (datos) => {
    let resultado = ""

    for (let i = 0; i < datos.length; i++) {
        resultado += `
        <li>
            <p>id inscripcion: ${datos[i].id_inscripcion}</p>
            <p>id alumno: ${datos[i].id_alumno}</p>
            <p>id clase: ${datos[i].id_clase}</p>
            <p>Fecha de inscripcion: ${datos[i].fecha_inscripcion}</p>
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

print({
            nombre: nombre.value,
            apellido_pat: apellido_pat.value,
            apellido_mat: apellido_mat.value,
            ci: ci.value,
            correo: correo.value,
            fecha_nacimiento: fecha_nacimiento.value
        })
formularioData.addEventListener('submit', (e) => {
    e.preventDefault();

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            nombre: nombre.value,
            apellido_pat: apellido_pat.value,
            apellido_mat: apellido_mat.value,
            ci: ci.value,
            correo: correo.value,
            fecha_nacimiento: fecha_nacimiento.value
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log("Respuesta del servidor:", data);
    })
    .catch(error => {
        console.log("Error:", error);
    });
});