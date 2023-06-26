from django.db import models


class Semilla(models.Model):
    codigo = models.CharField(max_length=255, verbose_name='Código', unique=True)
    nombre = models.CharField(max_length=255, verbose_name='Nombre')

    class Meta:
        verbose_name = 'Semilla'
        verbose_name_plural = 'Semillas'

    def __str__(self):
        return self.nombre
