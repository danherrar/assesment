# Generated by Django 3.2.5 on 2021-07-14 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storelocation',
            name='latitud',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='storelocation',
            name='longitud',
            field=models.FloatField(),
        ),
    ]
