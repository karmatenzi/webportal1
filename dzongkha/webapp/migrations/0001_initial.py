# Generated by Django 3.2.9 on 2022-02-27 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DzongkhaWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phelkay', models.CharField(max_length=70)),
                ('zhebsa', models.CharField(max_length=70)),
                ('phrases', models.CharField(max_length=150)),
                ('audio', models.FileField(upload_to='document/')),
            ],
        ),
    ]
