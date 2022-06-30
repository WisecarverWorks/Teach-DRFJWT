from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
# Same dir
from .models import Assessment
from .serializers import AssessmentSerializer
# Create your views here.

# Get Function
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_assessment(request):
    assessments = Assessment.objects.all()
    serializer = AssessmentSerializer(assessments, many=True)
    return Response(serializer.data)

# Get Post Function
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_assessment(request):

    print('User' f"{request.user.id} {request.user.email} {request.user.username}")

    if request.method == 'POST':
        serializer = AssessmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        assessments = Assessment.objects.filter(user_id=request.user.id)
        serializer = AssessmentSerializer(assessments, many=True)
        return Response(serializer.data)