# Generated by Django 5.0.3 on 2024-03-31 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes', verbose_name='Imagen'),
        ),
    ]