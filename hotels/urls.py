from django.urls import path, include
from hotels import views


urlpatterns = [
    path('', views.HotelLists.as_view(), name='hotel_lists'),
    path('<int:pk>', views.HotelRoom.as_view(), name='hotel_rooms')

]
