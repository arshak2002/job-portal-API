from django.shortcuts import render
from rest_framework import viewsets
from apps.company.models import JobModel
from apps.company.serializers import JobModelSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class JobsViewSet(viewsets.ModelViewSet):
    queryset = JobModel.objects.all()
    serializer_class = JobModelSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["title","category"]

