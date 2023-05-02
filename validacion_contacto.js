$(document).ready(function() {
    $('#contactform').validate({
      rules: {
        
        "exampleInputName1": {
          required: true,
          minlength: 3
        },
        "exampleInputEmail1": {
          required: true,
          email: true
        },
        "exampleInputMessage1": {
          required: true,
          minlength: 6
        }
      },
      messages: {
        
        "exampleInputName1": {
          required: "Por favor ingrese su nombre",
          minlength: "Su nombre debe tener al menos 3 caracteres"
        },
        "exampleInputEmail1": {
          required: "Por favor ingrese su correo electrónico",
          email: "Por favor ingrese un correo electrónico válido"
        },
        "exampleInputMessage1": {
          required: "Por favor ingrese su mensaje",
          minlength: "Su mensaje debe tener al menos 6 caracteres"
        }
      },
      submitHandler: function(form) {
        
        alert('Formulario enviado');
        form.submit();
      }
    });
  });