from django.db import models

# Create your models here.
class page(models.Model):
    student_name = models.CharField(max_length=100, null=True)
    student_Rollno = models.CharField(max_length=100,null=True)
    student_course = models.CharField(max_length=100,null=True)
    student_email = models.EmailField(null=True)


    def __str__(self):
        return self.student_name

