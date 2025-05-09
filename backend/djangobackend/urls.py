from django.contrib import admin
from django.urls import path
from dota_app.views import get_rosterdata, get_herodata

urlpatterns = [
    path('roster', get_rosterdata), #for getting all data
    path('hero/<str:hero_id>', get_herodata) #for getting specific data
]
