# Generated by Django 3.2.3 on 2021-05-30 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210527_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='student_indexes',
            field=models.JSONField(default=[]),
        ),
    ]
