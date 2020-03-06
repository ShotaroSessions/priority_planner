from django.shortcuts import render

from .models import Goal

def index(request):
    """The home page for Priority Planner."""
    return render(request, 'priority_planners/index.html')

def goals(request):
    """Show all goals."""
    goals = Goal.objects.order_by('date_added')
    context = {'goals' : goals}
    return render(request, 'priority_planners/goals.html', context)