# Generated by Django 3.0.4 on 2020-03-29 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songo', '0002_song_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='a_id',
            field=models.IntegerField(max_length=20),
        ),
    ]
