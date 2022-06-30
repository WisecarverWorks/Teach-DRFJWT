from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.get_all_posts),
    path('', views.user_posts),
]
