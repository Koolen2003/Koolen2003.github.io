from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.db import models

class StudentMark(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=50)
    module = models.CharField(max_length=100)
    computer_architecture = models.FloatField()
    networking = models.FloatField()
    r_programming = models.FloatField()


    
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    