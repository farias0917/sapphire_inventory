const btn = document.getElementById("btn")
const textoError = document.getElementById("textoError")
const textoError2 = document.getElementById("textoError2")
const textoError3 = document.getElementById("textoError3")
const textoError4 = document.getElementById("textoError4")
const textoError5 = document.getElementById("textoError5")
const errorContainer = document.getElementById("errorContainer")

const form = document.getElementById("form")


form.marca.addEventListener("input", e=>{
    e.preventDefault()

    if (e.target.value == "") {
        textoError.textContent = "Este campo es requerido"
        textoError.style.color = "red"
    }else{
        textoError.textContent = ""
        errorContainer.classList.remove("errorContainer")
        errorContainer.textContent = ""
    }
})


form.nombre.addEventListener("input", e=>{
    e.preventDefault()

    if (e.target.value == "") {
        textoError2.textContent = "Este campo es requerido"
        textoError2.style.color = "red"
    }else{
        textoError2.textContent = ""
        errorContainer.classList.remove("errorContainer")
        errorContainer.textContent = ""
    }
})


form.descripcion.addEventListener("input", e=>{
    e.preventDefault()

    if (e.target.value == "") {
        textoError3.textContent = "Este campo es requerido"
        textoError3.style.color = "red"
    }else{
        textoError3.textContent = ""
        errorContainer.classList.remove("errorContainer")
        errorContainer.textContent = ""
    }
})


form.cantidad.addEventListener("input", e=>{
    e.preventDefault()

    if (e.target.value == "") {
        textoError4.textContent = "Este campo es requerido"
        textoError4.style.color = "red"
    }else{
        textoError4.textContent = ""
        errorContainer.classList.remove("errorContainer")
        errorContainer.textContent = ""
    }
})

form.categoria.addEventListener("input", e =>{
     e.preventDefault()

     if (form.categoria.value != "") {
        textoError5.textContent = ""
    }
})

form.addEventListener("submit", e =>{
    e.preventDefault()

    if (form.marca.value == "" || form.nombre.value == "" || form.descripcion.value == "" || form.cantidad.value == "") {
        errorContainer.textContent = "ningún campo debe quedar vacio"
        errorContainer.setAttribute("class","errorContainer")
    }else if(form.categoria.value == ""){
        textoError5.textContent = "Debe seleccionar una categoria"
        textoError5.style.color = "red"
    }else{
        form.submit()
    }
})
