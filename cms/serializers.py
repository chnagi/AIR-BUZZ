from rest_framework import serializers
from .models import *

class AirCrafts(serializers.ModelSerializer):
	class Meta:
		model=AirCrafts
		fields='__all__'
class Flights(serializers.ModelSerializer):
	class Meta:
		model=Flights
		fields='__all__'
