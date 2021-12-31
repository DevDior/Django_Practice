from django.urls import path
from practice import views

urlpatterns = [
    path('', views.post_list),
]