from django.contrib import admin
from .models import Department
# Register your models here.

class adminDepartmentmodel(admin.ModelAdmin):
    list_display = ['department_name','department_description']
admin.site.register(Department,adminDepartmentmodel)