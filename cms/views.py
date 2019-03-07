from django.shortcuts import render
from . models import *
from . serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return render(request,"cms/index.html")

def aircraft(request):
    planes = AirCraftsSerializer(AirCrafts.objects.all(),many=True)
    data = planes.data
    flight = FlightsSerializer(Flights.objects.all(),many=True)
    data2 = flight.data
    return render(request,"cms/aircraft.html",{"airdata":data,"flights":data2})

def flights(request):
    flight = FlightsSerializer(Flights.objects.all(),many=True)
    data = flight.data
    return render(request,"cms/flight.html",{"flightdata":data})

def news(request):
    News = NewsFeedSerializer(NewsFeed.objects.all(),many=True)
    data = News.data
    return render(request,"cms/news.html",{"News":data})

@csrf_exempt
@api_view(['GET', 'POST', 'DELETE'])
def AirCrafts_primary(request,pk):
    Aircraft_data = AirCrafts.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = AirCraftsSerializer(Aircraft_data)
        return Response(serializer.data)



@csrf_exempt
@api_view(['GET', 'POST', 'DELETE'])
def AirCrafts_detail(request):
    Aircraft_data = AirCrafts.objects.all()
    if request.method == 'GET':
        serializer = AirCraftsSerializer(Aircraft_data,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
    	#data=JSONParser().parse(request)
    	serializer = AirCraftsSerializer(data=request.data)
    	if serializer.is_valid():
    		serializer.save()
    		return Response(serializer.data)
    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@csrf_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Flights_detail(request):
    flight_data=Flights.objects.all()
    if request.method == 'GET':
        serializer = FlightsSerializer(flight_data,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FlightsSerializerPOST(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Flights_primary(request,pk):
    flight_data=Flights.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = FlightsSerializer(flight_data)
        return Response(serializer.data)


@csrf_exempt
@api_view(['GET', 'POST', 'DELETE'])
def News_detail(request):
    News_data=NewsFeed.objects.all()
    if request.method == 'GET':
        serializer = NewsFeedSerializer(News_data,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NewsFeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST', 'DELETE'])
def News_primary(request,pk):
    News_data=NewsFeed.objects.get(pk)
    if request.method == 'GET':
        serializer = NewsFeedSerializer(News_data)
        return Response(serializer.data)


