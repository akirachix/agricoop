from django.db import models

class Group_list(models.Model):
    group_name=models.CharField(max_length=100)
    number_of_group_members=models.PositiveSmallIntegerField()