const btnUserModal = document.getElementById("btnUserModal")
const btnDeleteModal = document.querySelectorAll(".delete")
const userModal = document.getElementById("userModal")
const userModalDelete = document.getElementById("userModalDelete")
const btnClose = document.getElementById("close")
const btnCancelDelete = document.getElementById("cancelDelete")

btnUserModal.addEventListener("click",e =>{
    userModal.style.display = "flex"
})

btnClose.addEventListener("click", e =>{
    userModal.style.display = "none"
})

btnDeleteModal.forEach((elemento) =>{
    elemento.addEventListener("click", function eliminar(){
        userModalDelete.style.display = "block"
    })
})

btnCancelDelete.addEventListener("click", e =>{
    userModalDelete.style.display = "none"

})
