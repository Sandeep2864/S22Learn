from django.db import models

class Signup(models.Model):
    username = models.BigIntegerField(unique=True)  # Consider using a character field
    password = models.CharField(max_length=128)  # Increased password length

class Student(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Ensure unique names
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Registration(models.Model):
    first_name=models.CharField(max_length=30)
    mid_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    dob=models.DateField()
    branch=models.CharField(max_length=30)
    mail=models.CharField(max_length=30)
    cgpa=models.FloatField()
    tenthmarks=models.IntegerField()
    twelfthmarks=models.IntegerField()
    abcnumber=models.FloatField()