# Generated by Django 3.2.9 on 2022-03-11 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_contactdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactdetails',
            name='mobilenumber',
        ),
    ]