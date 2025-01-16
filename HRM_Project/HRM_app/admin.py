from django.contrib import admin
from .models import Department
# Register your models here.

class adminDepartmentmodel(admin.ModelAdmin):
    list_display = ['Department_Name','Department_Description']
admin.site.register(Department,adminDepartmentmodel)