from datetime import timedelta

from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.utils import timezone

from main.models import Prefactura


@receiver(pre_delete, sender=Prefactura)
def pre_delete_update_producto(sender, instance: Prefactura, **kwargs):
    try:
        producto = instance.producto.first()
        producto.cantidad_existente += instance.cantidad
        producto.save()
    except:
        pass


@receiver(pre_save, sender=Prefactura)
def pre_save_prefactura(sender, instance: Prefactura, **kwargs):
    fecha_limite = timezone.now() - timedelta(days=15)
    Prefactura.objects.filter(fecha__lte=fecha_limite).delete()
