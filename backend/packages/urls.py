from django.urls import path
from packages import views 
# Url endpoints for authentication
urlpatterns = [
    path('packages/', views.get_all_packages),
    path('', views.user_packages),
]
