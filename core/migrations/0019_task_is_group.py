# Generated by Django 3.2.4 on 2023-07-12 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_delete_enroll'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_group',
            field=models.BooleanField(default=False),
        ),
    ]