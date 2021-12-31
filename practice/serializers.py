from django.db import models
from django.db.models import fields
from rest_framework import serializers
from practice.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'created_at', 'title', 'text']