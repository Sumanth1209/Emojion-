from django.db import models
from datetime import datetime, date

# Create your models here.
class emo(models.Model):
    uname=models.CharField(max_length=50)
    passwd=models.CharField(max_length=40)
    emotion=models.IntegerField(blank=True,null=True)
    EU=models.CharField(max_length=20,blank=True,null=True)
    source=models.IntegerField(blank=True,null=True)
    date=models.DateField(auto_now_add=True,auto_now=False,blank=True)
    time=models.TimeField(auto_now_add=True,auto_now=False,blank=True)
    
    #picpath=models.URLField
    
    def __str__(self):
        return self.uname
