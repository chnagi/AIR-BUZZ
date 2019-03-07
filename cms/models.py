from django.db import models
class AirCrafts(models.Model):
	MSN = models.IntegerField(max_length=100,primary_key=True,reuired=True,validators=[MinValueValidator(0)])
	Name = models.CharField(max_length=100,required=True)
class Flights(models.Model):
	MSN=models.ForeignKey(AirCrafts,on_delete=models.CASCADE,required=True)
	HarnessLength = models.IntegerField(default=0,required=True,validators=[ MinValueValidator(0)])
	GrossWeight = models.IntegerField(default=0,required=True,validators=[MinValueValidator(0)])
	AtmosphericPressure = models.IntegerField(default=0,required=True,validators=[MinValueValidator(0)])
	FuelCapacity_left=models.IntegerField(default=0,required=True,validators=[MinValueValidator(0)])
	FuelCapacity_right=models.IntegerField(default=0,required=True,validators=[MinValueValidator(0)])
	FuelQuantity_left=models.IntegerField(default=0,required=True,validators=[MinValueValidator(0)])
	FuelQuantity_right=models.IntegrField(default=0,required=True),validators=[MinValueValidator(0)]
	Max_Altitude=models.IntegerField(default=0,required=True,validators=[MinValueValidator(0)])
	Flight_No=models.CharField(max_length=100,required=True)
