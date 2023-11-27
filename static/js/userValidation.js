const form = document.getElementById("form")
const textoError6 = document.getElementById("textoError6")

form.confirmarContrasena.addEventListener("input", e =>{
    e.preventDefault()
    let password = form.contrasena.value
    let confirmPass = form.confirmarContrasena.value

    if (password != confirmPass) {
        textoError6.textContent = "Las contraseñas no coinciden"
        textoError6.style.color = "red"
    }else{
        textoError6.textContent = ""
    }
})

form.addEventListener("submit", e =>{
    e.preventDefault()

    if (form.contrasena.value != form.confirmarContrasena.value) {
        textoError6.textContent = "Las contraseñas no coinciden"
        textoError6.style.color = "red"
    }else if (form.contrasena.value == "") {
        textoError6.textContent = "No pueden quedar vacios los campos"
        textoError6.style.color = "red"
    }else{
        form.submit()
    }
})
