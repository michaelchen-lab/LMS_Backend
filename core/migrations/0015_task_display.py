# Generated by Django 3.2.4 on 2022-07-12 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_remove_resource_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='display',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Published'), (2, 'Draft')], default=1),
        ),
    ]
