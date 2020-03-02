from django.db import models
from colorful.fields import RGBColorField


class Goal(models.Model):
    """A Goal the user wants to complete."""
    parent = None
    children  = []
    color = RGBColorField()
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_completed = None

