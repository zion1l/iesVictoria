$(document).ready(function(){
    fn_ajusta_campos_formulario('formulario');

})

function fn_ajusta_campos_formulario( formulario ) {
        if( ! $("#" + formulario).length )
            return;

        var lineas_forumario = $("#" + formulario).find(".form-group");

        lineas_forumario.each( function() {
            var ancho_disponible = $(this).innerWidth();
            var etiqueta = $(this).children("label");
            var campo = $(etiqueta).next();
            var campoip = $(campo).next();
            if( ( $(etiqueta).css("display") === "inline-block" ) || ( $(etiqueta).css("float") === "left" ))  {
                ancho_disponible = ancho_disponible - $(etiqueta).width() - 20;
                if( ( $(campo).prop("tagName") === "TEXTAREA" ) && ($(etiqueta).css("display") === "inline-block" )) {
                    $(etiqueta).css("float", "left");
                    $(campo).css("margin-left","4px");
                }
                if( $(campo).hasClass("bootstrap-select") ){
                    $(campo).width(ancho_disponible-2);
                    return;
                }

            }
            $(campo).outerWidth(ancho_disponible);
        });
    }