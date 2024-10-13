from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', signin, name='login'),
    path('logout/', signout, name='logout'),
    path('profile/', profile, name='profile'),
    path('company/', company, name='company'),
]
