# Generated by Django 3.2.4 on 2023-07-20 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_task_is_group_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='is_group_task',
        ),
    ]