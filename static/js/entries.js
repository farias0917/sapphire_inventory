const btnEntriesModal = document.getElementById("btnEntriesModal")
const entrieModal = document.getElementById("entrieModal")
const close = document.getElementById("close")

btnEntriesModal.addEventListener("click", () =>{
    entrieModal.style.display = "flex"
})

close.addEventListener("click", () =>{
    entrieModal.style.display = "none"
})

