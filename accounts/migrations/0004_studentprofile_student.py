# Generated by Django 3.2.3 on 2021-05-28 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210528_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='student',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
