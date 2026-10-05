document.addEventListener("DOMContentLoaded",()=>{
    //Ejercicio 3
    function Actividad (nombre,lugar,dia,horario,cupo,estado){
        this.nombre=nombre;
        this.lugar=lugar;
        this.dia=dia;
        this.horario=horario;
        this.cupo=cupo;
        this.estado=estado;
    }
    class SistemaDeportes{
        constructor (){
            this.actividades=[];
        }
        agregarActividad(actividadNueva){
            this.actividades.push(actividadNueva);
        }
        listarActividades(){
            return this.actividades;
        }
    }
    let sistema = new SistemaDeportes();
    let actividad1= new Actividad("Futbol","cancha de fuutbol 5","sabado","16:00",10,"completo");
    let actividad2= new Actividad("Basquet","cancha con iluminacion","martes","21:00",2,"disponible");
    let actividad3= new Actividad("Voley","cancha techada","jueves","9:00",11,"disponible");
    let actividad4= new Actividad("Atletismo","pista de entrenamiento","sabado","17:00",24,"completo");
    sistema.agregarActividad(actividad1);
    sistema.agregarActividad(actividad2);
    sistema.agregarActividad(actividad3);
    sistema.agregarActividad(actividad4);

    //Ejercicio 4
    const tabla= document.getElementById("cuerpoTabla");
    let listadoActividades = sistema.listarActividades();
    for (let actividad of listadoActividades){
        let fila = document.createElement("tr");
        fila.innerHTML=`
        <td>${actividad.nombre}</td>
        <td>${actividad.lugar}</td>
        <td>${actividad.dia}</td>
        <td>${actividad.horario}</td>
        <td>${actividad.cupo}</td>
        <td>${actividad.estado}</td>`;
        tabla.appendChild(fila);
    }
});   
 