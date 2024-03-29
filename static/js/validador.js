
entrar();

$(document).ready(function() {
    jQuery.extend(jQuery.validator.messages, {
      required: "Este campo es obligatorio.",
      remote: "Por favor, rellena este campo.",
      email: "Por favor, escribe una dirección de correo válida",
      url: "Por favor, escribe una URL válida.",
      date: "Por favor, escribe una fecha válida.",
      dateISO: "Por favor, escribe una fecha (ISO) válida.",
      number: "Por favor, escribe un número entero válido.",
      digits: "Por favor, escribe sólo dígitos.",
      creditcard: "Por favor, escribe un número de tarjeta válido.",
      equalTo: "Por favor, escribe el mismo valor de nuevo.",
      accept: "Por favor, escribe un valor con una extensión aceptada.",
      maxlength: jQuery.validator.format("Por favor, no escribas más de {0} caracteres."),
      minlength: jQuery.validator.format("Por favor, no escribas menos de {0} caracteres."),
      rangelength: jQuery.validator.format("Por favor, escribe un valor entre {0} y {1} caracteres."),
      range: jQuery.validator.format("Por favor, escribe un valor entre {0} y {1}."),
      max: jQuery.validator.format("Por favor, escribe un valor menor o igual a {0}."),
      min: jQuery.validator.format("Por favor, escribe un valor mayor o igual a {0}.")
    });
});



function entrar(){
//email jqueryvalidador
console.log("CamposObligatorios")
$("#entrar").validate({
    errorClass: "is-invalid", 
    rules:{
        email:{
            email:true,
            required:true
        },
        pass:{
            required:true

        },
    },  
})
}


//validacion correo 
$("#entrar").submit(function () {  
    if($("#email").val().indexOf('@', 0) == -1 || $("#email").val().indexOf('.', 0) == -1 || $("#email").val().length < 1) {  
        Swal.fire({
            type: 'error',
            title: 'Oops...',
            text: 'La dirección e-mail parece incorrecta!',
          });  
        return false;  
    }  
    return true;  
});  

//validacion correo vacio
$("#entrar").submit(function(){

    if($("#email").val().length = 0 || $("#email").val().length < 1){
        Swal.fire({
            type: 'error',
            title: 'Oops...',
            text: 'El campo del correo está vacío',
          });  
          return false;
    }

})



//validacion password vacio
$("#entrar").submit(function () {  
    var pass= document.getElementById("pass").value;

    if(pass.length < 1) {  

        Swal.fire({
            type: 'error',
            title: 'Oops...',
            text: 'El campo de la contraseña está vacío',
          });  
        return false;  
    }  
    return true;  

});  



