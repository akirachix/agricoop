from django.db import models



class Group_list(models.Model):
    group_name=models.CharField(max_length=100)
    no_of_group_member=models.PositiveSmallIntegerField(null=True)
    group_leader_contact=models.CharField(max_length=20,blank=True, null=True )

