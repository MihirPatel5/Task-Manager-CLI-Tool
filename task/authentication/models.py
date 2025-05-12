from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.permissions import BasePermission


STATUS =[
    ('completed', 'compeleted'),
    ('in_progres', 'in_progres'),
    ('suspended', 'suspended')
]

# class TaskManager(models.Manager):
#     def add_task(self):

class User(AbstractUser):
    pass

class Profile(models.Model):
    ROLE_CHOICE = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICE, default='employee')

class Task(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    status = models.CharField(choices=STATUS, max_length=50)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()

class IsAdminOrManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.profile.role in ['admin', 'manager']
