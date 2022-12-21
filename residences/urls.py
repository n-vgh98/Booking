from django.urls import path, include
from residences import views


urlpatterns = [
    path('', views.ResidenceList.as_view(), name='residences_list'),
    path('<int:pk>', views.ResidenceDetail.as_view(), name='residences_detail')

]
