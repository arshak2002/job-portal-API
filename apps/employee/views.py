from django.shortcuts import render
from apps.employee.models import ApplyJob
from apps.employee.serializers import ApplyJobSerializer
from rest_framework import viewsets

# Create your views here.

class ApplyJobViewSet(viewsets.ModelViewSet):
    queryset = ApplyJob.objects.all()
    serializer_class = ApplyJobSerializer
