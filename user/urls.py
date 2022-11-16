from urllib.parse import urlparse
from django.urls import path
from . import views



urlpatterns = [
    path('login', views.login_user, name='login'),
    path('register', views.register_user, name='register_user'),
    path('logout', views.logout_user, name='logout'),
]
