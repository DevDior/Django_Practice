from django.db.models import fields
from rest_framework import serializers
from rest_framework.utils import field_mapping
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many = True, read_only = True)
    class Meta:
        model = Post
        fields = '__all__'
        
        
class Blocked_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blocked_User
        fields = '__all__'
        
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
        
class CommunitySerializer(serializers.ModelSerializer):
    posts = PostSerializer(many = True, read_only = True)
    blocks = Blocked_UserSerializer(many = True, read_only = True)
    subjects = SubjectSerializer(many = True, read_only = True)
    
    class Meta:
        model = Community
        fields = '__all__'