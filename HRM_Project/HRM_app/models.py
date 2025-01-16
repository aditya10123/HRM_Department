from django.db import models

# Create your models here.

class Department(models.Model):
    Department_Name = models.CharField(max_length=100)
    Department_Description = models.TextField(blank=True,null=True)
    

