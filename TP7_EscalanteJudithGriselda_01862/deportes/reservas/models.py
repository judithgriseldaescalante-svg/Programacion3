from django.db import models

class ActividadDeportiva(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    lugar = models.CharField(max_length=100)
    cupo = models.IntegerField()

    def __str__(self):
        return self.nombre

class Horario(models.Model):
    actividad= models.ForeignKey(ActividadDeportiva, on_delete=models.CASCADE, related_name='horarios')
    dias_semana=[
        ("Lunes","Lunes"),
        ("Martes", "Martes"),
        ("Miercoles","Miercoles"),
        ("Jueves", "Jueves"),
        ("Viernes", "Viernes"),
        ("Sabado","Sabado"),
        ("Domingo","Domingo")
    ]
    dia= models.CharField(max_length=15, choices=dias_semana)
    hora_inicio= models.TimeField()
    hora_fin=models.TimeField()
    def __str__(self):
        return f"{self.actividad.nombre} - {self.dia} ({self.hora_inicio} a {self.hora_fin})"

class Inscripcion (models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=30)
    dni= models.IntegerField()
    fecha_inscripcion= models.DateField(auto_now_add=True)
    estado_inscripcion=[
        ("Activa", "Activa"),
        ("Cancelada","Cancelada")
    ]
    estado= models.CharField(max_length=10, choices=estado_inscripcion)
    horario=models.ForeignKey(Horario, on_delete=models.CASCADE, related_name='inscripcion')

    def __str__(self):
        return self.nombre
