from django.contrib import admin
from apps . company.models import JobModel,CompanyDetails

# Register your models here.


admin.site.register(JobModel)
admin.site.register(CompanyDetails)