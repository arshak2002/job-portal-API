from django.shortcuts import render
from apps.accounts.models import User
from apps.accounts.serializers import UserSerializer,UserLoginSerializer
from rest_framework import permissions

from rest_framework import generics

# Create your views here.

class UserRegister(generics.CreateAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]