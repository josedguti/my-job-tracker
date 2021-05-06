from django.db import models

# Create your models here.

class List(models.Model):
    companyname = models.CharField(max_length=255)
    date = models.DateField()
    contacted = models.BooleanField(default=False)
    interviewed = models.BooleanField(default=False)


    