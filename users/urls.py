from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from users import views
from rest_framework_simplejwt import views as jwt_views


from users.views import LoginUser

urlpatterns = [
    path('', views.UserList.as_view(), name='user_list'),
    # path('profile/', views.ProfileList.as_view(), name='profile_list'),
    path('profile/<int:pk>', views.UserProfile.as_view(), name='user_pofile'),
    path('login', LoginUser.as_view(), name='login_user'),

]
