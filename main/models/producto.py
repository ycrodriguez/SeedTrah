from django.db import models


class Producto(models.Model):
    semilla = models.ForeignKey('main.Semilla', on_delete=models.SET_NULL, null=True)
    tipo = models.CharField(max_length=255, verbose_name='Tipo')
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    cantidad_existente = models.IntegerField(verbose_name='Cantidad Existente(Lb)')
    cantidad_vendida = models.IntegerField(verbose_name='Cantidad Vendida(Lb)')
    descripcion = models.CharField(max_length=255, verbose_name='Descripción', blank=True)
    total = models.IntegerField(verbose_name='Total')
    valor = models.FloatField(verbose_name='Valor(MN)')
    almacen = models.ForeignKey('main.Almacen', on_delete=models.CASCADE, verbose_name='Almacén')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.semilla.codigo
