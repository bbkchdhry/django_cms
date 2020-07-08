const modal = document.querySelector(".user_modal")
const edit_user_modal = document.querySelector(".edit_user_modal")

$("#add_user").on("click", function (e){
    e.preventDefault();
    console.log("Add User....")
    toggleModal();
})


$(".modal_container_close").on("click", function (e){
  toggleModal();
  document.querySelector("#post_user").reset();
})

function toggleModal(){
    if(modal.style.display === "flex"){
        modal.style.display = "none"
    }
    else{
        modal.style.display = "flex"
    }
}

$(".edit_modal_container_close").on("click", function (e){
  toggleEditModal();
  document.querySelector("#edit_user").reset();
})

function toggleEditModal(data){
    if(edit_user_modal.style.display === "flex"){
        edit_user_modal.style.display = "none"
    }
    else{
        edit_user_modal.querySelector("#first_name").value = data.first_name;
        edit_user_modal.querySelector("#last_name").value = data.last_name;
        edit_user_modal.querySelector("#user_name").value = data.user_name;
        edit_user_modal.querySelector("#email").value = data.email;
        console.log($("input[name=is_superuser]:checked").value);
        const is_superuser = typeof data.is_superuser
        console.log(is_superuser)
        edit_user_modal.querySelector("input[name='is_active']").value = data.is_active;
        edit_user_modal.style.display = "flex"
    }

}
