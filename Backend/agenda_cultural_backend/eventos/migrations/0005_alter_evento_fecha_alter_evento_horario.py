# Generated by Django 4.2.1 on 2023-09-02 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0004_evento_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='evento',
            name='horario',
            field=models.CharField(max_length=50),
        ),
    ]