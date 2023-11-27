const categoryModal = document.getElementById("categoryModal")
const btnCategoryModal = document.getElementById("btnCategoryModal")
const btnClose = document.getElementById("close")

btnCategoryModal.addEventListener("click", e =>{
    categoryModal.style.display = "flex"
})

btnClose.addEventListener("click", e =>{
    categoryModal.style.display = "none"
})