from django.shortcuts import render
from apps.accounts.models import User
from apps.accounts.serializers import UserSerializer,UserLoginSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics
from apps .employee.models import EmployeeDetails
from apps.company.models import CompanyDetails

# Create your views here.

class UserRegister(generics.CreateAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            obj = serializer.instance
            if obj.type_of == True:
                CompanyDetails.objects.create(
                   user=obj
                )
            
            EmployeeDetails.objects.create(
                name=obj
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

