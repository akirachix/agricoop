# Generated by Django 3.2.8 on 2021-11-10 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group_details', '0006_alter_bean_details_beans_variety'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bean_details',
            name='beans_variety',
            field=models.CharField(choices=[('Bush beans', 'Bush beans'), ('Ruvuninkingi', 'Ruvuninkingi'), ('Climbing beans', 'Climbing beans')], max_length=30, null=True),
        ),
    ]
