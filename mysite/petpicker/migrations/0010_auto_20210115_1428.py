# Generated by Django 3.1.5 on 2021-01-15 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petpicker', '0009_mymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petpicker_model',
            name='Init_Price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='petpicker_model',
            name='Lenght',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='petpicker_model',
            name='Life_Span',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='petpicker_model',
            name='Main_Cost',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='petpicker_model',
            name='Main_Time',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='petpicker_model',
            name='Max_Space',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='petpicker_model',
            name='Trainable',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='petpicker_model',
            name='Weight',
            field=models.FloatField(default=0),
        ),
    ]
