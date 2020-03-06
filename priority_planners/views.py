from django.shortcuts import render

from .models import Goal, Update


def index(request):
    """The home page for Priority Planner."""
    return render(request, 'priority_planners/index.html')


def goals(request):
    """Show all goals."""
    goal_list = [goal for goal in Goal.objects.order_by('date_added') if goal.date_completed is None]
    finished = [goal for goal in Goal.objects.order_by('date_added') if goal.date_completed is not None]

    goal_updates = [goal.update_set.order_by('-date_added') for goal in goal_list]
    finished_updates = [goal.update_set.order_by('-date_added') for goal in finished]

    goals_and_updates = []
    finished_and_updates = []

    # Iterate through the goals and updates lists simultaneously
    for goal, update in zip(goal_list, goal_updates):
        goals_and_updates.append((goal, update))
    for goal, update in zip(finished, finished_updates):
        finished_and_updates.append((goal, update))

    context = {'goals': goals_and_updates, 'finished': finished_and_updates}
    return render(request, 'priority_planners/goals.html', context)


def goal(request, goal_id):
    """Show a single goal and it's updates"""
    goal = Goal.objects.get(id=goal_id)
    updates = goal.update_set.order_by('-date_added')
    context = {'goal': goal, 'updates': updates}
    return render(request, 'priority_planners/goal.html', context)
