from django.db import models


class Prefactura(models.Model):
    costo_total = models.FloatField(verbose_name='Costo Total(MN)')
    costo_unitario = models.FloatField(verbose_name='Costo Unitario(MN)')
    cantidad = models.FloatField(verbose_name='Cantidad a Comprar(Lb)', null=True)
    lugar_recogida = models.CharField(max_length=255, verbose_name='Lugar de Recogida', blank=True)
    fecha = models.DateTimeField(auto_now=True)
    almacen = models.ForeignKey('main.Almacen', on_delete=models.CASCADE, verbose_name='Almacén')
    cliente = models.ForeignKey('main.Cliente', on_delete=models.CASCADE, verbose_name='Cliente', null=True)
    producto = models.ManyToManyField('main.Producto', verbose_name='Productos')

    class Meta:
        verbose_name = 'Prefactura'
        verbose_name_plural = 'Prefacturas'

    def __str__(self):
        return '{}'.format(self.pk)
