from django.db import models
from apps.accounts.models import User
from apps.company.models import JobModel

# Create your models here.

class ApplyJob(models.Model):
    STATUS_CHOICES = (
        ('submitted', 'Submitted'),
        ('reviewed', 'Reviewed'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )

    applicant = models.ForeignKey(User,on_delete=models.CASCADE)
    job = models.ForeignKey(JobModel,on_delete=models.CASCADE)
    cover_letter = models.TextField()
    application_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default="submitted")

    def __str__(self):
        return self.applicant.first_name

