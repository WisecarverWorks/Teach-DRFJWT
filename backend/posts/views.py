from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth.models import User
from .models import Post
from .serializers import PostSerializer


## Create views here

class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

def get_all_posts(self, request, *args, **kwargs):
    post = Post.objects.all()
    serializer = PostSerializer(post, many=True)
    return Response(serializer.data)

def user_posts(self, request, *args, **kwargs):
    posts_serializer = PostSerializer(data=request.data)
    if PostSerializer.is_valid():
     PostSerializer.save()
     return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
    else:
     print('error', posts_serializer.errors)
     return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)