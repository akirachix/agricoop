# Generated by Django 3.2.8 on 2021-11-17 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group_details', '0005_auto_20211117_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivaries',
            name='date_delivaries',
        ),
        migrations.AddField(
            model_name='delivaries',
            name='date_of_delivery',
            field=models.DateTimeField(null=True),
        ),
    ]
