from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Assessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=500)
    date = models.DateField()
    