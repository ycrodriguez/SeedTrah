from django.db import models


class EntidadEstatal(models.Model):
    numero_inscripcion = models.PositiveBigIntegerField(verbose_name='Número de Inscripción')
    tipo = models.CharField(max_length=255, verbose_name='Tipo')

    class Meta:
        verbose_name = 'Entidad Estatal'
        verbose_name_plural = 'Entidades Estatales'

    def __str__(self):
        return str(self.numero_inscripcion)
