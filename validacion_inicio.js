const form = document.getElementById('loginForm');
const emailInput = document.getElementById('email');
const nameInput = document.getElementById('name');
const passwordInput = document.getElementById('password');

form.addEventListener('submit', function(event) {
  event.preventDefault();
  const email = emailInput.value.trim();
  const name = nameInput.value.trim();
  const password = passwordInput.value.trim();

  if (email === '' || name === '' || password === '') {
    alert('Por favor no dejes espacios en blanco');
  } else if (!validateEmail(email)) {
    alert('Por favor ingresa un correo valido');
  } else if (!validatePassword(password)) {
    alert('La contraseña debe tener al menos 8 caracteres y tener al menos una mayuscula, una minuscula, y un numero');
  } else {
    alert('Formulario enviado');
        form.submit();
  }
});

function validateEmail(email) {
  const re = /\S+@\S+\.\S+/;
  return re.test(email);
}

function validatePassword(password) {
  const re = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z\d]{8,}$/;
  return re.test(password);
}
