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
]
