from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class AirCrafts(models.Model):
	MSN = models.IntegerField(primary_key=True,validators=[MinValueValidator(0)])
	Name = models.CharField(max_length=100)
class Flights(models.Model):
	MSN=models.ForeignKey(AirCrafts,on_delete=models.CASCADE)
	HarnessLength = models.IntegerField(default=0,validators=[ MinValueValidator(0)])
	GrossWeight = models.IntegerField(default=0,validators=[MinValueValidator(0)])
	AtmosphericPressure = models.IntegerField(default=0,validators=[MinValueValidator(0)])
	FuelCapacity_left=models.IntegerField(default=0,validators=[MinValueValidator(0)])
	FuelCapacity_right=models.IntegerField(default=0,validators=[MinValueValidator(0)])
	FuelQuantity_left=models.IntegerField(default=0,validators=[MinValueValidator(0)])
	FuelQuantity_right=models.IntegerField(default=0,validators=[MinValueValidator(0)])
	Max_Altitude=models.IntegerField(default=0,validators=[MinValueValidator(0)])
	Flight_No=models.CharField(max_length=100)
