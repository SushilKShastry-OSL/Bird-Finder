# Generated by Django 3.2 on 2021-05-07 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FindBird', '0002_rename_character_bird'),
    ]

    operations = [
        migrations.AddField(
            model_name='bird',
            name='paragraph2',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='bird',
            name='paragraph3',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='bird',
            name='paragraph',
            field=models.TextField(default=None),
        ),
    ]
