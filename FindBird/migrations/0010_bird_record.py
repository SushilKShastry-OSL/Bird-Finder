# Generated by Django 3.2 on 2021-05-16 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindBird', '0009_auto_20210516_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='bird',
            name='record',
            field=models.FileField(default='', upload_to='FindBird/audio'),
        ),
    ]
