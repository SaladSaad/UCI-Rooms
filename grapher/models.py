from calendar import day_abbr
import code
from tkinter.tix import DisplayStyle
from django.db import models

# Create your models here.
class Course(models.Model):
    code = models.IntegerField()
    days = models.CharField(max_length=20)
    starttime = models.IntegerField()
    endtime = models.IntegerField()
    location = models.CharField(max_length=15)

    def __str__(self):
        return self.code, self.location
