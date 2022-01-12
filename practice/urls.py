from django.urls import path
from practice import views

urlpatterns = [
    # user
    path('signup', views.sign_up),
    path('user/<str:user_id>/<str:password>', views.check_user),
    path('user_update/<str:user_id>', views.user_update),
    
    #community
    path('', views.community_list, name='community_list'),
    path('<int:pk>/<str:user_id>', views.community_detail, name='community_detail'),
    
    #subject
    path('subject_post/<int:community_id>/<str:user_id>', views.subject_post),
    path('subject_detail/<int:community_id>/<int:subject_id>/<str:user_id>', views.subject_detail),
    
    #block
    path('block/<str:user_id>', views.block),
    
    #post
    path('post/<int:community_id>', views.post_list, name='post_list'),
    path('post/<int:community_id>/<int:pk>/<str:user_id>', views.post_detail, name='post_detail'),
    
    # comment
    path('comment_post/<int:community_id>/<int:pk>', views.comment_list),
    path('comment_detail/<str:user_id>/<int:pk>', views.comment_detail)
]