from django.db import models # type: ignore

# Create your models here.
class School(models.Model):
    scname = models.CharField(max_length=100)
    scaddress = models.CharField(max_length=100)
    # scphone = models.IntegerField()
    def __str__(self):
        return self.scname
    
class Student(models.Model):
    stname = models.CharField(max_length=100)
    stage = models.IntegerField()
    staddress = models.CharField(max_length=100)
    # stphone = models.IntegerField()
    scname = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')
    def __str__(self):
        return self.stname
    
