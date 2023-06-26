# Generated by Django 4.2 on 2023-05-13 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_alter_venta_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='prefactura',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='producto',
        ),
        migrations.AddField(
            model_name='cliente',
            name='usuario',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='prefactura',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.cliente', verbose_name='Cliente'),
        ),
        migrations.AddField(
            model_name='prefactura',
            name='producto',
            field=models.ManyToManyField(to='main.producto', verbose_name='Productos'),
        ),
        migrations.AddField(
            model_name='venta',
            name='prefactura',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.prefactura', verbose_name='Prefactura'),
        ),
    ]
