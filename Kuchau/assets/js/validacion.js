function validarFormulario() {
    var inputs = document.querySelectorAll('input');

    var formularioValido = true;

    inputs.forEach(function(input) {
        var valor = input.value.trim();
        
        var label = document.querySelector(`label[for="${input.id}"]`);

        if (valor === '') {
            alert(`El campo ${label.textContent} no puede estar vacío.`);
            formularioValido = false;
        } else {
            if (input.classList.contains('int-only')) {
                if (!/^\d+$/.test(valor)) {
                    alert(`El campo ${label.textContent} debe contener solo números enteros.`);
                    formularioValido = false;
                }
            }
        }
    });

    return formularioValido;
}

window.validarFormulario = validarFormulario;
