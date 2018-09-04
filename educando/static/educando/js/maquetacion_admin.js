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
})