# Generated by Django 3.2.8 on 2021-11-11 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group_details', '0012_auto_20211110_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivaries',
            name='group_name',
        ),
        migrations.AlterField(
            model_name='delivaries',
            name='beans_variety',
            field=models.CharField(choices=[('Bush beans', 'Bush beans'), ('Climbing beans', 'Climbing beans'), ('Ruvuninkingi', 'Ruvuninkingi')], max_length=200, null=True),
        ),
    ]
