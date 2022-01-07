from django.urls import path
from practice import views

urlpatterns = [
    path('signup', views.sign_up),
    path('', views.community_list, name='community_list'),
    path('<int:pk>/<str:user_id>', views.community_detail, name='community_detail'),
    path('block', views.block),
    path('post/<int:community_id>', views.post_list, name='post_list'),
    path('post/<int:community_id>/<int:pk>/<str:user_id>', views.post_detail, name='post_detail'),
    path('post_delete', views.post_delete),
    path('comment_create', views.comment_create),
    path('comment_delete/<str:user_id>/<int:pk>', views.comment_delete)
]