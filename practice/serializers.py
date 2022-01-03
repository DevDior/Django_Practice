from django.db.models import fields
from rest_framework import serializers
from rest_framework.utils import field_mapping
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'user_pw', 'user_email', 'user_name', 'user_nick_name', 'user_phone_num', 'sex', 'blocked')

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'community_id', 'subject')
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    subjects = SubjectSerializer()
    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'view_count', 'created_at', 'writer', 'community_id', 'comments')
        
class CommunitySerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    subjects = SubjectSerializer(many=True, read_only=True)
    
    class Meta:
        model = Community
        fields = ('id', 'author_id', 'subjects', 'posts')