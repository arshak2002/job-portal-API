from rest_framework import serializers
from apps.employee.models import ApplyJob,EmployeeDetails

class ApplyJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyJob
        fields = '__all__'

class EmployeeDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeDetails
        fields = '__all__'