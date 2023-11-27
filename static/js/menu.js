const bntMenu = document.getElementById("btnMenu")
const barraLateral = document.querySelector(".barra-lateral")
const spans = document.querySelectorAll("span")
const palanca = document.querySelector(".switch")
const circulo = document.querySelector(".circulo")
const main = document.querySelector(".container")
const logoContainer = document.querySelector(".logoContainer")
const imgContainer = document.querySelector(".imgContainer")
const options = document.querySelector(".options")

imgContainer.addEventListener("click",function (e) {
    e.preventDefault()
    options.style.display = "block"
})

document.addEventListener("click", event=>{
    if (!options.contains(event.target) && event.target !== imgPerfil) {
        options.style.display = "none";
    }
})


palanca.addEventListener("click", () =>{
    let body = document.body

    body.classList.toggle("dark-mode")
    circulo.classList.toggle("prendido")
})

bntMenu.addEventListener("click", () =>{
    barraLateral.classList.toggle("mini-barra-lateral")

    main.classList.toggle("min-container")

    logoContainer.classList.toggle("min-logo")

    spans.forEach(span =>{
        span.classList.toggle("oculto")
    })
})
