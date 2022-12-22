from django.urls import path, include
from flights import views


urlpatterns = [
    path('', views.FlightsList.as_view(), name='flights_list')

]
