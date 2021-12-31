from django.db import models
from django.utils import timezone

from basic_practice.basic_practice.settings import AUTH_PASSWORD_VALIDATORS

class User(models.Model):
    SEX = [
        ('M', "Man"),
        ("G", "Girl"),
    ]
    
    user_id = models.CharField(max_length=50, unique=True)
    user_pw = models.CharField(max_length=50)
    user_email = models.CharField(max_length=128)
    user_name = models.CharField(max_length=50)
    user_nick_name = models.CharField(max_length=50)
    user_phone_nub = models.PhoneNumberField(unique=True)
    sex = models.CharField(max_length=2, choices=SEX)
    blocked = models.BooleanField(default=False)
    
class Community(models.Model):
    author = 
    
class Post(models.Model):
    created_at = models.DateField(default=timezone.now)
    title = models.CharField(max_length=100)
    text = models.TextField()
    
    class Meta:
        ordering = ['created_at']