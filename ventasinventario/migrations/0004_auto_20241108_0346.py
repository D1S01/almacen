# Generated by Django 3.2.25 on 2024-11-08 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventasinventario', '0003_auto_20241108_0056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='modificacion',
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
