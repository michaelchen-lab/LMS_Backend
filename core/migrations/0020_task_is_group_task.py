# Generated by Django 3.2.4 on 2023-07-20 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_task_is_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_group_task',
            field=models.BooleanField(default=False),
        ),
    ]