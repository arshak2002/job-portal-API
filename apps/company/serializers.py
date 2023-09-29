from rest_framework import serializers
from apps.company.models import JobModel,CompanyDetails

class JobModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobModel
        fields = '__all__'

class CompanyDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyDetails
        fields = '__all__'