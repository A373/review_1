# Generated by Django 3.2.3 on 2021-05-26 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ola_cab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_type',
            field=models.CharField(choices=[('Ac', 'Ac'), ('General', 'General')], max_length=255),
        ),
    ]
