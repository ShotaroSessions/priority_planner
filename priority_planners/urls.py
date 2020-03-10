"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views


app_name = 'priority_planners'
urlpatterns= [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all goals.
    path('goals/', views.goals, name='goals'),
    # Page that details a goal
    path('goals/<int:goal_id>/', views.goal, name='goal'),
    # Page that details an update
    path('updates/<int:update_id>/', views.update, name='update'),
    # Page for adding a new goal
    path('new_goal/', views.new_goal, name='new_goal'),
    # Page for adding a new update
    path('new_update/<int:goal_id>/', views.new_update, name='new_update'),
    # Page for editing an goal
    path('edit_goal/<int:goal_id>/', views.edit_goal, name='edit_goal'),
    # Path for editing an update
    path('edit_update/<int:update_id>/', views.edit_update, name='edit_update'),
    # Path for deleting a goal
    path('delete_goal/<int:goal_id>/', views.delete_goal, name='delete_goal'),
    # Path for deleting an update
    path('delete_update/<int:update_id>/', views.delete_update, name='delete_update'),
    # Path for finishing a goal
    path('finish_goal/<int:goal_id>/', views.finish_goal, name='finish_goal'),

]
