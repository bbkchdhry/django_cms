const modal = document.querySelector(".user_modal")

$("#add_user").on("click", function (e){
    e.preventDefault();
    console.log("Add User....")
    toggleModal();
})


$(".modal_container_close").on("click", function (e){
  toggleModal();
  document.querySelector("#post_user").reset();
})

$(modal).on("click", function (e){
    if (e.currentTarget === e.target){
        toggleModal();
    }
})

function toggleModal(){
    document.querySelector(".modal_title").innerHTML = "User Form"
    if(modal.style.display === "flex"){
        modal.style.display = "none"
    }
    else{
        modal.style.display = "flex"
    }
}

function toggleEditModal(data){
    document.querySelector(".modal_title").innerHTML = "Edit User"
    console.log(data)
    if(modal.style.display === "flex"){
        modal.style.display = "none"
    }
    else{
        modal.style.display = "flex"
    }

}
