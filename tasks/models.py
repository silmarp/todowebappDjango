from django.db import models
import datetime 

# Create your models here.

class Lists(models.Model):
    tittle = models.CharField(max_length=20)
    

class Task(models.Model):
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text
    