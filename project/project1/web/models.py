from distutils.command.upload import upload
from django.db import models

# Create your models here.

# CRUD - 4
class Emp(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
 