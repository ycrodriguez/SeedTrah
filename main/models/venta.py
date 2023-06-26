from django.db import models
from django.utils import timezone


class Venta(models.Model):
    lugar_compra = models.CharField(max_length=255, verbose_name='Lugar de Compra')
    fecha = models.DateTimeField(verbose_name='Fecha', default=timezone.now)
    prefactura = models.OneToOneField('main.Prefactura', on_delete=models.CASCADE, verbose_name='Prefactura', null=True)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    def __str__(self):
        return 'Venta {}'.format(self.pk)
