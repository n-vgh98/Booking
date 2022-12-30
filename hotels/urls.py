from django.urls import path, include
from hotels import views
from .views import *

urlpatterns = [
    path('', views.HotelLists.as_view(), name='hotels_list'),
    path('<int:pk>', views.HotelDetail.as_view(), name='hotel_rooms'),
    path('<int:pk>/passenger/', create_reservation, name='hotel_room_passenger_reservation')

]
