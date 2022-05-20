from calendar import day_abbr
import code
from tkinter.tix import DisplayStyle
from django.db import models

# Create your models here.
class Course(models.Model):
    code = models.IntegerField(max_length=6)
    days = models.CharField(max_length=20)
    starttime = models.IntegerField(max_length=4)
    endtime = models.IntegerField(max_length=4)
    location = models.CharField(max_length=15)