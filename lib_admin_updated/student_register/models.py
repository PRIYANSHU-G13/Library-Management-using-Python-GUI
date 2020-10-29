from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime,date

# Create your models here.

class Course(models.Model):
    title=models.CharField(max_length=10)

    class Meta:
        db_table="Course"

    def __str__(self):
        return self.title

class Student(models.Model):
    fullname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    mobile=models.CharField(max_length=14)
    DOB=models.DateField(auto_now_add=False,auto_now=False)
    regno=models.CharField(max_length=11)
    batch=models.CharField(max_length=10)
    fine=models.CharField(max_length=5)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)

    class Meta:
        db_table="Student"
    
    def __str__(self):
        return self.fullname
