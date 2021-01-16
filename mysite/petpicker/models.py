from django.db import models
from django_matplotlib import MatplotlibFigureField


# Create your models here.
class petpicker_Model(models.Model):
    Init_Price = models.FloatField(default=0)
    Main_Time = models.FloatField(default=0)
    Life_Span = models.FloatField(default=0)
    Trainable = models.FloatField(default=0)
    Main_Cost = models.FloatField(default=0)
    Weight = models.FloatField(default=0)
    Lenght = models.FloatField(default=0)
    Max_Space = models.FloatField(default=0)
