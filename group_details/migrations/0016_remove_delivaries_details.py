# Generated by Django 3.2.8 on 2021-11-11 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group_details', '0015_delivaries_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivaries',
            name='details',
        ),
    ]