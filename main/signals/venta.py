from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from main.models import Venta, Prefactura


@receiver(post_save, sender=Venta)
def post_save_update_venta_producto(sender, instance: Venta, **kwargs):
    try:
        for p in instance.prefactura.producto.all():
            p.cantidad_vendida += instance.prefactura.cantidad
            if p.cantidad_existente == 0:
                prefacturas = p.prefactura_set.all()
                if prefacturas.count() == prefacturas.filter(venta__isnull=False).count():
                    p.delete()
                    return
            p.save()
    except Exception as e:
        print('ERROR', e)


@receiver(post_delete, sender=Venta)
def post_delete_update_venta_producto(sender, instance: Venta, **kwargs):
    try:
        producto = instance.prefactura.producto.first()
        producto.cantidad_vendida -= instance.prefactura.cantidad
        producto.save()
    except:
        pass
