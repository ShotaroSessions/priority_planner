# Generated by Django 3.0.3 on 2020-03-06 04:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('priority_planners', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
