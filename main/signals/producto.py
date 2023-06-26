from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

from main.models import Producto


@receiver(post_delete, sender=Producto)
def delete_imagen_posdelete(sender, instance: Producto, **kwargs):
    if instance.imagen:
        try:
            os.remove(instance.imagen.path)
        except:
            print('Error')
