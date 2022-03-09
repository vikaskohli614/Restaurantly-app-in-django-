import email
from email import message
from unicodedata import name
from django.db import models

# Create your models here.
class tablebook(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    date=models.DateField()
    time=models.TimeField()
    people=models.CharField(max_length=20)
    message=models.TextField()

class contactus(models.Model):
    cname=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    subject=models.CharField(max_length=122)
    message=models.TextField()