# Generated by Django 3.2.25 on 2024-11-11 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventasinventario', '0005_administrador_jefebodega'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='administrador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='ventasinventario.administrador'),
        ),
    ]
