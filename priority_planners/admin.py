from django.contrib import admin

from .models import Goal
from .models import Update

admin.site.register(Goal)
admin.site.register(Update)