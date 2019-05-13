# Generated by Django 2.2.1 on 2019-05-12 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainboard', '0005_config_period'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='config',
            name='site',
        ),
        migrations.AddField(
            model_name='site',
            name='config',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainboard.Config'),
            preserve_default=False,
        ),
    ]