from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from importlib.metadata import requires
from pyexpat import model
from turtle import title
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user) # to get author's name


# create database for post
class Post_content(models.Model):  
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=get_current_user)  # create post's author
    content = models.TextField(max_length=10000, blank=False, null=False)  # create content of post
    image = models.ImageField(upload_to = "image", blank=True)  # create a place to store images
    time_create = models.DateTimeField(auto_now_add=True)  # create post time
    
    def __str__(self):
        return self.content
    
    
# create database for comment
class Comment(models.Model):
    post = models.ForeignKey(Post_content, on_delete=models.CASCADE)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=get_current_user)
    user_comment = models.CharField(max_length=10000, blank=False, null=False)
    image_comment = models.ImageField(upload_to = "comment", blank=True)
    time_comment = models.DateTimeField(auto_now_add=True)
    
    

    
    
    
        
    