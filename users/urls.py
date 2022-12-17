from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path('', views.UserList.as_view(), name='user_list'),
    path('profile/', views.ProfileList.as_view(), name='profile_list'),
    path('profile/<int:pk>', views.UserProfile.as_view(), name='UserProfile'),
]
