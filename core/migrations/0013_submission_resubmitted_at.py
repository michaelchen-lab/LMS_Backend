# Generated by Django 3.2.4 on 2022-04-07 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20220406_0251'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='resubmitted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]