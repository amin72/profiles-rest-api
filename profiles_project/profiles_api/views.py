from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from .serializers import UserProfileSerializer
from .models import UserProfile
from .permissions import UpdateOwnProfile


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [UpdateOwnProfile]
