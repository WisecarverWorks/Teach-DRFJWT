from rest_framework import serializers
from .models import Assessment 

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ['id', 'title', 'body', 'date', 'user_id']
        