# Generated by Django 3.2.8 on 2021-11-04 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group_list',
            fields=[
                ('group_name', models.CharField(max_length=100)),
                ('no_of_members', models.PositiveSmallIntegerField()),
                ('profile', models.ImageField(default='default.jpg', null=True, upload_to='static/images')),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('phone_number', models.CharField(max_length=100)),
            ],
        ),
    ]