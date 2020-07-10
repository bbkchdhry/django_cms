$.ajax({
    url: 'list/',
    type: 'get',
    dataType: 'json',
    success: function (data){
        let rows = ''
        data.forEach(d=>{
            rows += `
                <tr id="role-${d.id}">
                    <td>${d.id}</td>
                    <td>${d.name}</td>
                    <td>
                        <a onclick="delete_role(${d.id})" class="text-muted font-16" style="margin-right: 10px" id="delete_btn"><i class="fas fa-trash-alt"></i></a>
                        <a onclick="get_role_edit_modal(${d.id})" class="text-muted font-16" id="edit_btn"><i class="far fa-edit"></i></a>
                    </td>
                </tr>
            
            `
        })
        let tableBody = $("table tbody")
        tableBody.append(rows)
        $(function(){
             $('#role_datatable').DataTable({
            pageLength: 10,
            fixedHeader: true,
            responsive: true,
            "sDom": 'rtip',
            columnDefs: [{
                targets: 'no-sort',
                orderable: false
            }]
        });

        var table = $('#role_datatable').DataTable();
        $('#key-search').on('keyup', function() {
            table.search(this.value).draw();
        });
        $('#type-filter').on('change', function() {
            table.column(4).search($(this).val()).draw();
        });
        })
    }
})

$(document).on("submit", "#post_role", function (e){
    e.preventDefault();
    $.ajax({
        url: "create/",
        type: 'post',
        dataType: 'json',
        data: {
            name: $("input[name='name']").val(),
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
            action: "post"
        },
        success: function(data){
            document.querySelector('#post_role').reset();
            let row = ""

            row += `
                <tr>
                    <td>${data.id}</td>
                    <td>${data.name}</td>
                    <td>
                        <a href="#" onclick="" class="text-muted font-16" style="margin-right: 10px" id="delete_btn"><i class="fas fa-trash-alt"></i></a>
                        <a href="#" onclick="get_role_edit_modal(${data.id})" class="text-muted font-16" id="edit_btn"><i class="far fa-edit"></i></a>
                    </td>
                </tr>
            
            `
            let tableBody = $("table tbody")
            tableBody.append(row)
        }
    })
})

function delete_role(data){
    let result = confirm(`Do you want to delete role id ${data} ?`);
    if(result){
        $.ajax({
            url: "delete/"+data,
            type: "delete",
            dataType: "json",
            success: function (){
                $(`#role-${data}`).hide();
            }
        });
    }

}

function get_role_edit_modal(data){
    $.ajax({
        url: "edit/"+data,
        type: "get",
        dataType: "json",
        success: function(data){
            console.log(data)
            toggleEditRoleModal(data);
        }
    })
}

$(document).on('submit', '#edit_role', function(e){
    let roleId = e.target.elements[1].value;
    $.ajax({
        url: "edit/"+roleId,
        type: "put",
        dataType: "json",
        data: {
            name: $(".role_name input[name='name']").val(),
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
            action: "put"
        },
        success: function (){
            $(".edit_role_modal").hide();
        }
    })
})