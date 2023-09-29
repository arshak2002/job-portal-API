from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.employee.views import ApplyJobViewSet

router = DefaultRouter()

router.register('apply-job',ApplyJobViewSet)

urlpatterns = [
    path('',include(router.urls)),
]