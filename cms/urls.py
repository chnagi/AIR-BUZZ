"""airbuzz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',index,name="index"),
    path('api/aircraft/<int:pk>',AirCrafts_primary,name="AirCrafts_detail"),
    path('api/flight/<int:pk>',Flights_primary,name="flight"),
    path('api/news/<int:pk>',News_primary,name="news"),
    path('api/aircraft/',AirCrafts_detail,name="Air"),
    path('api/flight/',Flights_detail,name="flight"),
    path('api/news/',News_detail,name="news"),
    path('aircraft/',aircraft,name="air"),

    
]
