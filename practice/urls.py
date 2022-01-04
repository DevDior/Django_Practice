from django.urls import path
from practice import views

urlpatterns = [
    path('signup', views.sign_up),
    path('', views.community_list, name='community_list'),
    path('<int:pk>', views.community_detail),
    path('community_delete', views.community_delete),
    path('post/<int:community_pk>', views.post_list, name='post_list'),
    path('post/<int:community_pk>/<int:pk>', views.post_detail),
    path('post_delete', views.post_delete),
]