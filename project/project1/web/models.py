from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Destination(models.Model): 
    name = models.CharField(max_length=200) 
    fname =  models.CharField(max_length=100)
    img =  models.ImageField(upload_to='pics')
    bon =  models.BooleanField
 