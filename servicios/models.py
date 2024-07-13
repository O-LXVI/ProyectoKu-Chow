from django.db import models

class Servicios(models.Model):
    servicio = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    mecanico = models.CharField(max_length=100)
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.servicio} - {self.mecanico}"

    @classmethod
    def get_by_id(cls, id):
        try:
            return cls.objects.get(pk=id)
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_by_servicio(cls, servicio):
        try:
            return cls.objects.get(servicio=servicio)
        except cls.DoesNotExist:
            return None
