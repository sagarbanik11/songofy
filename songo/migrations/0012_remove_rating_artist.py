# Generated by Django 3.0.4 on 2020-03-31 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songo', '0011_auto_20200331_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='artist',
        ),
    ]
