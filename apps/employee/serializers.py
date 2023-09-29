from rest_framework import serializers
from apps.employee.models import ApplyJob

class ApplyJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyJob
        fields = '__all__'