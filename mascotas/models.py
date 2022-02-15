from django.db import models

# Create your models here.


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    domicilio = models.TextField()

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellidos)


class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad = models.IntegerField()
    foto = models.ImageField(upload_to="static/img/mascotas/", null=True, blank=True)
    fecha_rescate = models.DateField()
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    vacunas = models.ManyToManyField(Vacuna)

    def __str__(self):
        return self.nombre
