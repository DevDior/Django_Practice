from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, get_list_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect('community_list')
        return JsonResponse(serializer.error, status=400)

@csrf_exempt
def community_list(request):
    if request.method == 'GET':
        communities = Community.objects.all()
        serializer = CommunitySerializer(communities, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)        
        serializer = CommunitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect('community_list')
        return JsonResponse(serializer.errors, status=400)

def community_detail(request, pk):
    if request.method == 'GET':
        community = get_object_or_404(Community, id=pk)
        serializer = CommunitySerializer(community)
        return JsonResponse(serializer.data, safe=False)
    
def community_delete(request):
    data = JSONParser().parse(request)
    community = get_object_or_404(Community, id=data['id'], author_id=data['user_id'])
    if request.method == 'DELETE':
        community.delete()
        return redirect('community_list')
    
@csrf_exempt
def post_list(request, community_pk):
    if request.method == 'GET':
        posts = get_list_or_404(Post, community_id=community_pk)
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect('post_list', community_pk)
        return JsonResponse(serializer.errors, status=400)

def post_detail(request, community_pk, pk):
    post = get_object_or_404(Post, community_id=community_pk, id=pk)
    if request.method == 'GET':
        serializer = PostSerializer(post, )
        serializer.data['view_count'] += 1
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def post_delete(request):
    data = JSONParser().parse(request)
    queryset = Post.objects.filter(writer=data['user_id']) | Post.objects.filter(community_id=data['community_id'])
    post = get_object_or_404(queryset, id=data['id'])
    if request.method == 'DELETE':
        post.delete()
        return redirect('post_list')
        
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
        
def comment_delete(request):
    data = JSONParser().parse(request)
    comment = get_object_or_404(Comment, id=data['id'], user_id=data['user_id'])
    if request.method == 'DELETE':
        comment.delete()
        return redirect('post_detail')