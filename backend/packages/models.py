from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Package(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    os = models.CharField(max_length=30)
    student = models.CharField(max_length=100)
    date = models.DateField()