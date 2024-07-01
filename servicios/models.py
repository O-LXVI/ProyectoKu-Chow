from django.db import models

class Servicios(models.Model):
    servicio = models.CharField(max_length=100)  # Puedes ajustar el max_length según tus necesidades
    valor = models.DecimalField(max_digits=10, decimal_places=2)  # max_digits y decimal_places son ajustables
    mecanico = models.CharField(max_length=100)  # Puedes ajustar el max_length según tus necesidades
    descripcion = models.TextField()  # Campo adicional que puede ser cualquier cosa, aquí se usa un texto

    def __str__(self):
        return f"{self.servicio} - {self.mecanico}"
