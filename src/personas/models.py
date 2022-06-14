from django.db import models

# Create your models here.
class Persona(models.Model):
    nombres=models.CharField(max_length=100, null=True)
    apellidos=models.CharField(max_length=100, blank=True)
    edad=models.IntegerField()
    donador=models.BooleanField(default=False)