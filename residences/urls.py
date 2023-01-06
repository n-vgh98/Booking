from django.urls import path, include
from residences import views
from .views import *


urlpatterns = [
    path('', views.ResidenceList.as_view(), name='residences_list'),
    path('<int:pk>', views.ResidenceDetail.as_view(), name='residences_detail'),
    path('<int:pk>/passenger/', CreateReservation.as_view(), name='residence_passenger_reservation'),
    path('<int:pk>/rate/', views.ResiddenceRate.as_view(), name='residence_rates'),

]
