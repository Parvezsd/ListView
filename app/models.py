from django.db import models # type: ignore
from django.urls import reverse
# Create your models here.
class School(models.Model):
    scname = models.CharField(max_length=100)
    scaddress = models.CharField(max_length=100)
    scloc=models.CharField(max_length=100,null=True)
    scprincipal=models.CharField(max_length=100,default='Hello')
    def __str__(self):
        return self.scname
    def get_absolute_url(self):
        return reverse('SchoolDetail',kwargs={'pk':self.pk})
    
class Student(models.Model):
    stname = models.CharField(max_length=100)
    stage = models.IntegerField()
    staddress = models.CharField(max_length=100)
    # stphone = models.IntegerField()
    scname = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')
    def __str__(self):
        return self.stname
    
