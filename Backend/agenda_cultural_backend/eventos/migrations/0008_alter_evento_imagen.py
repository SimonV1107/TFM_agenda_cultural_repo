# Generated by Django 4.2.1 on 2023-09-12 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0007_remove_evento_ubicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='imagen',
            field=models.ImageField(upload_to='blog/%Y/%m/%d'),
        ),
    ]
