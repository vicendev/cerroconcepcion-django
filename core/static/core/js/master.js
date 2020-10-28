$('#estate-hideshow').on("click",function(){
    $('#div-estate-filter').slideToggle()

    value = $('#estate-hideshow').attr('value')

    if(value === "Mostrar Filtros"){
        $('#estate-hideshow').attr('value','Ocultar Filtros')
    }
    else{
        $('#estate-hideshow').attr('value','Mostrar Filtros')
    }
})