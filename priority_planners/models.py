from django.db import models
from colorful.fields import RGBColorField


class Goal(models.Model):
    """A Goal the user wants to complete."""
    parent = None
    children = []
    color = RGBColorField()
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_completed = None


class Update(models.Model):
    """A note regarding a specific goal."""
    parent = models.ForeignKey(Goal, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 40:
            return f"{self.text[:50]}..."
        else:
            return self.text
