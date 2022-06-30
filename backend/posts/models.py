from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    # We are uploading Images 
    image = models.ImageField(upload_to='post_images')

    def __str__(self):
        return self.title # we set this so that our function will return self title