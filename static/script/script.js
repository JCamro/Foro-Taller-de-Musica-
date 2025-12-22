
// GALERIA

document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById("modal-visor");
    const modalImg = document.getElementById("img-expandida");
    const captionText = document.getElementById("caption");
    const closeBtn = document.querySelector(".close-btn");

    // Seleccionar todos los enlaces de la galería
    const galeryLinks = document.querySelectorAll('.galery-container a');

    galeryLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault(); // Evita que abra el enlace normalmente
            
            modal.style.display = "block";
            modalImg.src = this.href; // Usa el href del <a> como fuente
            captionText.innerHTML = this.getAttribute('data-title');
            
            // Bloquear scroll del fondo
            document.body.style.overflow = "hidden";
        });
    });

    // Cerrar al hacer clic en la X
    closeBtn.onclick = () => {
        cerrarModal();
    };

    // Cerrar al hacer clic fuera de la imagen
    modal.onclick = (e) => {
        if (e.target === modal) cerrarModal();
    };

    function cerrarModal() {
        modal.style.display = "none";
        document.body.style.overflow = "auto";
    }
});


// REDIRECCION A FORMULARIO
document.addEventListener("DOMContentLoaded", () => {
    // 1. Capturamos los parámetros de la URL
    const params = new URLSearchParams(window.location.search);
    const instrumentoSeleccionado = params.get('instrumento');
    const planSeleccionado = params.get('plan');

    // 2. Referenciamos los selectores por su ID
    const selectInstrumento = document.getElementById('instrumento');
    const selectPlan = document.getElementById('plan');

    // 3. Si el parámetro 'instrumento' existe en la URL, lo marcamos
    if (instrumentoSeleccionado) {
        selectInstrumento.value = instrumentoSeleccionado;
    }

    // 4. Si el parámetro 'plan' existe en la URL, lo marcamos
    if (planSeleccionado) {
        selectPlan.value = planSeleccionado;
    }
});


// DATOS DEL FORMULARIO
formulario.addEventListener("submit", (e) => {
    
    const nombre = document.getElementById("nombre").value;
    const dniInput = document.getElementById("dni").value;
    const numeroInput = document.getElementById("telefono").value;
    const edadInput = document.getElementById("edad").value;
    const instrumento = document.getElementById("instrumento").value;

    if (!dniValido(dniInput)) {
        e.preventDefault(); // Detiene el envío si el DNI está mal
        alert("DNI inválido: Debe tener 8 dígitos numéricos.");
        return;
    }

    if (!numeroValido(numeroInput)) {
        e.preventDefault(); // Detiene el envío si el número está mal
        alert("Número telefónico inválido: Debe empezar con 9 y tener 9 dígitos.");
        return;
    }

    try {
        if (validarClasificacionEdad(parseInt(edadInput), instrumento)) {
            
            alert("¡Procesando reserva para " + nombre + "!");
        }
    } catch (error) {
        e.preventDefault(); // Detiene el envío si la edad no corresponde al instrumento
        alert(error.message); 
    }
});

function dniValido(dni) {
    const regexDni = /^[0-9]{8}$/;
    return regexDni.test(dni);
}

function numeroValido(numero) {
    const regexCelular = /^9[0-9]{8}$/;
    return regexCelular.test(numero);
}

function validarClasificacionEdad(edad, instrumento) {
    switch (instrumento) {
        case "aprestamiento":
            if (edad < 3 || edad > 5) throw new Error("Edad para Aprestamiento: 3 a 5 años.");
            return true;
        case "bateria":
            if (edad < 7) throw new Error("Edad para Batería: 7 años a más.");
            return true;
        case "violin":
            if (edad < 6) throw new Error("Edad para Violín: 6 años a más.");
            return true;
        case "guitarra-acustica":
        case "guitarra-electrica":
            if (edad < 7) throw new Error("Edad para Guitarra: 7 años a más.");
            return true;
        case "organo":
            if (edad < 6) throw new Error("Edad para Órgano: 6 años a más.");
            return true;
        case "canto":
            if (edad < 5) throw new Error("Edad para Canto: 5 años a más.");
            return true;
        default:
            return true;
    }
}