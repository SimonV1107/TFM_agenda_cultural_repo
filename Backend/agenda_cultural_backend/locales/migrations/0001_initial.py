# Generated by Django 4.2.1 on 2023-09-02 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('ubicacion', models.DateField()),
                ('telefono', models.CharField(max_length=50)),
                ('web', models.CharField(max_length=50)),
            ],
        ),
    ]