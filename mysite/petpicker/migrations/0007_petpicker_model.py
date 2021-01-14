# Generated by Django 3.1.5 on 2021-01-14 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('petpicker', '0006_delete_petpicker_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='petpicker_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Init_Price', models.IntegerField()),
                ('Main_Time', models.IntegerField()),
                ('Life_Span', models.IntegerField()),
                ('Trainable', models.IntegerField()),
                ('Main_Cost', models.IntegerField()),
                ('Weight', models.IntegerField()),
                ('Lenght', models.IntegerField()),
                ('Max_Space', models.IntegerField()),
            ],
        ),
    ]