$.ajax({
    url: "list/",
    type: "get",
    dataType: "json",
    success: function(data){
        console.log(data)
        let rows = ""
        data.forEach(d=>{
            rows += `
                <tr id="user_roles_${d.id}">
                    <td>${d.id}</td>
                    <td>${d.user}</td>
                    <td>${d.roles}</td>
                    <td>
                        <a onclick="delete_user_roles(${d.id})" class="text-muted font-16" style="margin-right: 10px" id="delete_btn"><i class="fas fa-trash-alt"></i></a>
                        <a onclick="get_user_role_edit_modal(${d.id})" class="text-muted font-16" id="edit_btn"><i class="far fa-edit"></i></a>
                    </td>
                </tr>
            `
        })
        let tableBody = $("table tbody");
        tableBody.append(rows)
        $(function(){
             $('#user_roles_datatable').DataTable({
            pageLength: 10,
            fixedHeader: true,
            responsive: true,
            "sDom": 'rtip',
            columnDefs: [{
                targets: 'no-sort',
                orderable: false
            }]
        });

        var table = $('#user_roles_datatable').DataTable();
        $('#key-search').on('keyup', function() {
            table.search(this.value).draw();
        });
        $('#type-filter').on('change', function() {
            table.column(4).search($(this).val()).draw();
        });
        })
        }
})


$(document).on("submit", "#post_user_roles", function(e){
    e.preventDefault();
    let roles = [];
    $("input[name='roles']:checked").each(function() {
        roles.push($(this).val());
    })
    console.log(roles)
    console.log(typeof roles)
    $.ajax({
        url: "create/",
        type: "post",
        data: {
            user: $("#user").val(),
            roles: roles,
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
            action: "post"
        },
        success: function (data){
            document.querySelector("#post_user_roles").reset();
            let row = ""
            row += `
               <tr id="user_roles_${data.id}">
                    <td>${data.id}</td>
                    <td>${data.user}</td>
                    <td>${data.roles}</td>
                    <td>
                        <a onclick="delete_user_roles(${data.id})" class="text-muted font-16" style="margin-right: 10px" id="delete_btn"><i class="fas fa-trash-alt"></i></a>
                        <a onclick="" class="text-muted font-16" id="edit_btn"><i class="far fa-edit"></i></a>
                    </td>
                </tr>
            `
            let tableBody = $("table tbody");
            tableBody.append(row)
        }
    })
})

function get_user_role_edit_modal(data){
    $.ajax({
        url: "edit/"+data,
        type: "get",
        dataType: "json",
        success: function(data){
            toggleUserRolesEditModal(data)
        }
    })
}

function delete_user_roles(data){
    let result = confirm(`Do you want to delete user id ${data} ?`)
    if(result){
        $.ajax({
            url: "delete/"+data,
            type: "delete",
            dataType: "json",
            success: function(){
                $(`#user_roles_${data}`).remove();
            }
        });
    }
}

$(document).on("submit", "#edit_user_roles", function (e){
    e.preventDefault();
    console.log("editing.....")
    console.log(e)
    let userRoleId = e.target.elements[1].value;
    console.log(userRoleId)
    let roles = []
    $(".roles input[name='roles']:checked").each(function(){
        roles.push($(this).val())
    });
    console.log(roles)
    $.ajax({
        url: "edit/"+userRoleId,
        type: "put",
        dataType: "json",
        data: {
            user: $("#edit_user").val(),
            roles: roles,
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
            action: "put"
        }
    })
})