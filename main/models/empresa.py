from django.db import models


class Empresa(models.Model):
    codigo = models.CharField(max_length=255, verbose_name='Código', unique=True)
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    correo = models.EmailField(verbose_name='Correo', blank=True)
    direccion = models.CharField(max_length=255, verbose_name='Dirección', blank=True)
    mision = models.CharField(max_length=255, verbose_name='Misión', blank=True)
    vision = models.CharField(max_length=255, verbose_name='Visión', blank=True)
    telefono = models.CharField(max_length=255, verbose_name='Teléfono', blank=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresa'

    def __str__(self):
        return self.nombre
