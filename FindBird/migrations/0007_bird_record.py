# Generated by Django 3.2 on 2021-05-08 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindBird', '0006_remove_bird_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='bird',
            name='record',
            field=models.FileField(default='', upload_to='FindBird/audio'),
        ),
    ]
