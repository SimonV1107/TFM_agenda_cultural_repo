# Generated by Django 4.2.1 on 2023-09-02 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locales', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='local',
            name='id',
        ),
        migrations.AlterField(
            model_name='local',
            name='nombre',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='local',
            name='ubicacion',
            field=models.CharField(max_length=50),
        ),
    ]
