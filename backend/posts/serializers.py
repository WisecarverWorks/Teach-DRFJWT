from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'content', 'title', 'image', 'user_id',]# This allows all serializer data to be accepted and passed 