$(document).ready(function() {
    
    $("#contactform").validate({
      
      rules: {
        
        exampleInputName1: {
          required: true,
          minlength: 2
        },
        
        exampleInputEmail1: {
          required: true,
          email: true
        },
        
        exampleInputMessage1: {
          required: true,
          minlength: 10
        }
      },
     
      messages: {
        exampleInputName1: {
          required: "Este campo es obligatorio",
          minlength: "Por favor ingrese al menos 2 caracteres"
        },
        exampleInputEmail1: {
          required: "Este campo es obligatorio",
          email: "Por favor ingrese un correo electrónico válido"
        },
        exampleInputMessage1: {
          required: "Este campo es obligatorio",
          minlength: "Por favor ingrese al menos 10 caracteres"
        }
      },
     

      submitHandler: function(form) {
        
        alert("Consulta enviada exitosamente");
        form.submit();
      }
    });
  
    
    $("#enviarFormulario").prop("disabled", true);
    $("#contactform").on("keyup change", function() {
      if ($("#contactform").valid()) {
        $("#enviarFormulario").prop("disabled", false);
      } else {
        $("#enviarFormulario").prop("disabled", true);
      }
    });
  });
  