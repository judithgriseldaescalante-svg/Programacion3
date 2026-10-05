document.addEventListener("DOMContentLoaded",()=>{
    //Ejercicio 1
    const fechaNacimiento = document.getElementById("fecha-nacimiento")
    fechaNacimiento.addEventListener("change", ()=>{
        let fechaIngresada = new Date (fechaNacimiento.value);
        let fechaActual = new Date();
        if (fechaIngresada>fechaActual){
            alert("La fecha de nacimiento no puede ser posterior a la fecha actual");
        }
    })
    //Ejercicio 2
    const dniIngresado = document.getElementById("dni");
    const error = document.getElementById("error-dni");
    dniIngresado.addEventListener("change", ()=>{
        if(dniIngresado.value.length != 8){
            error.textContent = "El DNI debe contener 8 digitos";
        }
        else{
            error.textContent=" ";
        }
    })
})
