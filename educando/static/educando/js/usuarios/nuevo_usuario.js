$(document).ready(function(){
    fn_crear_usuario();



})

function fn_crear_usuario(){
    var datos_usuario = JSON.stringify({
        "username": $('#id_username').val(),
        "password": $('#id_password1').val(),



    })


}