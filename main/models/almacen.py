from django.db import models


class Almacen(models.Model):
    codigo = models.CharField(max_length=255, verbose_name='Código')
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    capacidad = models.FloatField(verbose_name='Capacidad')
    direccion = models.CharField(max_length=255, verbose_name='Dirección')
    empresa = models.ForeignKey('main.Empresa', on_delete=models.CASCADE, verbose_name='Empresa')

    class Meta:
        verbose_name = 'Almacén'
        verbose_name_plural = 'Almacenes'

    def __str__(self):
        return self.codigo
