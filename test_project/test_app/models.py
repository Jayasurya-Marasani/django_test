from django.db import models

# Create your models here.
# Program
class Program(models.Model):
    title = models.CharField(max_length=20)
    branch = models.CharField(max_length=50)
 
    def __str__(self):
        return self.title + self.branch
# Student
class Student(models.Model):
    roll_number = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    year = models.IntegerField(default=1)
    dob = models.DateField('date of birth')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    # __str__ function   
    def __str__(self):
        d = self.program
        return self.roll_number + self.name  + d.title + d. branch