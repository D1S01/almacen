# Generated by Django 3.2.25 on 2024-11-08 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventasinventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.ManyToManyField(to='ventasinventario.Producto')),
            ],
        ),
    ]
