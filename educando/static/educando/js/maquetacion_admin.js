$(document).ready(function(){
    $('.user').on('click', function(){
        window.location.href = $(this).attr('data-href');
    })

     var table =$('#proffesor_table').DataTable({
        dom: 'f',
        "oLanguage": {
        "sZeroRecords": "No coincide ningún resultado",
        "sSearch": " Buscar:",
        "sInfoEmpty": "No se han encontrado registros"
        },
    })
    $('#id_guardar_profesor').on('click', function(){

            fn_crear_profesor();
    })

})

function fn_crear_profesor(){

    var datos_profesor = JSON.stringify({
        'first_name': $('#id_first_name').val(),
        'last_name':$('#id_last_name').val(),
        'username':$('#id_username').val(),
        'password1':$('#id_password1').val(),
        'password2':$('#id_password2').val()

    });

    $.ajax({
        url:'tabla_prof/nuevo_profesor/',
        data: {'datos_profesor': datos_profesor},
        type:'POST',
        success: function(messages){
            if(messages.error===undefined){
                $.notify({
                     message: messages.success
                    },{
                      type: 'success',
                      placement: {
                        from: "bottom",
                        align: "right"
                      },
                      z_index: 10000,
                    });
            }
            else{
                $.notify({
                     message: messages.error
                    },{
                      type: 'danger',
                      placement: {
                        from: "bottom",
                        align: "right"
                      },
                      z_index: 10000,
                    });

            }

        },
        error: function(messages){

        }


    })

}
