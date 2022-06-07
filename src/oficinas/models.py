from django.db import models

# Create your models here.
class Oficina(models.Model):
    persona = models.CharField(max_length = 25)
    identificador = models.IntegerField()
    fecha_inicio = models.DateField()
