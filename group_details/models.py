from django.db import models
import datetime


class Delivaries(models.Model):
    group_name_choice= (
        ('Iwacu group','Iwacu group'),
        ('Komera cooperative','Komera cooperative'),
        ('Ubwiyunge cooperative','Ubwiyunge cooperative'),
        )
    group_name=models.CharField(max_length=200,choices= group_name_choice,null=True)

    beans_variety_choice=(
        ('Bush Beans','Bush Beans'),
        ('Climbing Beans','Climbing Beans'),
        ('Ruvuninkingi','Ruvuninkingi')
    )
    beans_variety = models.CharField(max_length=800, choices= beans_variety_choice,null=True)

    date_of_delivery=models.DateTimeField(null=True)

    kgs_of_beans= models.PositiveSmallIntegerField(null=True)
