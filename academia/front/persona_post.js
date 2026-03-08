const url = "http://127.0.0.1:8000/persona";

print({
            nombre_persona: nombre_persona.value,
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
            nombre_persona: nombre_persona.value,
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