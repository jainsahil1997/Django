from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name=models.CharField(max_length=50)
    def __str__(self):
        return self.dept_name

class Subject (models.Model):
    sub_name=models.CharField(max_length=50)
    dept_name=models.ForeignKey(Department,on_delete=models.CASCADE,blank=True, null=True)
    code=models.CharField(max_length=50)
    def __str__(self):
        return self.sub_name

class Material (models.Model):
    code=models.ForeignKey(Subject,on_delete=models.CASCADE)
    ppt=models.CharField(max_length=1000)
    notes=models.CharField(max_length=1000)
    past_papers=models.CharField(max_length=1000)
