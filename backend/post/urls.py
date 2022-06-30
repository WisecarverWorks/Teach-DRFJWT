from django.urls import path
from post import views 

urlpatterns = [
    path('post/', views.get_all_posts),
    path('', views.user_post),
]
