from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from main.models import Venta


@receiver(post_save, sender=Venta)
def post_save_update_venta_producto(sender, instance: Venta, **kwargs):
    try:
        producto = instance.prefactura.producto.first()
        producto.cantidad_vendida += instance.prefactura.cantidad
        producto.save()
    except:
        pass


@receiver(post_delete, sender=Venta)
def post_delete_update_venta_producto(sender, instance: Venta, **kwargs):
    try:
        producto = instance.prefactura.producto.first()
        producto.cantidad_vendida -= instance.prefactura.cantidad
        producto.save()
    except:
        pass
