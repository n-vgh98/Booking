from django.contrib import admin
from django.urls import path, include
from users import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('', views.UserList.as_view(), name='user_list'),
    # path('profile/', views.ProfileList.as_view(), name='profile_list'),
    path('profile/<int:pk>', views.UserProfile.as_view(), name='user_pofile'),
    path('login', views.LoginUser.as_view(), name='login_user'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]
