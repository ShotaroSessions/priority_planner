# Generated by Django 3.0.3 on 2020-03-10 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('priority_planners', '0004_goal_date_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]