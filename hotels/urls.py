from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from users import views
from rest_framework_simplejwt import views as jwt_views


from users.views import LoginUser

urlpatterns = [
    path('', views.UserList.as_view(), name='user_list'),


]
