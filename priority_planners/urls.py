"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'priority_planners'
urlpatterns= [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all goals.
    path('goals/', views.goals, name='goals'),
]
