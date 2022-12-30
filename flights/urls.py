from django.urls import path, include
from flights import views
from .views import *


urlpatterns = [
    path('', views.FlightsList.as_view(), name='flights_list'),
    path('reservation/', create_reservation, name='flight_passengers')

]
