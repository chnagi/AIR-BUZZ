from django.shortcuts import render
from . models import *
from . serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
# Create your views here.
def index(request):
    return render(request,"cms/index.html")
    

@api_view(['GET', 'PUT', 'DELETE'])
def AirCrafts_detail(request):
    Aircraft_data=AirCrafts.obects.all()
    if request.method == 'GET':
        serializer = AirCraftsSerializer(Aircraft_data,many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AirCraftsSerializer(Aircraft_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def Flights_detail(request):
    flight_data=Flights.objects.all()
    if request.method == 'GET':
        serializer = FlightsSerializer(flight_data,many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FlightsSerializer(flight_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def News_detail(request):
    News_data=NewsFeed.obects.all()
    if request.method == 'GET':
        serializer = NewsFeedSerializer(News_data,many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NewsFeedSerializer(News_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


