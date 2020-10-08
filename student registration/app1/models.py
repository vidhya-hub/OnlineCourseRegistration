from django.db import models


class StudentModel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=10)
    photo=models.ImageField(upload_to="student_images/")
