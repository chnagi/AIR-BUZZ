from rest_framework import serializers
from .models import *

class AirCraftsSerializer(serializers.ModelSerializer):
	class Meta:
		model=AirCrafts
		fields='__all__'
class FlightsSerializer(serializers.ModelSerializer):
	class Meta:
		model=Flights
		fields='__all__'
class NewsFeedSerializer(serializers.ModelSerializer):
	class Meta:
		model=NewsFeed
		fields='__all__'
