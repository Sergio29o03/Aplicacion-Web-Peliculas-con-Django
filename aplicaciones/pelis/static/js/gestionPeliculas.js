(function(){

    notificacionSwal(document.title,"Bienvenido ♥","succes","ok")
    const btnEliminacion=document.querySelectorAll(".btnEliminacion");

    formulariopelicula.addEventListener("submit",function(e){
        let nombre = String(txtNombre.value).trim();
        let genero = String(txtGenero.value).trim();
        let año = parseint(numAño.value);
        if (nombre.length<3){
            notificacionSwal(document.title,"El nombre de la pelicula no puede ir vacio...","warning","ok")
            e.preventDefault();
        }else if(genero.length<3){
            notificacionSwal(document.title,"El genero de la pelicula no puede ir vacio...","warning","ok")
            e.preventDefault();
        }
    });





    btnEliminacion.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacion=confirm('¿Seguro de eliminar la pelicula?');
                if(!confirmacion){
                    e.preventDefault();
        }
    });
});
})();