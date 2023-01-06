from django.urls import path, include
from hotels import views
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'comments', HotelComment, basename='comments')



urlpatterns = [
    path('', views.HotelLists.as_view(), name='hotels_list'),
    path('<int:pk>', views.HotelDetail.as_view(), name='hotel_rooms'),
    path('<int:pk>/rate/', views.RateHotel.as_view(), name='hotel_rates'),
    # path('<int:pk>/comment/', views.HotelComment.as_view(), name='hotel_comments'),
    path('<int:pk>/passenger/', views.CreateReservation.as_view(), name='hotel_room_passenger_reservation')

]

urlpatterns += router.urls