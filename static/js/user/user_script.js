$.ajax({
url: 'list/',
type: 'get',
dataType: 'json',
success: function (data){
    let rows = ''
    console.log("data is: ")
    console.log(data)
    data.forEach(d => {
        rows += `
              <tr id="user-${d.id}">
                  <td>${d.id}</td>
                  <td>${d.user_name}</td>
                  <td style="word-break: break-all">${d.salt}</td>
                  <td style="word-break: break-all">${d.hashed_password}</td>
                  <td>${d.first_name}</td>
                  <td>${d.last_name}</td>
                  <td>${d.email}</td>
                  <td>${d.is_superuser}</td>
                  <td>${d.is_active}</td>
                  <td>
                     <a onclick="delete_user(${d.id})" class="text-muted font-16" style="margin-right: 10px" id="delete_btn"><i class="fas fa-trash-alt"></i></a>
                     <a onclick="get_edit_modal(${d.id});" class="text-muted font-16" id="edit_btn"><i class="far fa-edit"></i></a>
                 </td>
              </tr>
        `
    })
    let tableBody = $("table tbody");
    tableBody.append(rows);
    $(function(){
         $('#user_datatable').DataTable({
        pageLength: 10,
        fixedHeader: true,
        responsive: true,
        "sDom": 'rtip',
        columnDefs: [{
            targets: 'no-sort',
            orderable: false
        }]
    });

    var table = $('#user_datatable').DataTable();
    $('#key-search').on('keyup', function() {
        table.search(this.value).draw();
    });
    $('#type-filter').on('change', function() {
        table.column(4).search($(this).val()).draw();
    });
    })
}

});


$(document).on("submit", "#post_user", function (e){
    e.preventDefault();
    console.log("User posting....")
    $.ajax({
        url: "create/",
        type: "post",
        dataType: "json",
        data: {
            first_name: $("#first_name").val(),
            last_name: $("#last_name").val(),
            user_name: $("#user_name").val(),
            password: $("#password").val(),
            email: $("#email").val(),
            is_superuser: $("input[name='is_superuser']:checked").val(),
            is_active: $("input[name='is_active']:checked").val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: "post"
        },
        success: function(data){
            document.querySelector("#post_user").reset();
              let row = '';
              row += `
                <tr>
                      <td>${data.id}</td>
                      <td>${data.user_name}</td>
                      <td style="word-break: break-all">${data.salt}</td>
                      <td style="word-break: break-all">${data.hashed_password}</td>
                      <td>${data.first_name}</td>
                      <td>${data.last_name}</td>
                      <td>${data.email}</td>
                      <td>${data.is_superuser}</td>
                      <td>${data.is_active}</td>
                  <td>
                     <a href="#" onclick="delete_user(${data.id})" class="text-muted font-16" style="margin-right: 10px" id="delete_btn"><i class="fas fa-trash-alt"></i></a>
                     <a href="#" onclick="get_edit_modal(${data.id});" class="text-muted font-16" id="edit_btn"><i class="far fa-edit"></i></a>
                  </td>
                </tr>    
              `;
              tableBody = $("table tbody");
              tableBody.append(row);

            }
    })
})

function delete_user(data){
    let result = confirm(`Do you want to delete user id ${data} ?`)
    if(result){
        $.ajax({
            url: 'delete/'+data,
            type: "delete",
            dataType: "json",
            success: function (){
                $(`#user-${data}`).remove();
            }
        })
    }
}

function get_edit_modal(data){
    $.ajax({
        url: 'edit/'+data,
        type: "get",
        dataType: "json",
        success: function (data){
            toggleUserEditModal(data);
        }
    })
}

$(document).on("submit", "#edit_user", function(e){
    console.log("editing.....")
    let userId = e.target.elements[1].value;
    console.log(e.target.elements[1].value)
    $.ajax({
        url: 'edit/'+userId,
        type: "post",
        dataType: "json",
        data: {
            first_name: $("#edit_first_name").val(),
            last_name: $("#edit_last_name").val(),
            user_name: $("#edit_user_name").val(),
            email: $("#edit_email").val(),
            is_superuser: $(".edit_is_superuser input[name='is_superuser']:checked").val(),
            is_active: $(".edit_is_active input[name='is_active']:checked").val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: "put"
        },
        success: function(){
            $(".edit_user_modal").hide();
            $("#datatable").DataTable().reload();
        }

    })
})