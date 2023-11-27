const file = document.getElementById("productImg").onchange = function(e) {
    let reader = new FileReader()
    reader.readAsDataURL(e.target.files[0])

    reader.onload = function() {
        let preview = document.getElementById("formContainer2")
        let imagen = document.createElement("img")
        imagen.classList.add("modalImg")
        imagen.src = reader.result
        preview.append(imagen)
    }
}