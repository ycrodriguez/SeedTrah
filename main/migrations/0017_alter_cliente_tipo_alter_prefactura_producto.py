# Generated by Django 4.2 on 2023-05-17 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_remove_venta_cant_vendida_remove_venta_valor_total_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tipo',
            field=models.CharField(choices=[('Persona Natural', 'Persona Natural'), ('Entidad Estatal', 'Entidad Estatal')], default='Persona Natural', max_length=255),
        ),
        migrations.AlterField(
            model_name='prefactura',
            name='producto',
            field=models.ManyToManyField(null=True, to='main.producto', verbose_name='Productos'),
        ),
    ]
