$(document).ready(function(){

     var table =$('#marks_table').DataTable({
        dom: 'f',
        "oLanguage": {
        "sZeroRecords": "No coincide ningún resultado",
        "sSearch": " Buscar: ",
        "sInfoEmpty": "No se han encontrado registros"
        },
    })
    var table_marks =$('#marks_table').DataTable({
        dom: 'f',
        "oLanguage": {
        "sZeroRecords": "No coincide ningún resultado",
        "sSearch": " Buscar: ",
        "sInfoEmpty": "No se han encontrado registros"
        },
    })
    $('.subject').on('click', function(){
        window.location.href = $(this).attr('data-href');
    })
})