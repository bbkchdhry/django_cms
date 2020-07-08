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
        edit_user_modal.querySelector("#edit_first_name").value = data.first_name;
        edit_user_modal.querySelector("#edit_last_name").value = data.last_name;
        edit_user_modal.querySelector("#edit_user_name").value = data.user_name;
        edit_user_modal.querySelector("#edit_email").value = data.email;
        console.log($("input[name=is_superuser]:checked").value);
        const is_superuser = data.is_superuser.toString()[0].toUpperCase() + data.is_superuser.toString().slice(1)
        const is_active = data.is_active.toString()[0].toUpperCase() + data.is_active.toString().slice(1)
        $("input[name='is_superuser'][value="+is_superuser+"]").prop('checked', true);
        $("input[name='is_active'][value="+is_active+"]").prop('checked', true)
        edit_user_modal.style.display = "flex"
    }
}
