# Generated by Django 5.0.3 on 2024-03-31 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.TextField(null=True, verbose_name='Descripcion')),
                ('cantidad', models.CharField(max_length=1000, verbose_name='Cantidad')),
            ],
        ),
    ]
