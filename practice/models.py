from enum import unique
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone

from basic_practice.settings import AUTH_PASSWORD_VALIDATORS

class User(models.Model):
    SEX = [
        ('M', "Man"),
        ("G", "Girl"),
    ]
    
    user_id = models.CharField(max_length=30, primary_key=True, unique=True)
    user_pw = models.CharField(max_length=30)
    user_email = models.CharField(max_length=128, unique=True)
    user_name = models.CharField(max_length=30)
    user_nick_name = models.CharField(max_length=30)
    user_phone_num = models.CharField(max_length=30, unique=True)
    sex = models.CharField(max_length=2, choices=SEX)
    blocked = models.BooleanField(default=False)
    
class Community(models.Model):
    author_id = models.ForeignKey('User', on_delete=models.CASCADE, db_column='autor_id')
    
class Subject(models.Model):
    community_id = models.ForeignKey('Community', on_delete=models.CASCADE, db_column='community_id')
    subject = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    view_count = models.IntegerField()
    created_at = models.DateField(default=timezone.now)
    writer = models.ForeignKey('User', on_delete=models.CASCADE, db_column='writer_id')
    community_id = models.ForeignKey('Community', on_delete=models.CASCADE, db_column='community_id')
    
    class Meta:
        ordering = ['created_at']
        
class Comment(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, db_column='user_id')
    post_id = models.ForeignKey('Post', on_delete=CASCADE, db_column='post_id')
    text = models.TextField()
    created_at = models.DateField(default=timezone.now)