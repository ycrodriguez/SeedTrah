from django.db import models
from django.utils import timezone


class Venta(models.Model):
    lugar_compra = models.CharField(max_length=255, verbose_name='Lugar de Compra')
    valor_total = models.FloatField(verbose_name='Valor total', default=0)
    cant_vendida = models.IntegerField(verbose_name='Cantidad Vendida', default=0)
    fecha = models.DateTimeField(verbose_name='Fecha', default=timezone.now)
    cliente = models.ForeignKey('main.Cliente', on_delete=models.CASCADE, verbose_name='Cliente')
    producto = models.ManyToManyField('main.Producto')

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    def __str__(self):
        return 'Venta {}'.format(self.pk)
