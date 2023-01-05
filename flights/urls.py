from django.urls import path, include
from flights import views
from .views import *


urlpatterns = [
    path('', views.FlightsList.as_view(), name='flights_list'),
    path('<int:pk>/reservation/', CreateReservation.as_view(), name='flight_passengers')

]
