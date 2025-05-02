from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    joined_in = models.DateTimeField(auto_now_add=True)
    course_name = models.CharField(max_length=200)
    course_period =models.IntegerField()
    student_number = models.CharField(max_length=8)
    address = models.CharField(max_length=50)
    def __str__(self):
        return f"${self.student_number}_{self.name}"
    
class Course_Available(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    course_period = models.IntegerField()
    def __str__(self):
        return self.title


class Instructor_Available(models.Model):
    Instructor_name = models.CharField(max_length=200)
    joined_in = models.DateTimeField(auto_now_add=True)
    course_assigned =models.ForeignKey('Course_Available',on_delete=models.SET_NULL,blank=True,null=True)
    instructor_number = models.CharField(max_length=5)
    address = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.instructor_number}_{self.Instructor_name}"
    




