# Generated by Django 4.2.1 on 2023-11-02 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locales', '0005_alter_local_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='imagen',
            field=models.ImageField(upload_to='images/locals/'),
        ),
    ]
