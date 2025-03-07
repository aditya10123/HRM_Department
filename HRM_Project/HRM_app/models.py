from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=100, blank=True,null=True)
    department_description = models.TextField(default="", blank=True,null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)  
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.department_name
    
class Roles(models.Model):
    role_name = models.CharField(max_length=100, blank=True,null=True)
    role_description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.role_name   
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Employe_User(AbstractUser):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=100, unique=True)
    dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name="employees")
    role = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True, related_name="users")
    reporting_manager = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True,related_name="team_members")
    date_of_joining = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    username = models.CharField(max_length=150, unique=True, blank=False)
    password = models.CharField(max_length=128)  # Django stores hashed passwords

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_set",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_set",
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.reporting_manager:
            hr_admin = Employe_User.objects.filter(role__role_name="HR").first()
            self.reporting_manager = hr_admin if hr_admin else None
        super().save(*args, **kwargs)

    def _str_(self):
        return f"{self.first_name} {self.last_name} - {self.role.role_name if self.role else'No Role'}"
    
class Task(models.Model):

    task_id = models.AutoField(primary_key=True)
    task_title = models.CharField(max_length=100)
    task_description = models.TextField(max_length=300)
    task_priority = models.CharField(max_length=50, choices=[("High", "High"), ("Medium", "Medium"), ("Low", "Low")])
    start_date = models.DateField()
    end_date = models.DateField()
    task_type = models.CharField(max_length=50, choices=[("Individual", "Individual"), ("Team", "Team")])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.task_title


class TaskAssignment(models.Model):
    """Links tasks to employees who are assigned to them."""
    assignment_id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="assignments")
    employee = models.ForeignKey(Employe_User, on_delete=models.CASCADE, related_name="tasks")
    assigned_by = models.ForeignKey(
        Employe_User, on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_tasks"
    ) 
    assigned_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50,
        choices=[("Pending", "Pending"), ("In Progress", "In Progress"), ("Completed", "Completed")],
        default="Pending"
    )
    completed_at = models.DateTimeField(null=True, blank=True)
    assigned_by_name = models.CharField(max_length=255, null=True, blank=True)

    def _str_(self):
        return f"{self.task.task_title} - {self.employee.first_name}"



from django.db import models
from django.contrib.auth.models import User

# class PerformanceReview(models.Model):
#     REVIEW_PERIOD_CHOICES = [
#         ('Monthly', 'Monthly'),
#         ('Quarterly', 'Quarterly'),
#         ('Annual', 'Annual'),
#     ]

#     review_title = models.CharField(max_length=100)
#     review_date = models.DateField()
#     employee = models.ForeignKey(Employe_User, on_delete=models.CASCADE, related_name='reviews_received')
#     reviewed_by = models.ForeignKey(Employe_User, on_delete=models.CASCADE, related_name='reviews_given')
#     review_period = models.CharField(max_length=100, choices=REVIEW_PERIOD_CHOICES)
#     rating = models.IntegerField()
#     comments = models.TextField(max_length=300, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def str(self):
#         return f"{self.review_title} - {self.employee.username}"