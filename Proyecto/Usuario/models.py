from django.db import models

# Create your models here.

class Usuario(models.Model):
    dni = models.CharField(primary_key=True, max_length=8)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} / {1} / {2}"
        return texto.format(self.dni, self.nombres, self.apellidos)
