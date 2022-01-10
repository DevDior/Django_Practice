from django.http import HttpResponse
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
def block(request):
    data = JSONParser().parse(request)
    
    if request.method == 'POST':
        community = get_object_or_404(Community, id=data['community_id'])
        
        if data['author_id'] == community.author_id_id:
            # 이미 user가 blocke된 경우
            if Blocked_User.objects.filter(blocked_user_id_id=data['blocked_user_id'], community_id_id=data['community_id']).exists() == True:
                return HttpResponse("Already blocked user")
            
            # 커뮤니티 주인이 자기를 block할 경우    
            if data['author_id'] == data['blocked_user_id']:
                return HttpResponse("Please cherish yourself.")
        
            posts = Post.objects.filter(writer=data['blocked_user_id'], community_id=data['community_id'])
            comments = Comment.objects.filter(user_id_id=data['blocked_user_id'], post_id_id__community_id_id=data['community_id'])
            posts.delete()
            comments.delete()
            
            serializer = Blocked_UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return redirect('community_detail', data['community_id'], data['author_id'])
            return JsonResponse(serializer.errors, status=400)
        else:
            return HttpResponse("Don't block user, Permission denied")
    
    elif request.method == 'DELETE':
        community = get_object_or_404(Community, id=data['community_id'])
        
        if data['user_id'] == community.author_id:
            blocked_user = get_object_or_404(Blocked_User, user_id=data['blocked_user_id'])
            blocked_user.delete()
            return redirect('community_detail', data['community_id'])
        else:
            return HttpResponse("Don't unblock user, Permission denied")
        
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

@csrf_exempt
def community_detail(request, pk, user_id):
    if request.method == 'GET' and Blocked_User.objects.filter(blocked_user_id_id=user_id).exists() == False:
        community = get_object_or_404(Community, id=pk)
        serializer = CommunitySerializer(community)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'GET' and Blocked_User.objects.filter(blocked_user_id_id=user_id).exists() == True:
        return HttpResponse("Your id blocked")
    
    elif request.method =='DELETE':
        community = get_object_or_404(Community, id=pk)
        if community.author_id_id == user_id:
            community.delete()
            return redirect('community_list')
        else:
            return HttpResponse("You don't have delete permission")
    
@csrf_exempt
def post_list(request, community_id):
    if request.method == 'GET':
        posts = get_list_or_404(Post, community_id=community_id)
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        filter 
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect('post_list', community_id)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def post_detail(request, community_id, pk, user_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, community_id=community_id, id=pk)
        post.view_count += 1
        post.save()
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'DELETE':
        post = get_object_or_404(Post, id=pk)
        if post.writer_id == user_id or post.community_id.author_id_id == user_id:
            post.delete()
            return redirect('post_list', community_id)
        else:
            return HttpResponse("you don't have delete permission")

@csrf_exempt
def comment_create(request, community_id, pk):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect('post_detail', community_id, pk, data['user_id'])
        return JsonResponse(serializer.errors, status=400)
        
@csrf_exempt
def comment_delete(request, user_id, pk):
    comment = get_object_or_404(Comment, id=pk, user_id=user_id)
    post = get_object_or_404(Post, id=comment.post_id_id)
    post_id = post.id
    communtiy_id = post.community_id_id
    if request.method == 'DELETE':
        comment.delete()
        return redirect('post_detail', communtiy_id, post_id, user_id)