from django.db import models
from django.contrib.auth.models import User
from colorful.fields import RGBColorField


class Goal(models.Model):
    """A Goal the user wants to complete."""
    parent = None
    color = RGBColorField()
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model"""
        return self.title


class Update(models.Model):
    """A note regarding a specific goal."""
    parent = models.ForeignKey(Goal, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.title
