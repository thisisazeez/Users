from django.db import models
from django.contrib.auth.models import AbstractUser


class myUser(AbstractUser):

    profile_picture = models.ImageField(upload_to='images/')
    mobile_number = models.CharField(max_length=12)
    myroles = models.CharField(max_length=50, null=True, blank=True, choices=(
        ('Management', 'Management'),
        ('Student','Student'),
        ('Academic_Staff', 'Teacher'),
        ('Non-Academic_Staff', 'Non-Academic'),
        ('none', 'none'),
    ))
