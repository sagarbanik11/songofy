# Generated by Django 3.0.4 on 2020-03-29 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songo', '0003_auto_20200329_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(upload_to='pics/%Y/%m/%d/'),
        ),
    ]