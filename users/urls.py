from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path('', views.UserList.as_view(), name='user_list')
]
