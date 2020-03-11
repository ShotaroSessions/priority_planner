from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import Http404

from .models import Goal, Update
from .forms import GoalForm, UpdateForm


def index(request):
    """The home page for Priority Planner."""
    return render(request, 'priority_planners/index.html')


@login_required
def goals(request):
    """Show all goals with their updates."""
    goals_all = Goal.objects.filter(owner=request.user).order_by('date_added')
    goal_list = [goal for goal in goals_all if goal.completed is False]
    finished = [goal for goal in goals_all if goal.completed is True]

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


@login_required
def goal(request, goal_id):
    """Show a single goal and it's updates"""
    goal = get_object_or_404(Goal, id=goal_id)
    # Make sure the goal belongs to the current user.
    if goal.owner != request.user:
        raise Http404

    updates = goal.update_set.order_by('-date_added')
    context = {'goal': goal, 'updates': updates}
    return render(request, 'priority_planners/goal.html', context)


@login_required
def update(request, update_id):
    """Show a single update and it's text"""
    update = get_object_or_404(Update, id=update_id)
    if update.parent.owner != request.user:
        raise Http404
    context = {'update': update}
    return render(request, 'priority_planners/update.html', context)


@login_required
def new_goal(request):
    """Add a new goal."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = GoalForm()
    else:
        # POST data submitted; process data.
        form = GoalForm(data=request.POST)
        if form.is_valid():
            new_goal = form.save(commit=False)
            new_goal.owner = request.user
            new_goal.save()
            return redirect('priority_planners:goals')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'priority_planners/new_goal.html', context)


@login_required
def new_update(request, goal_id):
    """ Add a new update for a particular goal"""
    goal = get_object_or_404(Goal, id=goal_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = UpdateForm()
    else:
        # POST data submitted; process data.
        form = UpdateForm(data=request.POST)
        if form.is_valid():
            new_update = form.save(commit=False)
            new_update.parent = goal
            if goal.owner != request.user:
                raise Http404
            new_update.save()
            return redirect('priority_planners:goal', goal_id=goal_id)

    # Display a blank or invalid form
    context = {'goal': goal, 'form': form}
    return render(request, 'priority_planners/new_update.html', context)


@login_required
def edit_goal(request, goal_id):
    """Edit an existing goal"""
    goal = get_object_or_404(Goal, id=goal_id)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current goal.
        form = GoalForm(instance=goal)
    else:
        # Post data submitted; process data.
        form = GoalForm(instance=goal, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('priority_planners:goal', goal_id=goal.id)

    context = {'goal': goal, 'form': form}
    return render(request, 'priority_planners/edit_goal.html', context)


@login_required
def edit_update(request, update_id):
    """Edit an existing update"""
    update = get_object_or_404(Update, id=update_id)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current update.
        form = UpdateForm(instance=update)
    else:
        # Post data submitted; process data.
        form = UpdateForm(instance=update, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('priority_planners:update', update_id=update.id)

    context = {'update': update, 'form': form}
    return render(request, 'priority_planners/edit_update.html', context)


@login_required
def delete_goal(request, goal_id):
    """Delete an existing goal"""
    goal = get_object_or_404(Goal, id=goal_id)
    if request.method == 'POST':
        # confirming delete
        goal.delete()
        return redirect('priority_planners:goals')
    context = {
        "goal": goal
    }
    return render(request, 'priority_planners/delete_goal.html', context)


@login_required
def delete_update(request, update_id):
    """Delete an existing update"""
    update = get_object_or_404(Update, id=update_id)
    if request.method == 'POST':
        # confirming delete
        update.delete()
        return redirect('priority_planners:goals')
    context = {
        "update": update
    }
    return render(request, 'priority_planners/delete_update.html', context)


@login_required
def finish_goal(request, goal_id):
    """Finish an existing goal"""
    goal = get_object_or_404(Goal, id=goal_id)
    if request.method == 'POST':
        # confirming finish
        goal.date_completed = timezone.now()
        goal.completed = True
        goal.save()
        return redirect('priority_planners:goals')
    context = {
        "goal": goal
    }
    return render(request, 'priority_planners/finish_goal.html', context)
