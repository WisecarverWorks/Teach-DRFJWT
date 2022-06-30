from django.urls import path
from assessment import views

urlpatterns = [
    path('assessment/', views.get_all_assessment),
    path('', views.user_assessment)
]
