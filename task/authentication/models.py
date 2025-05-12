from django.db import models
from django.contrib.auth.models import AbstractUser


STATUS =[
    ('completed', 'compeleted'),
    ('in_progres', 'in_progres'),
    ('suspended', 'suspended')
]
class Task(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    status = models.CharField(choices=STATUS, max_length=50)

# class TaskManager(models.Manager):
#     def add_task(self):

class User(AbstractUser):
    pass
