from django.db import models


class Student(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    contact_no=models.IntegerField(max_length=12)
    email=models.EmailField(max_length=50)
    age=models.IntegerField(max_length=4)
