from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'is_completed', 'is_important', 'due_date']
    list_filter = ['is_completed', 'is_important']
    search_fields = ['title', 'description']
