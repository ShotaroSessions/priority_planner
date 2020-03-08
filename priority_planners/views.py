from django.shortcuts import render, redirect

from .models import Goal, Update
from .forms import GoalForm

def index(request):
    """The home page for Priority Planner."""
    return render(request, 'priority_planners/index.html')


def goals(request):
    """Show all goals with their updates."""
    goals_all = Goal.objects.order_by('date_added')
    goal_list = [goal for goal in goals_all if goal.date_completed is None]
    finished = [goal for goal in goals_all if goal.date_completed is not None]

    goal_updates = [goal.update_set.order_by('-date_added')
                    for goal in goal_list]
    finished_updates = [goal.update_set.order_by('-date_added')
                        for goal in finished]

    # Lists of tuples containing goals and a list of their updates
    goals_and_updates = [(goal, updates) for goal, updates
                         in zip(goal_list, goal_updates)]
    finished_and_updates = [(goal, updates) for goal, updates
                            in zip(finished, finished_updates)]

    context = {'goals': goals_and_updates, 'finished': finished_and_updates}
    return render(request, 'priority_planners/goals.html', context)


def goal(request, goal_id):
    """Show a single goal and it's updates"""
    goal = Goal.objects.get(id=goal_id)
    updates = goal.update_set.order_by('-date_added')
    context = {'goal': goal, 'updates': updates}
    return render(request, 'priority_planners/goal.html', context)


def update(request, update_id):
    """Show a single update and it's text"""
    update = Update.objects.get(id=update_id)
    context = {'update': update}
    return render(request, 'priority_planners/update.html', context)

def new_goal(request):
    """Add a new goal."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = GoalForm()
    else:
        # POST data submitted; process data
        form = GoalForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('priority_planners:goals')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'priority_planners/new_goal.html', context)
