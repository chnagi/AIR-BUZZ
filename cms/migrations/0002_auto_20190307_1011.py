# Generated by Django 2.1.7 on 2019-03-07 04:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircrafts',
            name='MSN',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]