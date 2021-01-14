from django.db import models
from django_matplotlib import MatplotlibFigureField


# Create your models here.
class petpicker_Model(models.Model):
    Init_Price = models.IntegerField(default=0)
    Main_Time = models.IntegerField(default=0)
    Life_Span = models.IntegerField(default=0)
    Trainable = models.IntegerField(default=0)
    Main_Cost = models.IntegerField(default=0)
    Weight = models.IntegerField(default=0)
    Lenght = models.IntegerField(default=0)
    Max_Space = models.IntegerField(default=0)


class MyModel(models.Model):
    figure = MatplotlibFigureField(figure='my_figure')
