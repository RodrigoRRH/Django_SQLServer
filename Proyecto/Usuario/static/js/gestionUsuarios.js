(function(){
    const btnEliminacion = document.querySelectorAll(".btnEliminacion")

    btnEliminacion.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacion = confirm('¿Seguro de eliminar el curso?');
            if (!confirmacion){
                e.preventDefault();
            }
        });
    });
})();

function mostrarPassword(){
    var cambio = document.getElementById("txtContraseña");
    if(cambio.type == "password"){
        cambio.type = "text";
        $('.icon').removeClass('fa fa-eye-slash').addClass('fa fa-eye');
    }else{
        cambio.type = "password";
        $('.icon').removeClass('fa fa-eye').addClass('fa fa-eye-slash');
    }
} 