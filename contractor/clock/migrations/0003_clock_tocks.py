# Generated by Django 2.2.6 on 2019-12-13 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clock', '0002_clock_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='clock',
            name='tocks',
            field=models.IntegerField(default=4),
        ),
    ]
