from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class userProfile(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    date_of_birth = models.DateField()
    full_name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.full_name


class Department(models.Model):
    department = models.CharField(max_length=200, unique=True)
    link = models.URLField(max_length=220, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.department
