from django.shortcuts import render
from . models import *
from . serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
def index(request):
    return render(request,"cms/index.html")

def aircraft(request):
    planes = AirCraftsSerializer(AirCrafts.objects.all(),many=True)
    data = planes.data
    return render(request,"cms/aircraft.html",{"airdata":data})
def flights(request):
    flight = FlightsSerializer(Flights.objects.all(),many=True)
    data = flight.data
    return render(request,"cms/flight.html",{"flightdata":data})
def news(request):
    News = NewsFeedSerializer(NewsFeed.objects.all(),many=True)
    data = News.data
    return render(request,"cms/news.html",{"News":data})

@api_view(['GET', 'PUT', 'DELETE'])
def AirCrafts_detail(request):
    Aircraft_data=AirCrafts.objects.all()
    if request.method == 'GET':
        serializer = AirCraftsSerializer(Aircraft_data,many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AirCraftsSerializer(Aircraft_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
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
