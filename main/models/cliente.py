from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    direccion = models.CharField(max_length=255, verbose_name='Dirección')
    telefono = models.CharField(max_length=255, verbose_name='Teléfono', blank=True)
    empresa = models.ForeignKey('main.Empresa', on_delete=models.CASCADE)
    persona_natural = models.OneToOneField('main.PersonaNatural', on_delete=models.CASCADE, null=True, blank=True,
                                           verbose_name='Persona Natural')
    entidad_estatal = models.OneToOneField('main.EntidadEstatal', on_delete=models.CASCADE, null=True, blank=True,
                                           verbose_name='Entidad Estatal')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nombre
