from re import template
from urllib.parse import urlparse
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name ="newfeed"

urlpatterns = [
    path('', views.newfeed, name="newfeed"),
    path('add/', views.add_Post, name="addPost"),
    path('save/', views.save_Post, name="savePost"),
    path('404/', views.error, name='cocl'),
    path('<int:pk>/', views.posts, name='posts'),
]
