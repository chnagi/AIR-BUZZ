# Generated by Django 2.1.7 on 2019-03-07 04:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirCrafts',
            fields=[
                ('MSN', models.IntegerField(max_length=100, primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0)])),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HarnessLength', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('GrossWeight', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('AtmosphericPressure', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('FuelCapacity_left', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('FuelCapacity_right', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('FuelQuantity_left', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('FuelQuantity_right', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('Max_Altitude', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('Flight_No', models.CharField(max_length=100)),
                ('MSN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.AirCrafts')),
            ],
        ),
    ]
