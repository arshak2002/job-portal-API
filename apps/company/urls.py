from django.urls import path,include
from rest_framework.routers import DefaultRouter
from apps.company.views import JobsViewSet

router = DefaultRouter()
router.register('jobs',JobsViewSet)

urlpatterns = [
    path('',include(router.urls)),
]