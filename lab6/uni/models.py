from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return self.name