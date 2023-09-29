from django.db import models
from apps.accounts.models import User

# Create your models here.

class JobModel(models.Model):
    category = models.CharField(max_length=50,null=True,blank=True)
    title = models.CharField(max_length=225)
    company = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField()
    location = models.CharField(max_length=225)
    salary = models.DecimalField(decimal_places=2,max_digits=10)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


