from .models import CustomUser
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """CreateUser view"""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
