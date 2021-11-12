# Generated by Django 3.2.8 on 2021-11-09 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
        ('group_details', '0003_alter_bean_details_beans_variety'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bean_details',
            name='beans_variety',
            field=models.ForeignKey(choices=[('Bush Beans', 'Bush Beans'), ('Climbing Beans', 'Climbing Beans'), ('Ruvuninkingi', 'Ruvuninkingi')], null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.payments'),
        ),
    ]