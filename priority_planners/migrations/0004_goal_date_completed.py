# Generated by Django 3.0.3 on 2020-03-10 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('priority_planners', '0003_update_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='date_completed',
            field=models.DateTimeField(null=True),
        ),
    ]
