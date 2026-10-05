//Ejercicio 5
document.addEventListener("DOMContentLoaded",()=>{
    const btnGenerar = document.getElementById("btnGenerar");
    const inputCantidad = document.getElementById("cantidadParticipantes");
    const contenedor = document.getElementById("contenedorParticipantes");
    if (btnGenerar) {
        btnGenerar.addEventListener("click", () => {
            let cantidad = parseInt(inputCantidad.value);
            contenedor.innerHTML = "";
            for (let i = 1; i <= cantidad; i++) {
                let tarjeta = document.createElement("div");
                tarjeta.classList.add("tarjeta-deporte", "mt-4");
                tarjeta.innerHTML = `
                    <fieldset>
                        <legend>Participante ${i}</legend>
                        <div class="mb-3">
                            <label class="form-label">Apellido y Nombre:</label>
                            <input type="text" class="form-control" required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">DNI:</label>
                            <input type="number" class="form-control" required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Fecha de nacimiento:</label>
                            <input type="date" class="form-control" required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Sexo:</label>
                            <select class="form-control">
                                <option value="masculino">Masculino</option>
                                <option value="femenino">Femenino</option>
                                <option value="otro">Otro</option>
                            </select>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Nivel:</label>
                            <input type="text" class="form-control">
                        </div>
                    </fieldset>`;
                contenedor.appendChild(tarjeta);
            }
        });
    }
})

