# Generated by Django 4.0.5 on 2022-06-23 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qoshiq',
            name='eshit',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='qoshiq',
            name='file',
            field=models.URLField(default=0),
        ),
    ]