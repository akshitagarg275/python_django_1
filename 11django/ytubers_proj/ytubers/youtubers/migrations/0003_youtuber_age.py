# Generated by Django 4.0.5 on 2022-07-07 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0002_alter_youtuber_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtuber',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
