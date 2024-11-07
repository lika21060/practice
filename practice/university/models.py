from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255, )
surname=models.CharField(max_length=225)
birth_date=models.DateTimeField()


class Profile(models.Model):
    Student=models.OneToOneField('university.Student',
related_name='profile',
on_delete=models.CASCADE,
)
phone_number=models.CharField(max_length=225)
address=models.CharField(max_length=225)

class Course(models.Model):
    title=models.CharField(max_length=225)
description=models.TextField()

class Professor(models.Model):
    name=models.CharField(max_length=225)
surname=models.CharField(max_length=225)
Courses=models.ManyToManyField('university.Course',
related_name='professor')

class Class(models.Model):
    Course=models.ForeignKey('university.Course',
related_name='university_classes',
on_delete=models.CASCADE)

students=models.ManyToManyField('university.student',
related_name='classes')

