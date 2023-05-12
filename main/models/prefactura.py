from django.db import models

from main.models import Producto


class Prefactura(models.Model):
    costo_total = models.FloatField(verbose_name='Costo Total')
    costo_unitario = models.FloatField(verbose_name='Costo Unitario')
    lugar_recogida = models.CharField(max_length=255, verbose_name='Lugar de Recogida', blank=True)
    almacen = models.ForeignKey('main.Almacen', on_delete=models.CASCADE, verbose_name='Almacén')

    class Meta:
        verbose_name = 'Prefactura'
        verbose_name_plural = 'Prefacturas'

    def __str__(self):
        return '{}'.format(self.pk)

    @property
    def list_productos(self):
        array_prod = []
        productos = Producto.objects.filter(prefactura_id=self.pk)
        for p in productos:
            array_prod.append(p.semilla.codigo)
        return array_prod

    list_productos.fget.short_description = 'Listado de productos'
