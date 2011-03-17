$(document).ready(function(){
    var alto_sidebar = $('#sidebar').height();
    var alto_contenido = $('#contenido').height();
    if(alto_sidebar<=alto_contenido){
        $('#sidebar').height(alto_contenido);
    }else{
        $('#contenido').height(alto_sidebar);
    }
});


