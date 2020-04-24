from django.urls import path
from .views import LoginUser, RegisterUser, LogoutUser

urlpatterns = [
    path('login/', LoginUser, name='login'),
    path('register/', RegisterUser, name='register'),
    path('logout/', LogoutUser, name='logout'),
]
