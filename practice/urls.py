from django.urls import path
from practice import views

urlpatterns = [
    path('signup', views.sign_up),
    path('', views.community_list, name='community_list'),
    path('community_delete', views.community_delete),
    path('post', views.post_list, name='post_list'),
    path('post_delete', views.post_delete),
]