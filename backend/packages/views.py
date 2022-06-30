from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
# Local
from .models import Package
from .serializers import PackageSerializer


# Get Function
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_packages(request):
    packages = Package.objects.all()
    serializer = PackageSerializer(packages, many=True)
    return Response(serializer.data)

# Post Function / Get Updated
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_packages(request):

    print('User', f"{request.user.id} {request.user.email} {request.user.username}")

    if request.method == 'POST':
        serializer = PackageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        packages = Package.objects.filter(user_id=request.user.id)
        serializer = PackageSerializer(packages, many=True)
        return Response(serializer.data)