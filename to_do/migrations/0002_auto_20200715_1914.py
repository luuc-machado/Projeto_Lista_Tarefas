# Generated by Django 3.0.8 on 2020-07-15 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='is_completed',
        ),
        migrations.AlterField(
            model_name='task',
            name='is_checked',
            field=models.IntegerField(default=0),
        ),
    ]
