# Generated by Django 3.2.3 on 2021-05-26 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ola_cab', '0003_alter_slotbooking_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slotbooking',
            name='customer_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ola_cab.customer', unique=True),
        ),
    ]
