# Generated by Django 2.2.1 on 2019-05-08 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='site',
        ),
        migrations.AddField(
            model_name='item',
            name='site',
            field=models.ManyToManyField(to='mainboard.Site'),
        ),
    ]
