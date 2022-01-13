from django.db.models import fields
from rest_framework import serializers
from rest_framework.utils import field_mapping
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    writer = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = '__all__'
        
    def get_writer(self, instance):
        writer = instance.user_id.user_nick_name + '(' + instance.user_id_id + ')'
        return writer
        
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    writer = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = '__all__'
        
    def get_writer(self, instance):
        writer = instance.user_id.user_nick_name + '(' + instance.user_id_id + ')'
        return writer
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['subject'] = SubjectSerializer(instance.subject).data
        return response
        
class Blocked_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blocked_User
        fields = '__all__'
        
class CommunitySerializer(serializers.ModelSerializer):
    posts = PostSerializer(many = True, read_only = True)
    blocks = Blocked_UserSerializer(many = True, read_only = True)
    subjects = SubjectSerializer(many = True, read_only = True)
    
    class Meta:
        model = Community
        fields = '__all__'