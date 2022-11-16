import email
from django.db import models
from django.contrib.auth.models import User


class profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=False, null=False)
    
    def __str__(self):
        return self.email
