from django import forms

from .models import Goal, Update


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'text']
        labels = {'title': '', 'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}



